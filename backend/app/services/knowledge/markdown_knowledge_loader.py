"""
AYDI Markdown Knowledge Loader
===============================

Parses structured markdown knowledge files (04_xx, 05_xx, 06_xx series)
into Python dictionaries compatible with the existing knowledge retrieval
infrastructure.

Each markdown file is parsed into:
- Metadata (title, category, subcategory)
- Structured data (tables → list of dicts)
- Pydantic model definitions (extracted but not executed)
- Manufacturer database (names, products, prices, availability)
- Erfahrungsberichte (experience reports with sources)
- Expert references
- FAQ entries
- Glossary terms
- Fehlerbilder (failure patterns with symptoms, causes, remedies)
- Fallstudien (case studies)
- Confidence mappings

All data is exposed as uppercase constants matching the existing module pattern.
"""

import os
import re
import logging
from typing import Dict, List, Any, Optional, Tuple
from pathlib import Path

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Path to knowledge markdown files
# ---------------------------------------------------------------------------
KNOWLEDGE_DIR = Path(__file__).parent
MARKDOWN_FILES_PATTERN = re.compile(r"^\d{2}_\d{2}_.*\.md$")

# ---------------------------------------------------------------------------
# Markdown Parsing Utilities
# ---------------------------------------------------------------------------


def _find_markdown_files() -> List[Path]:
    """Discover all numbered markdown knowledge files in the knowledge dir."""
    files = []
    for f in sorted(KNOWLEDGE_DIR.iterdir()):
        if f.is_file() and MARKDOWN_FILES_PATTERN.match(f.name):
            files.append(f)
    return files


def _parse_markdown_table(lines: List[str]) -> List[Dict[str, str]]:
    """
    Parse a markdown table into a list of dicts.
    Handles: | Header1 | Header2 | ... |
             |---------|---------|-----|
             | val1    | val2    | ... |
    """
    if len(lines) < 3:
        return []

    # Extract headers
    header_line = lines[0].strip()
    if not header_line.startswith("|"):
        return []

    headers = [h.strip() for h in header_line.split("|") if h.strip()]

    # Skip separator line (line[1])
    rows = []
    for line in lines[2:]:
        line = line.strip()
        if not line.startswith("|"):
            break
        cells = [c.strip() for c in line.split("|") if c.strip() != ""]
        if len(cells) >= 1:
            row = {}
            for i, header in enumerate(headers):
                row[header] = cells[i] if i < len(cells) else ""
            rows.append(row)

    return rows


def _extract_section_hierarchy(content: str) -> Dict[str, Any]:
    """
    Parse markdown into a hierarchy of sections.
    Returns nested dict: {title, level, content, subsections[], tables[]}
    """
    lines = content.split("\n")
    root = {
        "title": "",
        "level": 0,
        "content_lines": [],
        "subsections": [],
        "tables": [],
    }
    stack = [root]

    i = 0
    while i < len(lines):
        line = lines[i]

        # Detect heading
        heading_match = re.match(r"^(#{1,6})\s+(.+)$", line)
        if heading_match:
            level = len(heading_match.group(1))
            title = heading_match.group(2).strip()

            section = {
                "title": title,
                "level": level,
                "content_lines": [],
                "subsections": [],
                "tables": [],
            }

            # Pop stack to find parent
            while len(stack) > 1 and stack[-1]["level"] >= level:
                stack.pop()

            stack[-1]["subsections"].append(section)
            stack.append(section)
            i += 1
            continue

        # Detect table
        if line.strip().startswith("|") and i + 1 < len(lines):
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_lines.append(lines[i])
                i += 1
            if len(table_lines) >= 3:
                table_data = _parse_markdown_table(table_lines)
                if table_data and stack:
                    stack[-1]["tables"].append(table_data)
            continue

        # Regular content line
        if stack:
            stack[-1]["content_lines"].append(line)
        i += 1

    return root


def _extract_erfahrungsberichte(content: str) -> List[Dict[str, str]]:
    """Extract experience reports (Erfahrungsbericht) from markdown.

    Handles two formats:
    - New: **Erfahrungsbericht — Source:** followed by blockquote
    - Old: Forum-Threads tables with | Thread | Thema | Kernerkenntnis |
           Also: sections like "## XX. Forum-Threads & Eigner-Erfahrungen"
           or "## XX. Eigner-Erfahrungsberichte und Forum-Konsens"
           or "## XX. Praxisberichte und Forum-Konsens"
    """
    reports = []

    # --- Pattern 1: New-style **Erfahrungsbericht — Source:** blockquote ---
    pattern_new = re.compile(
        r"\*\*Erfahrungsbericht\s*—\s*(.+?):\*\*\s*\n>\s*\"(.+?)\"",
        re.DOTALL,
    )
    for match in pattern_new.finditer(content):
        source = match.group(1).strip()
        text = match.group(2).strip().replace("\n> ", " ")
        forum_match = re.match(
            r"(.+?),\s*User\s+[\"']?(.+?)[\"']?(?:,\s*(\d{4}))?$", source
        )
        if forum_match:
            reports.append({
                "source": forum_match.group(1).strip(),
                "user": forum_match.group(2).strip(),
                "year": forum_match.group(3) or "",
                "text": text,
                "type": "forum",
            })
        else:
            reports.append({
                "source": source,
                "user": "",
                "year": "",
                "text": text,
                "type": "other",
            })

    # --- Pattern 2: Old-style forum tables with Kernerkenntnis column ---
    # Find sections about forum threads / eigner-erfahrungen
    forum_section_pattern = re.compile(
        r"##\s+\d+\.?\s*(?:Forum-Threads|Eigner-Erfahrungsberichte|"
        r"Praxisberichte|Langzeit-Erfahrungsberichte)[^\n]*\n"
        r"(.+?)(?=\n##\s+\d+|\n##\s+ANHANG|\Z)",
        re.DOTALL | re.IGNORECASE,
    )
    for section_match in forum_section_pattern.finditer(content):
        section_content = section_match.group(1)
        # Extract forum name from ### headings
        current_forum = "Forum"
        lines = section_content.split("\n")
        i = 0
        while i < len(lines):
            line = lines[i]
            # Detect forum subsection heading
            forum_heading = re.match(
                r"###\s+[\d.]*\s*(.+?)(?:\s*\(.+\))?\s*$", line
            )
            if forum_heading:
                current_forum = forum_heading.group(1).strip()

            # Detect table with Kernerkenntnis
            if line.strip().startswith("|") and "Kernerkenntnis" in line:
                # Parse this table
                table_lines = []
                while i < len(lines) and lines[i].strip().startswith("|"):
                    table_lines.append(lines[i])
                    i += 1
                rows = _parse_markdown_table(table_lines)
                for row in rows:
                    kern = row.get("Kernerkenntnis", "").strip()
                    thread = row.get("Thread", row.get("Thema", "")).strip()
                    if kern:
                        # Clean quotes
                        kern = kern.strip('"').strip("'").strip(""").strip(""")
                        reports.append({
                            "source": current_forum,
                            "user": "",
                            "year": "",
                            "text": f"{thread}: {kern}" if thread else kern,
                            "type": "forum",
                        })
                continue
            i += 1

    return reports


def _extract_expert_references(content: str) -> List[Dict[str, str]]:
    """Extract expert references from markdown.

    Handles two formats:
    - New: **Experten-Referenz — Source:** followed by blockquote
    - Old: Tables in "Experten-Meinungen" / "Fachliteratur und Experten" sections
           with columns like Autor/Experte, Werk/Buch/Fokus, Relevanz/Kernaussage
    """
    refs = []

    # --- Pattern 1: New-style **Experten-Referenz — Source:** ---
    pattern_new = re.compile(
        r"\*\*Experten-Referenz\s*—\s*(.+?):\*\*\s*\n>\s*\"(.+?)\"",
        re.DOTALL,
    )
    for match in pattern_new.finditer(content):
        source = match.group(1).strip()
        text = match.group(2).strip().replace("\n> ", " ")
        refs.append({"source": source, "text": text})

    # --- Pattern 2: Old-style expert/literature tables ---
    expert_section_pattern = re.compile(
        r"##\s+\d+\.?\s*(?:Experten-Meinungen|Fachliteratur und Experten|"
        r"Experten und Fachliteratur)[^\n]*\n"
        r"(.+?)(?=\n##\s+\d+|\n##\s+ANHANG|\Z)",
        re.DOTALL | re.IGNORECASE,
    )
    for section_match in expert_section_pattern.finditer(content):
        section_content = section_match.group(1)
        lines = section_content.split("\n")
        i = 0
        while i < len(lines):
            line = lines[i]
            # Find tables with expert info
            if line.strip().startswith("|") and i + 2 < len(lines):
                header_lower = line.lower()
                if any(kw in header_lower for kw in [
                    "autor", "experte", "name", "werk", "buch", "kanal",
                    "fokus", "kernaussage", "relevanz"
                ]):
                    table_lines = []
                    while i < len(lines) and lines[i].strip().startswith("|"):
                        table_lines.append(lines[i])
                        i += 1
                    rows = _parse_markdown_table(table_lines)
                    for row in rows:
                        # Build source from author/name columns
                        source_parts = []
                        text_parts = []
                        for key, val in row.items():
                            key_lower = key.lower().strip().strip("*")
                            if not val.strip():
                                continue
                            if any(k in key_lower for k in [
                                "autor", "experte", "name", "kanal"
                            ]):
                                source_parts.append(val.strip().strip("*"))
                            elif any(k in key_lower for k in [
                                "werk", "buch", "titel"
                            ]):
                                source_parts.append(val.strip())
                            elif any(k in key_lower for k in [
                                "kernaussage", "relevanz", "fokus",
                                "beitrag", "thema"
                            ]):
                                text_parts.append(val.strip())
                        if source_parts:
                            refs.append({
                                "source": " — ".join(source_parts),
                                "text": "; ".join(text_parts) if text_parts else "",
                            })
                    continue
            i += 1

    return refs


def _extract_faq(content: str) -> List[Dict[str, str]]:
    """Extract FAQ entries from markdown.

    Handles multiple formats:
    - New: ### FAQ 1: Question
    - Old: ### F1: Question  (under ## XX. FAQ — Häufige Fragen)
    - Old: ### XX.1 Question  (numbered subsections under FAQ heading)
    """
    faqs = []
    seen_questions = set()

    # --- Pattern 1: New-style ### FAQ N: Question ---
    pattern_new = re.compile(
        r"###\s+FAQ\s+\d+:\s*(.+?)\n(.+?)(?=###\s+FAQ\s+\d+|\n---|\n##\s|\Z)",
        re.DOTALL,
    )
    for match in pattern_new.finditer(content):
        question = match.group(1).strip()
        answer = match.group(2).strip()
        conf_match = re.search(r"\(Confidence:\s*(\w+)\)", answer)
        confidence = conf_match.group(1) if conf_match else "documented"
        if question not in seen_questions:
            seen_questions.add(question)
            faqs.append({
                "question_de": question,
                "answer_de": answer,
                "confidence": confidence,
            })

    # --- Pattern 2: Old-style ### F1: Question (short prefix) ---
    pattern_f = re.compile(
        r"###\s+F(\d+):\s*(.+?)\n(.+?)(?=###\s+F\d+:|\n---|\n##\s|\Z)",
        re.DOTALL,
    )
    for match in pattern_f.finditer(content):
        question = match.group(2).strip()
        answer = match.group(3).strip()
        conf_match = re.search(r"\(Confidence:\s*(\w+)\)", answer)
        confidence = conf_match.group(1) if conf_match else "documented"
        if question not in seen_questions:
            seen_questions.add(question)
            faqs.append({
                "question_de": question,
                "answer_de": answer,
                "confidence": confidence,
            })

    # --- Pattern 3: Old-style numbered subsections under FAQ heading ---
    # Find the FAQ section first
    faq_section = re.search(
        r"##\s+\d+\.?\s*FAQ\s*[—–-]\s*(?:Häufige?\s+(?:Fragen|gestellte))[^\n]*\n"
        r"(.+?)(?=\n##\s+\d+|\n##\s+ANHANG|\Z)",
        content, re.DOTALL | re.IGNORECASE,
    )
    if faq_section:
        faq_content = faq_section.group(1)
        # Match ### XX.N Question or ### N. Question
        sub_pattern = re.compile(
            r"###\s+(?:\d+\.)?\d+\.?\s*(.+?)\n(.+?)(?=###\s+|\Z)",
            re.DOTALL,
        )
        for match in sub_pattern.finditer(faq_content):
            question = match.group(1).strip()
            answer = match.group(2).strip()
            # Skip if it's not really a question (section headings etc)
            if len(answer) < 10:
                continue
            conf_match = re.search(r"\(Confidence:\s*(\w+)\)", answer)
            confidence = conf_match.group(1) if conf_match else "documented"
            if question not in seen_questions:
                seen_questions.add(question)
                faqs.append({
                    "question_de": question,
                    "answer_de": answer,
                    "confidence": confidence,
                })

    return faqs


def _extract_glossary(content: str) -> List[Dict[str, str]]:
    """Extract glossary entries from the Glossar section.

    Handles multiple formats:
    - New: ## Glossar with table (DE | EN | Definition columns)
    - Old: ## XX. Glossar with table (Begriff | Erklärung columns)
    - Old: ## ANHANG D — Glossar with table
    """
    glossary = []

    # Find ALL Glossar sections (various heading formats)
    glossar_patterns = [
        # New: ## Glossar
        r"##\s+Glossar\s*\n(.+?)(?=\n##\s|\Z)",
        # Old: ## 40. Glossar
        r"##\s+\d+\.?\s*Glossar\s*\n(.+?)(?=\n##\s|\Z)",
        # Old: ## ANHANG X — Glossar
        r"##\s+ANHANG\s+\w+\s*[—–-]\s*Glossar\s*\n(.+?)(?=\n##\s|\Z)",
    ]

    glossar_content = ""
    for pat in glossar_patterns:
        match = re.search(pat, content, re.DOTALL | re.IGNORECASE)
        if match:
            glossar_content = match.group(1)
            break

    if not glossar_content:
        return glossary

    lines = glossar_content.strip().split("\n")

    # Parse ALL tables in the glossar section
    i = 0
    while i < len(lines):
        if lines[i].strip().startswith("|"):
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_lines.append(lines[i])
                i += 1
            if len(table_lines) >= 3:
                rows = _parse_markdown_table(table_lines)
                for row in rows:
                    entry = {}
                    for key, val in row.items():
                        key_lower = key.lower().strip().strip("*")
                        val_clean = val.strip().strip("*")
                        if not val_clean:
                            continue
                        # Term DE: "DE", "Begriff", "Begriff (DE)", "term"
                        if key_lower in ("de", "begriff", "term") or \
                           ("begriff" in key_lower and "en" not in key_lower):
                            entry["term_de"] = val_clean
                        elif key_lower == "en" or "english" in key_lower or \
                             ("begriff" in key_lower and "(en)" in key_lower):
                            entry["term_en"] = val_clean
                        elif "definition" in key_lower or "erklärung" in key_lower or "erklaerung" in key_lower:
                            entry["definition"] = val_clean
                        elif "term_de" not in entry and "de" not in key_lower:
                            # First unrecognized column with bold text is likely term
                            if val.strip().startswith("**"):
                                entry["term_de"] = val_clean
                    if entry.get("term_de"):
                        glossary.append(entry)
            continue
        i += 1

    return glossary


def _extract_fehlerbilder(content: str) -> List[Dict[str, str]]:
    """Extract Fehlerbild (failure pattern) entries.

    Handles multiple formats:
    - New: ### Fehlerbild N: Title  (with **Symptom:**, **Ursache:** etc)
    - Old: ### F1: Title  (under ANHANG F — Fehlerbild-Atlas, with **Bild:**, **Ursache:** etc)
    - Old: ### E.1 Fehlerbild 1: Title  (under ANHANG E — Fehlerbild-Atlas)
    - Old: ## XX. Schadensbilder & Versagensmechanismen sections
    """
    fehlerbilder = []
    seen_titles = set()

    def _parse_fehlerbild_body(title: str, body: str):
        """Parse a fehlerbild body with various field formats."""
        if title in seen_titles:
            return
        seen_titles.add(title)
        entry = {"title_de": title, "full_text": body}
        for field, patterns in [
            ("symptom_de", [
                r"\*\*Symptom:\*\*\s*(.+?)(?=\n\*\*|\Z)",
                r"\*\*Bild:\*\*\s*(.+?)(?=\n\*\*|\Z)",
            ]),
            ("ursache_de", [
                r"\*\*Ursache:\*\*\s*(.+?)(?=\n\*\*|\Z)",
            ]),
            ("haeufigkeit_de", [
                r"\*\*Häufigkeit:\*\*\s*(.+?)(?=\n\*\*|\Z)",
                r"\*\*Dringlichkeit:\*\*\s*(.+?)(?=\n\*\*|\Z)",
            ]),
            ("massnahme_de", [
                r"\*\*Maßnahme:\*\*\s*(.+?)(?=\n\*\*|\Z)",
                r"\*\*Erkennung:\*\*\s*(.+?)(?=\n\*\*|\Z)",
            ]),
            ("material_de", [
                r"\*\*Material:\*\*\s*(.+?)(?=\n\*\*|\Z)",
            ]),
            ("confidence", [
                r"\*\*Confidence:\*\*\s*(.+?)(?=\n|\Z)",
            ]),
        ]:
            for pat in patterns:
                field_match = re.search(pat, body, re.DOTALL)
                if field_match:
                    entry[field] = field_match.group(1).strip()
                    break
        fehlerbilder.append(entry)

    # --- Pattern 1: New-style ### Fehlerbild N: Title ---
    for match in re.finditer(
        r"###\s+Fehlerbild\s+\d+:\s*(.+?)\n(.+?)(?=###\s+Fehlerbild|\n---|\n##\s|\Z)",
        content, re.DOTALL,
    ):
        _parse_fehlerbild_body(match.group(1).strip(), match.group(2).strip())

    # --- Pattern 2: ANHANG F/E — Fehlerbild-Atlas subsections ---
    # Find the Fehlerbild-Atlas ANHANG section
    atlas_match = re.search(
        r"##\s+ANHANG\s+\w+\s*[—–-]\s*Fehlerbild-Atlas\s*\n(.+?)(?=\n##\s+ANHANG|\n##\s+\d|\Z)",
        content, re.DOTALL | re.IGNORECASE,
    )
    if atlas_match:
        atlas_content = atlas_match.group(1)
        # Match ### F1: Title or ### E.1 Fehlerbild 1: Title
        for match in re.finditer(
            r"###\s+(?:\w+\.?\d*:?\s*)?(?:Fehlerbild\s+\d+:\s*)?(.+?)\n(.+?)(?=###\s|\Z)",
            atlas_content, re.DOTALL,
        ):
            title = match.group(1).strip()
            body = match.group(2).strip()
            if len(body) > 20:  # Skip trivial matches
                _parse_fehlerbild_body(title, body)

    # --- Pattern 3: Schadensbilder sections ---
    for match in re.finditer(
        r"##\s+\d+\.?\s*(?:\w+\s*[—–-]\s*)?Schadensbilder[^\n]*\n(.+?)(?=\n##\s|\Z)",
        content, re.DOTALL | re.IGNORECASE,
    ):
        schadens_content = match.group(1)
        for sub_match in re.finditer(
            r"###\s+[\d.]*\s*(.+?)\n(.+?)(?=###\s|\Z)",
            schadens_content, re.DOTALL,
        ):
            title = sub_match.group(1).strip()
            body = sub_match.group(2).strip()
            if len(body) > 30:
                _parse_fehlerbild_body(title, body)

    return fehlerbilder


def _extract_fallstudien(content: str) -> List[Dict[str, str]]:
    """Extract case studies (Fallstudien).

    Handles multiple formats:
    - New: ### Fallstudie N: Title
    - Old: ### D.1 Fallstudie: Title  (under ANHANG D — Fallstudien)
    - Old: ### C.1 Fallstudie: Title  (under ANHANG C — Fallstudien)
    - Old: ### XX.N Fallstudie: Title  (numbered subsections)
    """
    studies = []
    seen_titles = set()

    def _parse_fallstudie_body(title: str, body: str):
        if title in seen_titles:
            return
        seen_titles.add(title)
        entry = {"title_de": title, "full_text": body}
        for field, patterns in [
            ("situation_de", [
                r"\*\*Situation:\*\*\s*(.+?)(?=\n\*\*|\Z)",
                r"\*\*Boot:\*\*\s*(.+?)(?=\n\*\*|\Z)",
            ]),
            ("diagnose_de", [
                r"\*\*Diagnose:\*\*\s*(.+?)(?=\n\*\*|\Z)",
                r"\*\*Problem:\*\*\s*(.+?)(?=\n\*\*|\Z)",
                r"\*\*Befund:\*\*\s*(.+?)(?=\n\*\*|\Z)",
            ]),
            ("ursache_de", [
                r"\*\*Ursache:\*\*\s*(.+?)(?=\n\*\*|\Z)",
            ]),
            ("ergebnis_de", [
                r"\*\*Ergebnis:\*\*\s*(.+?)(?=\n\*\*|\Z)",
                r"\*\*Lösung:\*\*\s*(.+?)(?=\n\*\*|\Z)",
                r"\*\*Reparatur:\*\*\s*(.+?)(?=\n\*\*|\Z)",
            ]),
            ("massnahme_de", [
                r"\*\*Maßnahme[^:]*:\*\*\s*(.+?)(?=\n\*\*|\Z)",
            ]),
            ("kosten_de", [
                r"\*\*Kosten[^:]*:\*\*\s*(.+?)(?=\n\*\*|\Z)",
                r"\*\*Schaden:\*\*\s*(.+?)(?=\n\*\*|\Z)",
                r"\*\*Kostenpunkt:\*\*\s*(.+?)(?=\n\*\*|\Z)",
            ]),
            ("lehre_de", [
                r"\*\*Lehre:\*\*\s*(.+?)(?=\n\*\*|\Z)",
                r"\*\*Lektion:\*\*\s*(.+?)(?=\n\*\*|\Z)",
            ]),
            ("confidence", [
                r"\*\*Confidence:\*\*\s*(.+?)(?=\n|\Z)",
            ]),
        ]:
            for pat in patterns:
                field_match = re.search(pat, body, re.DOTALL)
                if field_match:
                    entry[field] = field_match.group(1).strip()
                    break
        studies.append(entry)

    # --- Pattern 1: New-style ### Fallstudie N: Title ---
    for match in re.finditer(
        r"###\s+Fallstudie\s+\d+:\s*(.+?)\n(.+?)(?=###\s+Fallstudie\s+\d+|\n---|\n##\s|\Z)",
        content, re.DOTALL,
    ):
        _parse_fallstudie_body(match.group(1).strip(), match.group(2).strip())

    # --- Pattern 2: ANHANG sections with Fallstudien ---
    for anhang_match in re.finditer(
        r"##\s+ANHANG\s+\w+\s*[—–-]\s*Fallstudien[^\n]*\n(.+?)(?=\n##\s+ANHANG|\n##\s+\d|\Z)",
        content, re.DOTALL | re.IGNORECASE,
    ):
        anhang_content = anhang_match.group(1)
        # Match ### D.1 Fallstudie: Title or ### C.1 Fallstudie: Title
        for match in re.finditer(
            r"###\s+\w+\.\d+\s+Fallstudie:\s*(.+?)\n(.+?)(?=###\s+\w+\.\d+|\Z)",
            anhang_content, re.DOTALL,
        ):
            _parse_fallstudie_body(match.group(1).strip(), match.group(2).strip())

    # --- Pattern 3: Inline ### XX.N Fallstudie: Title ---
    for match in re.finditer(
        r"###\s+\d+\.\d+\s+Fallstudie:\s*(.+?)\n(.+?)(?=###\s+\d+\.\d+|\n##\s|\Z)",
        content, re.DOTALL,
    ):
        _parse_fallstudie_body(match.group(1).strip(), match.group(2).strip())

    return studies


def _extract_manufacturers(content: str) -> List[Dict[str, Any]]:
    """Extract manufacturer information from Hersteller sections.

    Handles multiple formats:
    - New: **Firmenprofil:** followed by bullet list
    - Old: ## XX. Hersteller: Name (Land)  as H2 headings
    - Old: ### XX.N Firmenprofil  subsections with bullet list
    - Old: Tables with manufacturer comparison data
    """
    manufacturers = []
    seen_names = set()

    # --- Pattern 1: New-style **Firmenprofil:** bullet list ---
    pattern_new = re.compile(
        r"\*\*Firmenprofil:\*\*\s*\n((?:\s*-\s*.+\n)+)",
        re.MULTILINE,
    )
    for match in pattern_new.finditer(content):
        block = match.group(1)
        profile = _parse_firmenprofil_bullets(block)
        if profile:
            name = profile.get("name", profile.get("origin", ""))
            if name and name not in seen_names:
                seen_names.add(name)
                manufacturers.append(profile)

    # --- Pattern 2: Old-style ## XX. Hersteller: Name (Land) ---
    hersteller_heading = re.compile(
        r"##\s+\d+\.?\s*Hersteller:\s*(.+?)(?:\s*\(([^)]+)\))?\s*$",
        re.MULTILINE,
    )
    for match in hersteller_heading.finditer(content):
        name = match.group(1).strip()
        origin = match.group(2).strip() if match.group(2) else ""
        if name in seen_names:
            continue
        seen_names.add(name)

        # Try to find Firmenprofil subsection nearby
        start_pos = match.end()
        next_h2 = re.search(r"\n##\s+\d", content[start_pos:])
        section_end = start_pos + next_h2.start() if next_h2 else len(content)
        section_content = content[start_pos:section_end]

        # Look for bullet list with profile data
        profile_block = re.search(
            r"(?:###[^\n]*[Ff]irmenprofil[^\n]*\n|###[^\n]*\n)"
            r"((?:\s*[-*]\s*.+\n)+)",
            section_content,
        )
        if profile_block:
            profile = _parse_firmenprofil_bullets(profile_block.group(1))
        else:
            profile = {}

        profile["name"] = name
        if origin:
            profile["origin"] = origin
        manufacturers.append(profile)

    # --- Pattern 3: Sections with "Hersteller & Produkte" ---
    for match in re.finditer(
        r"##\s+\d+\.?\s*(.+?)\s*[—–-]\s*Hersteller\s*&\s*Produkte\s*$",
        content, re.MULTILINE | re.IGNORECASE,
    ):
        section_name = match.group(1).strip()
        start_pos = match.end()
        next_h2 = re.search(r"\n##\s+\d", content[start_pos:])
        section_end = start_pos + next_h2.start() if next_h2 else len(content)
        section_content = content[start_pos:section_end]

        # Find manufacturer names in ### headings
        for sub in re.finditer(
            r"###\s+[\d.]*\s*(?:Hersteller:?\s+)?(.+?)(?:\s*\(([^)]+)\))?\s*$",
            section_content, re.MULTILINE,
        ):
            sub_name = sub.group(1).strip()
            sub_origin = sub.group(2).strip() if sub.group(2) else ""
            # Skip generic headings
            if any(kw in sub_name.lower() for kw in [
                "weitere", "übersicht", "vergleich", "spezifikation",
                "eigenschaft", "anwendung", "produkt"
            ]):
                continue
            if sub_name not in seen_names and len(sub_name) < 80:
                seen_names.add(sub_name)
                profile = {"name": sub_name}
                if sub_origin:
                    profile["origin"] = sub_origin
                manufacturers.append(profile)

    return manufacturers


def _parse_firmenprofil_bullets(block: str) -> Dict[str, str]:
    """Parse a Firmenprofil bullet list into a profile dict."""
    profile = {}
    for line in block.strip().split("\n"):
        line = line.strip().lstrip("-* ")
        if ":" in line:
            key, val = line.split(":", 1)
            key = key.strip().lower().strip("*")
            val = val.strip()
            if not val:
                continue
            if "gegründet" in key or "gründung" in key:
                profile["founded"] = val
            elif "herkunft" in key or "land" in key or "sitz" in key:
                profile["origin"] = val
            elif "spezialisierung" in key:
                profile["specialization"] = val
            elif "website" in key:
                profile["website"] = val
            elif "gewindesystem" in key or "gewinde" in key:
                profile["thread_system"] = val
            elif "material" in key:
                profile["material"] = val
            elif "konzern" in key or "muttergesellschaft" in key:
                profile["parent_company"] = val
            elif "zertifizierung" in key:
                profile["certifications"] = val
            elif "name" in key or "firma" in key:
                profile["name"] = val
    return profile


def _extract_pydantic_models(content: str) -> List[Dict[str, str]]:
    """Extract Pydantic model code blocks for reference."""
    models = []
    pattern = re.compile(
        r"class\s+(\w+)\(BaseModel\):\s*\n"
        r"\s*model_config\s*=\s*\{[^}]+\}\s*\n"
        r"((?:\s+\w+.*\n)*)",
        re.MULTILINE,
    )
    for match in pattern.finditer(content):
        model_name = match.group(1)
        fields_block = match.group(2)
        fields = []
        for line in fields_block.strip().split("\n"):
            line = line.strip()
            if ":" in line and "=" in line:
                field_name = line.split(":")[0].strip()
                fields.append(field_name)
            elif ":" in line:
                field_name = line.split(":")[0].strip()
                fields.append(field_name)
        models.append({
            "class_name": model_name,
            "fields": fields,
        })
    return models


# ---------------------------------------------------------------------------
# Main Parser: Parse a single markdown file
# ---------------------------------------------------------------------------


def parse_knowledge_file(filepath: Path) -> Dict[str, Any]:
    """
    Parse a single markdown knowledge file into a structured dict.

    Returns:
    {
        "file": "06_01_kuehlwasserschlaeuche.md",
        "category": "06",
        "subcategory": "01",
        "slug": "kuehlwasserschlaeuche",
        "title": "Kühlwasserschläuche",
        "sections": {...},           # Full section hierarchy
        "tables": [...],             # All tables as list-of-dicts
        "manufacturers": [...],      # Manufacturer profiles
        "erfahrungsberichte": [...],  # Experience reports
        "expert_references": [...],  # Expert quotes
        "faq": [...],                # FAQ entries
        "glossary": [...],           # Glossary terms
        "fehlerbilder": [...],       # Failure patterns
        "fallstudien": [...],        # Case studies
        "pydantic_models": [...],    # Model definitions
        "line_count": int,
    }
    """
    content = filepath.read_text(encoding="utf-8")
    lines = content.split("\n")

    # Extract identifiers from filename
    name = filepath.stem  # e.g. "06_01_kuehlwasserschlaeuche"
    parts = name.split("_", 2)
    category = parts[0] if len(parts) > 0 else ""
    subcategory = parts[1] if len(parts) > 1 else ""
    slug = parts[2] if len(parts) > 2 else name

    # Extract title from first H1
    title = ""
    title_match = re.match(r"^#\s+(.+)", lines[0] if lines else "")
    if title_match:
        title_raw = title_match.group(1).strip()
        # Remove number prefix like "06.01 — "
        title = re.sub(r"^\d+\.\d+\s*—?\s*", "", title_raw)

    # Parse sections
    sections = _extract_section_hierarchy(content)

    # Collect all tables from all sections
    all_tables = []

    def _collect_tables(section: Dict):
        all_tables.extend(section.get("tables", []))
        for sub in section.get("subsections", []):
            _collect_tables(sub)

    _collect_tables(sections)

    return {
        "file": filepath.name,
        "category": category,
        "subcategory": subcategory,
        "slug": slug,
        "title": title,
        "sections": sections,
        "tables": all_tables,
        "manufacturers": _extract_manufacturers(content),
        "erfahrungsberichte": _extract_erfahrungsberichte(content),
        "expert_references": _extract_expert_references(content),
        "faq": _extract_faq(content),
        "glossary": _extract_glossary(content),
        "fehlerbilder": _extract_fehlerbilder(content),
        "fallstudien": _extract_fallstudien(content),
        "pydantic_models": _extract_pydantic_models(content),
        "line_count": len(lines),
    }


# ---------------------------------------------------------------------------
# Top-Level Loader: Load ALL markdown knowledge files
# ---------------------------------------------------------------------------


def load_all_markdown_knowledge() -> Dict[str, Dict[str, Any]]:
    """
    Load and parse all markdown knowledge files.

    Returns dict keyed by file slug:
    {
        "kuehlwasserschlaeuche": {parsed_data},
        "galvanische_spannungsreihe_thru_hulls": {parsed_data},
        ...
    }
    """
    files = _find_markdown_files()
    knowledge = {}

    for filepath in files:
        try:
            parsed = parse_knowledge_file(filepath)
            knowledge[parsed["slug"]] = parsed
            logger.info(
                f"Loaded markdown knowledge: {filepath.name} "
                f"({parsed['line_count']} lines, "
                f"{len(parsed['tables'])} tables, "
                f"{len(parsed['manufacturers'])} manufacturers, "
                f"{len(parsed['erfahrungsberichte'])} reports, "
                f"{len(parsed['faq'])} FAQ)"
            )
        except Exception as e:
            logger.error(f"Failed to parse {filepath.name}: {e}")

    return knowledge


# ---------------------------------------------------------------------------
# Thematic Databases — Assembled from parsed markdown files
# ---------------------------------------------------------------------------

# Lazy-loaded singleton
_MARKDOWN_KNOWLEDGE: Optional[Dict[str, Dict[str, Any]]] = None


def _ensure_loaded() -> Dict[str, Dict[str, Any]]:
    global _MARKDOWN_KNOWLEDGE
    if _MARKDOWN_KNOWLEDGE is None:
        _MARKDOWN_KNOWLEDGE = load_all_markdown_knowledge()
    return _MARKDOWN_KNOWLEDGE


def get_markdown_knowledge() -> Dict[str, Dict[str, Any]]:
    """Get all parsed markdown knowledge (lazy-loaded)."""
    return _ensure_loaded()


def get_knowledge_by_slug(slug: str) -> Optional[Dict[str, Any]]:
    """Get a single knowledge file by slug."""
    return _ensure_loaded().get(slug)


def get_knowledge_by_category(category: str) -> List[Dict[str, Any]]:
    """Get all knowledge files in a category (e.g. '05' for Halbzeuge)."""
    return [
        v for v in _ensure_loaded().values()
        if v["category"] == category
    ]


# ---------------------------------------------------------------------------
# Aggregated Databases (matching existing module pattern)
# ---------------------------------------------------------------------------


def get_all_manufacturers() -> List[Dict[str, Any]]:
    """Aggregate all manufacturers from all markdown files."""
    manufacturers = []
    for slug, data in _ensure_loaded().items():
        for mfr in data.get("manufacturers", []):
            mfr["knowledge_source"] = slug
            manufacturers.append(mfr)
    return manufacturers


def get_all_erfahrungsberichte() -> List[Dict[str, str]]:
    """Aggregate all experience reports from all markdown files."""
    reports = []
    for slug, data in _ensure_loaded().items():
        for report in data.get("erfahrungsberichte", []):
            report["knowledge_source"] = slug
            reports.append(report)
    return reports


def get_all_fehlerbilder() -> List[Dict[str, str]]:
    """Aggregate all failure patterns from all markdown files."""
    fehlerbilder = []
    for slug, data in _ensure_loaded().items():
        for fb in data.get("fehlerbilder", []):
            fb["knowledge_source"] = slug
            fehlerbilder.append(fb)
    return fehlerbilder


def get_all_fallstudien() -> List[Dict[str, str]]:
    """Aggregate all case studies from all markdown files."""
    studies = []
    for slug, data in _ensure_loaded().items():
        for study in data.get("fallstudien", []):
            study["knowledge_source"] = slug
            studies.append(study)
    return studies


def get_all_faq() -> List[Dict[str, str]]:
    """Aggregate all FAQ entries from all markdown files."""
    faqs = []
    for slug, data in _ensure_loaded().items():
        for faq in data.get("faq", []):
            faq["knowledge_source"] = slug
            faqs.append(faq)
    return faqs


def get_all_glossary() -> List[Dict[str, str]]:
    """Aggregate all glossary entries from all markdown files."""
    glossary = []
    for slug, data in _ensure_loaded().items():
        for entry in data.get("glossary", []):
            entry["knowledge_source"] = slug
            glossary.append(entry)
    return glossary


def get_all_expert_references() -> List[Dict[str, str]]:
    """Aggregate all expert references from all markdown files."""
    refs = []
    for slug, data in _ensure_loaded().items():
        for ref in data.get("expert_references", []):
            ref["knowledge_source"] = slug
            refs.append(ref)
    return refs


# ---------------------------------------------------------------------------
# Search function for markdown knowledge
# ---------------------------------------------------------------------------


def search_markdown_knowledge(
    query: str, max_results: int = 20
) -> List[Dict[str, Any]]:
    """
    Full-text search across all markdown knowledge.
    Searches: titles, FAQ questions/answers, glossary, fehlerbilder,
    erfahrungsberichte, expert references.
    """
    query_lower = query.lower()
    results = []

    for slug, data in _ensure_loaded().items():
        # Search FAQ
        for faq in data.get("faq", []):
            q_text = faq.get("question_de", "")
            a_text = faq.get("answer_de", "")
            if query_lower in q_text.lower() or query_lower in a_text.lower():
                results.append({
                    "type": "faq",
                    "source": slug,
                    "title": data["title"],
                    "question_de": q_text,
                    "answer_de": a_text,
                    "confidence": faq.get("confidence", "documented"),
                })

        # Search glossary
        for entry in data.get("glossary", []):
            for val in entry.values():
                if isinstance(val, str) and query_lower in val.lower():
                    results.append({
                        "type": "glossary",
                        "source": slug,
                        "title": data["title"],
                        **entry,
                    })
                    break

        # Search fehlerbilder
        for fb in data.get("fehlerbilder", []):
            if query_lower in fb.get("title_de", "").lower() or \
               query_lower in fb.get("full_text", "").lower():
                results.append({
                    "type": "fehlerbild",
                    "source": slug,
                    "title": data["title"],
                    "fehlerbild_title": fb["title_de"],
                    "symptom_de": fb.get("symptom_de", ""),
                    "massnahme_de": fb.get("massnahme_de", ""),
                })

        # Search erfahrungsberichte
        for report in data.get("erfahrungsberichte", []):
            if query_lower in report.get("text", "").lower():
                results.append({
                    "type": "erfahrungsbericht",
                    "source": slug,
                    "title": data["title"],
                    "forum": report.get("source", ""),
                    "text": report["text"][:200],
                })

    return results[:max_results]


# ---------------------------------------------------------------------------
# Format for prompt injection (Claude Vision / Analysis context)
# ---------------------------------------------------------------------------


def format_markdown_knowledge_for_prompt(
    slugs: List[str],
    include_sections: Optional[List[str]] = None,
    max_lines: int = 100,
) -> str:
    """
    Format markdown knowledge for injection into analysis prompts.

    Args:
        slugs: List of knowledge slugs to include
        include_sections: Optional filter for section types
            ("faq", "fehlerbilder", "erfahrungsberichte", "glossary")
        max_lines: Maximum output lines

    Returns:
        German-formatted text for prompt context
    """
    parts = []
    knowledge = _ensure_loaded()

    for slug in slugs:
        data = knowledge.get(slug)
        if not data:
            continue

        parts.append(f"=== {data['title']} ===")

        sections_to_include = include_sections or [
            "fehlerbilder", "faq", "erfahrungsberichte"
        ]

        if "fehlerbilder" in sections_to_include:
            for fb in data.get("fehlerbilder", [])[:5]:
                parts.append(f"⚠️ Fehlerbild: {fb['title_de']}")
                if fb.get("symptom_de"):
                    parts.append(f"   Symptom: {fb['symptom_de'][:150]}")
                if fb.get("massnahme_de"):
                    parts.append(f"   Maßnahme: {fb['massnahme_de'][:150]}")

        if "faq" in sections_to_include:
            for faq in data.get("faq", [])[:5]:
                parts.append(f"❓ {faq['question_de']}")
                parts.append(f"   → {faq['answer_de'][:150]}")

        if "erfahrungsberichte" in sections_to_include:
            for report in data.get("erfahrungsberichte", [])[:3]:
                parts.append(
                    f"💬 {report.get('source', 'Forum')}: "
                    f"{report['text'][:150]}"
                )

    # Truncate to max_lines
    output = "\n".join(parts)
    output_lines = output.split("\n")
    if len(output_lines) > max_lines:
        output_lines = output_lines[:max_lines]
        output_lines.append("... (gekürzt)")

    return "\n".join(output_lines)


# ---------------------------------------------------------------------------
# Summary / Statistics
# ---------------------------------------------------------------------------


def get_markdown_knowledge_summary() -> Dict[str, Any]:
    """
    Return summary statistics for all loaded markdown knowledge.
    Used by /api/v1/knowledge/categories endpoint.
    """
    knowledge = _ensure_loaded()

    summary = {
        "total_files": len(knowledge),
        "total_lines": 0,
        "total_tables": 0,
        "total_manufacturers": 0,
        "total_erfahrungsberichte": 0,
        "total_faq": 0,
        "total_glossary": 0,
        "total_fehlerbilder": 0,
        "total_fallstudien": 0,
        "total_expert_references": 0,
        "files": {},
    }

    for slug, data in knowledge.items():
        file_summary = {
            "file": data["file"],
            "title": data["title"],
            "category": data["category"],
            "subcategory": data["subcategory"],
            "line_count": data["line_count"],
            "tables": len(data["tables"]),
            "manufacturers": len(data["manufacturers"]),
            "erfahrungsberichte": len(data["erfahrungsberichte"]),
            "faq": len(data["faq"]),
            "glossary": len(data["glossary"]),
            "fehlerbilder": len(data["fehlerbilder"]),
            "fallstudien": len(data["fallstudien"]),
            "expert_references": len(data["expert_references"]),
        }
        summary["files"][slug] = file_summary
        summary["total_lines"] += data["line_count"]
        summary["total_tables"] += len(data["tables"])
        summary["total_manufacturers"] += len(data["manufacturers"])
        summary["total_erfahrungsberichte"] += len(data["erfahrungsberichte"])
        summary["total_faq"] += len(data["faq"])
        summary["total_glossary"] += len(data["glossary"])
        summary["total_fehlerbilder"] += len(data["fehlerbilder"])
        summary["total_fallstudien"] += len(data["fallstudien"])
        summary["total_expert_references"] += len(data["expert_references"])

    return summary


# ---------------------------------------------------------------------------
# Mapping: slug → relevant retrieval context
# ---------------------------------------------------------------------------

# Maps knowledge slugs to the retrieval functions they should augment
SLUG_TO_RETRIEVAL_CONTEXT = {
    # 04_xx = Composites & Construction Materials
    "honeycomb_core": ["materials", "structural"],
    "soric_lantor": ["materials", "structural"],
    "vakuuminfusions_zubehoer": ["materials", "production"],
    "trennmittel": ["materials", "production"],
    "gfk_reparatur_sets": ["materials", "service_patterns"],
    # 05_xx = Fasteners & Hardware
    "edelstahl_schrauben": ["materials", "structural"],
    "edelstahl_bolzen_muttern": ["materials", "structural"],
    "bronze_schrauben_bolzen": ["materials", "structural"],
    "nieten": ["materials", "structural", "production"],
    "gewindeeinsaetze": ["materials", "structural"],
    "backing_plates": ["materials", "structural"],
    "edelstahl_halbzeuge": ["materials", "structural", "production"],
    "aluminium_halbzeuge": ["materials", "structural", "production"],
    "bronze_armaturen": ["materials", "compliance"],
    "galvanische_spannungsreihe_thru_hulls": [
        "materials", "structural", "compliance"
    ],
    # 01_xx = Dichtungen und Profile
    "fenster_dichtungen": ["materials", "compliance", "service_patterns"],
    "luken_dichtungen": ["materials", "compliance", "service_patterns"],
    "luken_scharnier_dichtungen_und_gasdruckfedern": [
        "materials", "compliance", "service_patterns", "structural"
    ],
    "niedergangs_dichtungen": ["materials", "compliance", "service_patterns"],
    "borddurchlass_dichtungen": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "wellenabdichtung_stopfbuchse_lippendichtung_pss": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "saildrive_manschetten": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "motordichtungen": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "kuehlwassersystem_dichtungen": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "deck_beschlag_abdichtung": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "mast_manschette": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "steuerkoker_ruderschaft_abdichtung": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    # 02_xx = Dichtstoffe und Kleber
    "pu_dichtstoffe_elastisch": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "pu_dichtstoffe_permanent_strukturell": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "teakdeck_fugenmasse": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    # 06_xx = Systems
    "kuehlwasserschlaeuche": ["service_patterns", "materials"],
}


def get_relevant_slugs_for_context(context: str) -> List[str]:
    """
    Given an analysis context (e.g. 'materials', 'structural'),
    return all relevant knowledge slugs.
    """
    return [
        slug for slug, contexts in SLUG_TO_RETRIEVAL_CONTEXT.items()
        if context in contexts
    ]
