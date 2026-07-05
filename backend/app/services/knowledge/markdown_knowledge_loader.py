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
    """Discover all numbered markdown knowledge files in the knowledge dir.

    Excludes files with backup-suffixes like `_clean.md` (intermediate
    bereinigte Kopien einer kanonischen Datei) and `_backup.md`. The
    canonical version always lives at the unsuffixed name.
    """
    BACKUP_SUFFIXES = ("_clean.md", "_backup.md", "_old.md", "_tmp.md")
    files = []
    for f in sorted(KNOWLEDGE_DIR.iterdir()):
        if not f.is_file() or not MARKDOWN_FILES_PATTERN.match(f.name):
            continue
        if any(f.name.endswith(suf) for suf in BACKUP_SUFFIXES):
            logger.debug("Skipping backup file %s", f.name)
            continue
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

    # --- Pattern 3: Inline blockquote expert references ---
    # Format: > **E-XX-NNN**: „quote text" — *Source Name*
    # Also handles "quote text" with regular quotes
    blockquote_pattern = re.compile(
        r'>\s*\*\*([A-Z]-[A-Z]{2,4}-\d{3})\*\*:\s*[\u201e\u201c\u201d""](.+?)[\u201c\u201d""\u201f]\s*\u2014\s*\*(.+?)\*',
        re.DOTALL,
    )
    for match in blockquote_pattern.finditer(content):
        ref_id = match.group(1).strip()
        text = match.group(2).strip().replace("\n> ", " ").replace("\n", " ")
        source = match.group(3).strip()
        refs.append({
            "ref_id": ref_id,
            "source": source,
            "text": text,
        })

    # --- Pattern 4: Blockquote with attribution on next line ---
    # Format: > **"quote"**\n> — Source
    # or: > **„quote"**\n> — Source
    blockquote_pattern2 = re.compile(
        r'>\s*\*\*[\u201e\u201c""](.+?)[\u201c\u201d""]\*\*\s*\n>\s*\u2014\s*(.+?)(?:\n\n|\n(?!>)|\Z)',
        re.DOTALL,
    )
    for match in blockquote_pattern2.finditer(content):
        text = match.group(1).strip().replace("\n> ", " ").replace("\n", " ")
        source = match.group(2).strip()
        refs.append({"source": source, "text": text})

    # --- Pattern 5: Subsection-based expert refs ---
    # Format: ## XX. Experten-Referenzen / Expertenzitate
    #   ### XX.N Name (source)\n- "quote"\n- "quote"
    expert_section_pattern2 = re.compile(
        r"##\s+(?:\d+\.?\s*)?(?:Experten-Referenz(?:en)?|Expertenzitat(?:e)?|"
        r"ANHANG\s+\w+\s*[—–-]\s*Expertenzitat(?:e)?)[^\n]*\n"
        r"(.+?)(?=\n##\s+\d+|\n##\s+ANHANG(?!\s+\w+\s*[—–-]\s*Expertenzitat)|\Z)",
        re.DOTALL | re.IGNORECASE,
    )
    for section_match in expert_section_pattern2.finditer(content):
        section_content = section_match.group(1)
        # Match ### XX.N Name (optional source info)
        for sub_match in re.finditer(
            r"###\s+(?:\d+\.\d+\s+)?(.+?)\n(.+?)(?=\n###\s|\Z)",
            section_content, re.DOTALL,
        ):
            source = sub_match.group(1).strip()
            body = sub_match.group(2).strip()
            # Extract quoted text from bullet points
            quotes = []
            for quote_match in re.finditer(
                r'-\s*["\u201e\u201c](.+?)["\u201d\u201c]',
                body, re.DOTALL,
            ):
                quotes.append(quote_match.group(1).strip())
            # Also bare bullet points starting with „
            for quote_match in re.finditer(
                r'-\s*[\u201e](.+?)[\u201c\u201d]',
                body, re.DOTALL,
            ):
                text = quote_match.group(1).strip()
                if text not in quotes:
                    quotes.append(text)
            if quotes:
                for q in quotes:
                    refs.append({"source": source, "text": q})
            elif len(body) > 20:
                # No quoted text — use full body as reference text
                refs.append({"source": source, "text": body[:500]})

    return refs


def _extract_faq(content: str) -> List[Dict[str, str]]:
    """Extract FAQ entries from markdown.

    Handles multiple formats:
    - New: ### FAQ 1: Question
    - Old: ### F1: Question  (under ## XX. FAQ — Häufige Fragen)
    - Old: ### XX.1 Question  (numbered subsections under FAQ heading)
    - Table: | Nr | Frage | Antwort | (under ## XX. FAQ — ...)
    """
    faqs = []
    seen_questions = set()

    # --- Pattern 1: ### FAQ N: Question or ### FAQ-XX-NNN: Question ---
    pattern_new = re.compile(
        r"###\s+FAQ[\s-][\w-]*\d+:\s*(.+?)\n(.+?)(?=###\s+FAQ[\s-]|\n---|\n##\s|\Z)",
        re.DOTALL,
    )
    for match in pattern_new.finditer(content):
        question = match.group(1).strip()
        answer = match.group(2).strip()
        # Clean answer: remove **Antwort:** prefix if present
        answer = re.sub(r"^\*\*Antwort:\*\*\s*", "", answer)
        conf_match = re.search(r"\(Confidence:\s*(\w+)\)", answer)
        if not conf_match:
            conf_match = re.search(r"<!--\s*Confidence:\s*(\w+)", answer)
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

    # --- Pattern 4: Table-style FAQ under FAQ heading ---
    # Matches: ## XX. FAQ — ... followed by | Nr | Frage | Antwort |
    # Also matches: ## XX. Erweiterte FAQ ...
    faq_table_sections = re.finditer(
        r"##\s+\d+\.?\s*(?:Erweiterte\s+)?FAQ[^\n]*\n"
        r"(.+?)(?=\n##\s+\d+|\n##\s+ANHANG|\Z)",
        content, re.DOTALL | re.IGNORECASE,
    )
    for section_match in faq_table_sections:
        section_content = section_match.group(1)
        lines = section_content.split("\n")
        i = 0
        while i < len(lines):
            line = lines[i]
            if line.strip().startswith("|") and i + 2 < len(lines):
                header_lower = line.lower()
                if "frage" in header_lower or "antwort" in header_lower:
                    table_lines = []
                    while i < len(lines) and lines[i].strip().startswith("|"):
                        table_lines.append(lines[i])
                        i += 1
                    rows = _parse_markdown_table(table_lines)
                    for row in rows:
                        question = ""
                        answer = ""
                        for key, val in row.items():
                            key_lower = key.lower().strip()
                            if "frage" in key_lower:
                                question = val.strip()
                            elif "antwort" in key_lower:
                                answer = val.strip()
                        if question and answer and question not in seen_questions:
                            seen_questions.add(question)
                            faqs.append({
                                "question_de": question,
                                "answer_de": answer,
                                "confidence": "documented",
                            })
                    continue
            i += 1

    # --- Pattern 5: Bold-prefix FAQ under FAQ/Erweiterte FAQ heading ---
    # Format: **F-XX-NNN: Question?**\nAnswer paragraph
    # Also: **F-XX-NNN**: *Question?*\nAnswer paragraph
    # Also: **F-XX-NNN**: Question\n**A**: Answer
    faq_bold_sections = re.finditer(
        r"##\s+\d+\.?\s*(?:Erweiterte\s+)?FAQ[^\n]*\n"
        r"(.+?)(?=\n##\s+\d+|\n##\s+ANHANG|\Z)",
        content, re.DOTALL | re.IGNORECASE,
    )
    for section_match in faq_bold_sections:
        section_content = section_match.group(1)
        # Match **F-XX-NNN: Question** or **F-XX-NNN**: Question\n**A**: Answer
        bold_faq_pattern = re.compile(
            r"\*\*F-[A-Z]{2,4}-\d{3}\*\*:\s*(.+?)\n"
            r"\*\*A\*\*:\s*(.+?)(?=\n\*\*F-[A-Z]{2,4}-\d{3}|\n##|\n---|\Z)",
            re.DOTALL,
        )
        for match in bold_faq_pattern.finditer(section_content):
            question = match.group(1).strip().rstrip("*")
            answer = match.group(2).strip()
            if question and answer and len(answer) > 10 and question not in seen_questions:
                seen_questions.add(question)
                faqs.append({
                    "question_de": question,
                    "answer_de": answer,
                    "confidence": "documented",
                })

        # Also match: **F-XX-NNN: Question?**\nAnswer (no **A** prefix)
        bold_faq_pattern2 = re.compile(
            r"\*\*F-[A-Z]{2,4}-\d{3}:\s*(.+?)\*\*\s*\n"
            r"((?:(?!\*\*F-[A-Z]{2,4}-\d{3}).)+)",
            re.DOTALL,
        )
        for match in bold_faq_pattern2.finditer(section_content):
            question = match.group(1).strip()
            answer = match.group(2).strip()
            if question and answer and len(answer) > 10 and question not in seen_questions:
                seen_questions.add(question)
                faqs.append({
                    "question_de": question,
                    "answer_de": answer,
                    "confidence": "documented",
                })

        # Also match: **F-XX-NNN**: *Question?*\nAnswer (italic question, no **A**)
        bold_faq_pattern3 = re.compile(
            r"\*\*F-[A-Z]{2,4}-\d{3}\*\*:\s*\*(.+?)\*\s*\n"
            r"((?:(?!\*\*F-[A-Z]{2,4}-\d{3}).)+)",
            re.DOTALL,
        )
        for match in bold_faq_pattern3.finditer(section_content):
            question = match.group(1).strip()
            answer = match.group(2).strip()
            if question and answer and len(answer) > 10 and question not in seen_questions:
                seen_questions.add(question)
                faqs.append({
                    "question_de": question,
                    "answer_de": answer,
                    "confidence": "documented",
                })

    # --- Pattern 6: ### F: Question format under FAQ heading ---
    # Format: ### F: Question?\n**A**: Answer
    faq_f_sections = re.finditer(
        r"##\s+\d+\.?\s*FAQ[^\n]*\n(.+?)(?=\n##\s+\d+|\n##\s+ANHANG|\Z)",
        content, re.DOTALL | re.IGNORECASE,
    )
    for section_match in faq_f_sections:
        section_content = section_match.group(1)
        for match in re.finditer(
            r"###\s+F:\s*(.+?)\n\*\*A\*\*:\s*(.+?)(?=\n###\s|\n##\s|\Z)",
            section_content, re.DOTALL,
        ):
            question = match.group(1).strip()
            answer = match.group(2).strip()
            if question and answer and len(answer) > 10 and question not in seen_questions:
                seen_questions.add(question)
                faqs.append({
                    "question_de": question,
                    "answer_de": answer,
                    "confidence": "documented",
                })

    # --- Pattern 7: **F: Question**\nA: Answer (bare A:, no bold) ---
    # Used in categories 01-03 under ## XX. FAQ or ### XX.N Häufig gestellte Fragen
    faq_bare_sections = re.finditer(
        r"##\s+\d+\.?\s*(?:FAQ|Häufig)[^\n]*\n(.+?)(?=\n##\s+\d+|\n##\s+ANHANG|\Z)",
        content, re.DOTALL | re.IGNORECASE,
    )
    for section_match in faq_bare_sections:
        section_content = section_match.group(1)
        # Match **F: Question?**\nA: Answer\n(Confidence: ...)
        for match in re.finditer(
            r"\*\*F:\s*(.+?)\*\*\s*\n"
            r"A:\s*(.+?)(?=\n\*\*F:|\n\(Confidence:|\n##|\n---|\Z)",
            section_content, re.DOTALL,
        ):
            question = match.group(1).strip()
            answer = match.group(2).strip()
            # Extract confidence if present after the answer
            conf_match = re.search(r"\(Confidence:\s*(\w+)", section_content[match.end():match.end()+100])
            confidence = conf_match.group(1) if conf_match else "documented"
            if question and answer and len(answer) > 10 and question not in seen_questions:
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
        r"##\s+\d+\.?\s*Glossar[^\n]*\n(.+?)(?=\n##\s|\Z)",
        # Old: ## ANHANG X — Glossar
        r"##\s+ANHANG\s+\w+\s*[—–-]\s*Glossar\s*\n(.+?)(?=\n##\s|\Z)",
        # Extended: ## XX. Erweiterte Glossar-Ergänzungen
        r"##\s+\d+\.?\s*Erweiterte\s+Glossar[^\n]*\n(.+?)(?=\n##\s|\Z)",
        # Anhang subsections: ## XX. Anhang — Glossar
        r"##\s+\d+\.?\s*Anhang[^\n]*Glossar[^\n]*\n(.+?)(?=\n##\s|\Z)",
    ]

    # Collect all glossar sections (there may be multiple)
    all_glossar_content = []
    for pat in glossar_patterns:
        for match in re.finditer(pat, content, re.DOTALL | re.IGNORECASE):
            all_glossar_content.append(match.group(1))

    if not all_glossar_content:
        return glossary

    seen_terms = set()
    for glossar_content in all_glossar_content:
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
                            elif "marine" in key_lower or "kontext" in key_lower:
                                # Marine-Kontext column → use as definition supplement
                                existing_def = entry.get("definition", "")
                                if existing_def:
                                    entry["definition"] = f"{existing_def} — {val_clean}"
                                else:
                                    entry["definition"] = val_clean
                            elif "term_de" not in entry and "de" not in key_lower:
                                # First unrecognized column with bold text is likely term
                                if val.strip().startswith("**"):
                                    entry["term_de"] = val_clean
                        if entry.get("term_de"):
                            term_key = entry["term_de"].lower()
                            if term_key not in seen_terms:
                                seen_terms.add(term_key)
                                glossary.append(entry)
                continue
            # --- Inline bold term format: **Term**: Def or **Term:** Def ---
            elif lines[i].strip().startswith("**") and ("**:" in lines[i] or ":**" in lines[i]):
                bold_match = re.match(
                    r"\s*\*\*(.+?)(?::\*\*|\*\*:)\s*(.+)",
                    lines[i],
                )
                if bold_match:
                    term = bold_match.group(1).strip()
                    definition = bold_match.group(2).strip()
                    # Collect continuation lines
                    j = i + 1
                    while j < len(lines) and lines[j].strip() and \
                          not lines[j].strip().startswith("**") and \
                          not lines[j].strip().startswith("|") and \
                          not lines[j].strip().startswith("#"):
                        definition += " " + lines[j].strip()
                        j += 1
                    term_key = term.lower()
                    if term_key not in seen_terms and len(definition) > 5:
                        seen_terms.add(term_key)
                        glossary.append({
                            "term_de": term,
                            "definition": definition,
                        })
                    i = j
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

    # --- Pattern 3: Schadensbilder sections (heading-based sub-entries) ---
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

    # --- Pattern 4: Table-format Schadensbilder / Fehlerbilder ---
    # Format A: | Nr | Schadensbild | Optik | Klopftest | US-Ergebnis | Ursache wahrscheinlich | Maßnahme |
    # Format B: | Nr | Fehlerbild | Ursache | Erkennung | Kritikalität | Reparatur | Kosten |
    # Format C: | Defekt-ID | Fehlerbild | Ursache | ... (under Fehlerkatalog sections)
    table_section_pattern = re.compile(
        r"##\s+\d+\.?\s*[^\n]*(?:Schadensbilder|Fehlerbilder|Fehlerkatalog|Fehler[^\n]*Ausfallmuster)[^\n]*\n"
        r"(.+?)(?=\n##\s+\d+|\Z)",
        re.DOTALL | re.IGNORECASE,
    )
    for section_match in table_section_pattern.finditer(content):
        section_content = section_match.group(1)
        # Find tables inside this section (may be under ### sub-headings)
        lines = section_content.split("\n")
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            # Detect header row containing relevant columns
            if line.startswith("|") and ("Schadensbild" in line or "Fehlerbild" in line):
                header_cells = [c.strip().strip("*") for c in line.split("|")]
                header_cells = [c for c in header_cells if c]
                # Skip separator row
                if i + 1 < len(lines) and re.match(r"^\s*\|[\s\-|]+\|?\s*$", lines[i + 1]):
                    i += 2
                else:
                    i += 1
                # Parse data rows
                while i < len(lines) and lines[i].strip().startswith("|"):
                    row_line = lines[i].strip()
                    cells = [c.strip().strip("*") for c in row_line.split("|")]
                    cells = [c for c in cells if c]
                    if len(cells) >= 3:
                        row = {}
                        for idx, hdr in enumerate(header_cells):
                            if idx < len(cells):
                                row[hdr] = cells[idx]
                        # Build fehlerbild entry from table row
                        title = row.get("Schadensbild", row.get("Fehlerbild", row.get("Schadensbild/Fehlerbild", "")))
                        if title and title not in seen_titles:
                            seen_titles.add(title)
                            entry = {"title_de": title}
                            nr = row.get("Nr", row.get("Defekt-ID", ""))
                            if nr:
                                entry["nr"] = nr
                            # Format A columns
                            if "Optik" in row:
                                entry["symptom_de"] = row["Optik"]
                            if "Ursache wahrscheinlich" in row:
                                entry["ursache_de"] = row["Ursache wahrscheinlich"]
                            elif "Ursache" in row:
                                entry["ursache_de"] = row["Ursache"]
                            if "Maßnahme" in row:
                                entry["massnahme_de"] = row["Maßnahme"]
                            if "Klopftest" in row:
                                entry["klopftest"] = row["Klopftest"]
                            if "US-Ergebnis" in row:
                                entry["us_ergebnis"] = row["US-Ergebnis"]
                            # Format B columns
                            if "Erkennung" in row:
                                entry["symptom_de"] = row.get("symptom_de", "") or row["Erkennung"]
                            if "Kritikalität" in row:
                                entry["haeufigkeit_de"] = row["Kritikalität"]
                            if "Reparatur" in row:
                                entry["massnahme_de"] = entry.get("massnahme_de", "") or row["Reparatur"]
                            if "Kosten" in row:
                                entry["kosten"] = row["Kosten"]
                            # Additional columns from various formats
                            if "Konsequenz" in row:
                                entry["konsequenz"] = row["Konsequenz"]
                            if "Prävention" in row:
                                entry["praevention"] = row["Prävention"]
                            rk = row.get("Reparatur-Kosten (12m SY)", "")
                            if rk:
                                entry["kosten"] = rk
                            hf = row.get("Häufigkeit", "")
                            if hf and "haeufigkeit_de" not in entry:
                                entry["haeufigkeit_de"] = hf
                            fehlerbilder.append(entry)
                    i += 1
                continue
            i += 1

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

    # --- Pattern 4: English "Case Study" format ---
    # ### Case Study N: Title  or  ### XX.N Case Study N: Title
    for match in re.finditer(
        r"###\s+(?:\d+\.\d+\s+)?Case\s+Study\s+\d+:\s*(.+?)\n(.+?)(?=###\s+(?:\d+\.\d+\s+)?Case\s+Study|\n##\s|\Z)",
        content, re.DOTALL | re.IGNORECASE,
    ):
        _parse_fallstudie_body(match.group(1).strip(), match.group(2).strip())

    # --- Pattern 5: ## XX. Case Studies / Erweiterte Case Studies section ---
    # with ### subsections
    for section_match in re.finditer(
        r"##\s+\d+\.?\s*(?:Erweiterte\s+)?Case\s+Stud(?:ies|y)[^\n]*\n"
        r"(.+?)(?=\n##\s+\d+|\Z)",
        content, re.DOTALL | re.IGNORECASE,
    ):
        section_content = section_match.group(1)
        for sub_match in re.finditer(
            r"###\s+(?:\d+\.\d+\s+)?(?:Case\s+Study\s+\d+:\s*)?(.+?)\n(.+?)(?=###\s|\Z)",
            section_content, re.DOTALL,
        ):
            title = sub_match.group(1).strip()
            body = sub_match.group(2).strip()
            if len(body) > 30 and "Case Study" not in title[:15]:
                _parse_fallstudie_body(title, body)

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
            key = parsed["slug"]
            if key in knowledge:
                # Slug collision across categories (e.g. 13_02 vs 17_02
                # 'ankerketten', 14_03 vs 20_02 'hydraulische_steuerung').
                # Previously the later file silently overwrote the earlier one,
                # dropping 6 knowledge files entirely. Keep the first under the
                # bare slug (so existing slug lookups still resolve) and store the
                # collider under its unique file stem so nothing is lost and both
                # remain reachable via category filters / value iteration.
                existing = knowledge[key]
                key = f"{parsed['category']}_{parsed['subcategory']}_{parsed['slug']}"
                logger.warning(
                    "Slug collision '%s': already loaded from category %s_%s; "
                    "storing %s under unique key '%s' (no data lost).",
                    parsed["slug"], existing["category"], existing["subcategory"],
                    filepath.name, key,
                )
            knowledge[key] = parsed
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
    "silikon_dichtstoffe": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "polysulfid_dichtstoffe": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "butylband": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "epoxid_kleber": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "acrylat_kleber": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "sekundenkleber_marine": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "kontaktkleber": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "primer_fuer_dichtstoffe": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "reiniger_und_entfetter": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "anti_seize_pasten": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    # 03_xx = Beschichtungen & Farben
    "antifouling_selbstpolierend": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "antifouling_hart": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "antifouling_kupferfrei": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "antifouling_foul_release_silikon": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "antifouling_coppercoat_permanentsysteme": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "unterwasser_primer": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "epoxid_barrier_coat_osmoseschutz": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "topside_lack_2k_polyurethan": [
        "materials", "production", "compliance", "service_patterns"
    ],
    "topside_lack_1k": [
        "materials", "production", "compliance", "service_patterns"
    ],
    "klarlack_fuer_holz": [
        "materials", "production", "compliance", "service_patterns"
    ],
    "teak_oel_und_pflege": [
        "materials", "production", "compliance", "service_patterns"
    ],
    "gelcoat_reparaturmaterial": [
        "materials", "production", "compliance", "service_patterns"
    ],
    "fairing_compounds_spachtel": [
        "materials", "production", "compliance", "service_patterns"
    ],
    "edelstahl_pflegemittel_und_passivierung": [
        "materials", "production", "compliance", "service_patterns"
    ],
    "aluminium_beschichtungssysteme": [
        "materials", "production", "compliance", "service_patterns"
    ],
    "bilgenfarbe": [
        "materials", "production", "service_patterns"
    ],
    # 04_xx = Harze/Fasern/Verbundwerkstoffe
    "polyester_harz": [
        "materials", "structural", "production"
    ],
    "vinylester_harz": [
        "materials", "structural", "production", "service_patterns"
    ],
    "epoxid_harz": [
        "materials", "structural", "production", "service_patterns"
    ],
    "fuellstoffe_fuer_harze": [
        "materials", "structural", "production", "service_patterns"
    ],
    "e_glas_gewebe_und_gelege": [
        "materials", "structural", "production", "service_patterns"
    ],
    "s_glas": [
        "materials", "structural", "production", "service_patterns"
    ],
    "carbongewebe": [
        "materials", "structural", "production", "service_patterns"
    ],
    "aramidgewebe": [
        "materials", "structural", "production", "service_patterns"
    ],
    "hybridgewebe": [
        "materials", "structural", "production", "service_patterns"
    ],
    "kernmaterial_endkorn_balsa": [
        "materials", "structural", "production", "service_patterns"
    ],
    "kernmaterial_pvc_schaum": [
        "materials", "structural", "production", "service_patterns"
    ],
    "kernmaterial_san_schaum": [
        "materials", "structural", "production", "service_patterns"
    ],
    # 06_xx = Systeme (Schläuche und Leitungen)
    "kuehlwasserschlaeuche": ["service_patterns", "materials", "compliance"],
    "auspuffschlaeuche": [
        "service_patterns", "materials", "compliance", "structural"
    ],
    "sanitaerschlaeuche": [
        "service_patterns", "materials", "compliance"
    ],
    "kraftstoffschlaeuche": [
        "service_patterns", "materials", "compliance", "structural"
    ],
    "trinkwasserschlaeuche": [
        "service_patterns", "materials", "compliance"
    ],
    "gasschlaeuche": [
        "service_patterns", "materials", "compliance", "structural"
    ],
    "hydraulikschlaeuche": [
        "service_patterns", "materials", "structural"
    ],
    "bilgenschlaeuche": [
        "service_patterns", "materials", "compliance"
    ],
    "deckwaschschlaeuche": [
        "service_patterns", "materials"
    ],
    # 07_xx = Seeventile und Borddurchlässe
    "seeventile": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "borddurchlaesse": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "seeventilhaehne": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "seewasserfilter": [
        "materials", "compliance", "service_patterns"
    ],
    "schlauchverbindungen": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "opferanoden": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    # 08_xx = Luken, Fenster und Bullaugen
    "decksluken": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "bullaugen": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "windschutzscheiben": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "lukenbeschlaege": [
        "materials", "structural", "service_patterns"
    ],
    "luken_fensterdichtungen": [
        "materials", "compliance", "service_patterns"
    ],
    # 09_xx = Winschen
    "winschen_grundlagen": [
        "materials", "structural", "service_patterns"
    ],
    "harken_winschen": [
        "materials", "structural", "service_patterns"
    ],
    "lewmar_winschen": [
        "materials", "structural", "service_patterns"
    ],
    "andersen_winschen": [
        "materials", "structural", "service_patterns"
    ],
    "antal_winschen": [
        "materials", "structural", "service_patterns"
    ],
    "elektrische_winschen": [
        "materials", "structural", "service_patterns", "compliance"
    ],
    "winschen_wartung": [
        "service_patterns", "materials"
    ],
    # 10_xx = Blöcke und Umlenkrollen
    "bloecke_grundlagen": [
        "materials", "structural", "service_patterns"
    ],
    "harken_bloecke": [
        "materials", "structural", "service_patterns"
    ],
    "lewmar_ronstan_bloecke": [
        "materials", "structural", "service_patterns"
    ],
    "hochlast_bloecke": [
        "materials", "structural", "service_patterns", "compliance"
    ],
    "bloecke_wartung": [
        "service_patterns", "materials"
    ],
    # 11_xx = Klampen, Klemmen und Schienensysteme
    "klampen_grundlagen": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "cam_cleats_klemmen": [
        "materials", "structural", "service_patterns"
    ],
    "schienensysteme": [
        "materials", "structural", "service_patterns"
    ],
    "relingstuetzen": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "augenplatten_decksbeschlaege": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    # 12_xx = Schäkel, Wirbel und Verbinder
    "schaekel_grundlagen": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "wirbel_drehgelenke": [
        "materials", "structural", "service_patterns"
    ],
    "bolzen_splinte": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "schnappschaekel": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "verbinder_wartung": [
        "service_patterns", "materials"
    ],
    # 13_xx = Ankersysteme und Festmacher
    "anker_grundlagen": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "ankerketten": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "ankerwinden": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "ankergeschirr": [
        "materials", "structural", "service_patterns"
    ],
    "festmacher_fender": [
        "materials", "service_patterns"
    ],
    "ankerbucht_bugbeschlaege": [
        "materials", "structural", "service_patterns"
    ],
    "mooring_systeme": [
        "materials", "compliance", "service_patterns"
    ],
    "ankersysteme_wartung": [
        "service_patterns", "materials"
    ],
    # 14_xx = Steueranlagen und Autopilot
    "steueranlagen_grundlagen": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "mechanische_steuerung": [
        "materials", "structural", "service_patterns"
    ],
    "hydraulische_steuerung": [
        "materials", "structural", "service_patterns"
    ],
    "ruderanlage_lager": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "autopilot_systeme": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "notruder_notsteuerung": [
        "structural", "compliance", "service_patterns"
    ],
    "steuerraeder_pinnen": [
        "materials", "structural", "service_patterns"
    ],
    "steueranlagen_wartung": [
        "service_patterns", "materials"
    ],
    # 15_xx = Rollreffanlagen und Furler
    "rollreffanlagen_grundlagen": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "grosssegel_rollreff": [
        "materials", "structural", "service_patterns"
    ],
    "furler_hersteller": [
        "materials", "structural", "service_patterns"
    ],
    "rollreffanlagen_wartung": [
        "service_patterns", "materials"
    ],
    # 16_xx = Segel
    "segel_grundlagen": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "grosssegel": [
        "materials", "structural", "service_patterns"
    ],
    "vorsegel": [
        "materials", "structural", "service_patterns"
    ],
    "spinnaker_gennaker": [
        "materials", "structural", "service_patterns"
    ],
    "segeltuch_materialien": [
        "materials", "structural"
    ],
    "segelmacher_hersteller": [
        "materials", "service_patterns"
    ],
    "segelschnitt_trimm": [
        "materials", "structural", "service_patterns"
    ],
    "segel_wartung": [
        "service_patterns", "materials"
    ],
    # 17_xx = Anker und Kette
    "ankertypen_grundlagen": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "ankerketten": [
        "materials", "structural", "service_patterns"
    ],
    "ankerwinden": [
        "materials", "structural", "service_patterns"
    ],
    "ankergeschirr": [
        "materials", "structural", "service_patterns"
    ],
    "snubber_kettenstopper": [
        "materials", "structural", "service_patterns"
    ],
    "ankertechniken": [
        "compliance", "service_patterns"
    ],
    "ankerbucht_design": [
        "structural", "materials", "compliance"
    ],
    "anker_wartung": [
        "service_patterns", "materials"
    ],
    # 18_xx = Motoren und Antrieb
    "marine_diesel_grundlagen": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "yanmar_motoren": [
        "materials", "structural", "service_patterns"
    ],
    "volvo_penta": [
        "materials", "structural", "service_patterns"
    ],
    "beta_nanni_vetus": [
        "materials", "structural", "service_patterns"
    ],
    "kuehlsystem": [
        "materials", "structural", "service_patterns"
    ],
    "abgasanlage": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "getriebe_saildrive": [
        "materials", "structural", "service_patterns"
    ],
    "wellenanlage": [
        "materials", "structural", "service_patterns"
    ],
    "propeller": [
        "materials", "structural", "service_patterns"
    ],
    "motorlager_einbau": [
        "structural", "materials", "service_patterns"
    ],
    "elektroantrieb": [
        "materials", "structural", "service_patterns"
    ],
    "bugstrahlruder": [
        "materials", "structural", "service_patterns"
    ],
    "motor_wartung": [
        "service_patterns", "materials"
    ],
    "motor_troubleshooting": [
        "service_patterns", "materials", "structural"
    ],
    # 19_xx = Kraftstoffsystem
    "kraftstofftanks_grundlagen": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "kraftstofffilter_abscheider": [
        "materials", "service_patterns"
    ],
    "kraftstoffleitungen_armaturen": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "kraftstoffsystem_wartung": [
        "service_patterns", "materials"
    ],
    # 20_xx = Steuerung
    "steuerung_grundlagen": [
        "structural", "materials", "compliance", "service_patterns"
    ],
    "hydraulische_steuerung": [
        "structural", "materials", "service_patterns"
    ],
    "ruderanlage_lager": [
        "structural", "materials", "service_patterns"
    ],
    "steuerraeder_pinnen": [
        "materials", "service_patterns"
    ],
    "notsteuerung": [
        "compliance", "structural", "service_patterns"
    ],
    "steuerung_wartung": [
        "service_patterns", "materials", "structural"
    ],
    # 21_xx = Autopilot
    "autopilot_grundlagen": [
        "structural", "materials", "compliance", "service_patterns"
    ],
    "autopilot_hersteller": [
        "materials", "service_patterns"
    ],
    "windfahnen_selbststeueranlage": [
        "structural", "materials", "service_patterns"
    ],
    "autopilot_installation": [
        "structural", "compliance", "service_patterns"
    ],
    "autopilot_wartung": [
        "service_patterns", "materials"
    ],
    # 22_xx = Elektrik
    "elektrik_grundlagen": [
        "structural", "materials", "compliance", "service_patterns"
    ],
    "batterien": [
        "materials", "structural", "service_patterns"
    ],
    "kabel_leitungen": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "ladegeraete_laderegler": [
        "materials", "service_patterns"
    ],
    "solaranlage": [
        "materials", "structural", "service_patterns"
    ],
    "windgenerator": [
        "materials", "structural", "service_patterns"
    ],
    "wechselrichter_landstrom": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "schalttafeln_sicherungen": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "beleuchtung": [
        "materials", "compliance", "service_patterns"
    ],
    "galvanische_korrosion": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "generatoren": [
        "materials", "structural", "service_patterns"
    ],
    "elektrik_wartung": [
        "service_patterns", "materials", "structural"
    ],
    # 23_xx = Elektronik/Navigation
    "navigation_grundlagen": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "kartenplotter": [
        "materials", "service_patterns"
    ],
    "radar_ais": [
        "materials", "compliance", "service_patterns"
    ],
    "ukw_funk": [
        "compliance", "service_patterns"
    ],
    "instrumente_sensoren": [
        "materials", "structural", "service_patterns"
    ],
    "nmea_vernetzung": [
        "materials", "structural", "service_patterns"
    ],
    "antennen_installation": [
        "materials", "structural", "service_patterns"
    ],
    "elektronik_wartung": [
        "service_patterns", "materials"
    ],
    # 24_xx = Sanitär
    "bordtoiletten": [
        "materials", "compliance", "service_patterns"
    ],
    "faekalientanks": [
        "materials", "compliance", "service_patterns"
    ],
    "frischwassersystem": [
        "materials", "structural", "service_patterns"
    ],
    "warmwasserbereiter": [
        "materials", "structural", "service_patterns"
    ],
    "pumpen_sanitaer": [
        "materials", "structural", "service_patterns"
    ],
    "rohrleitungen_armaturen_sanitaer": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "sanitaer_wartung": [
        "service_patterns", "materials"
    ],
    # 25_xx = Gas und Kochen
    "gasanlage_grundlagen": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "kocher_backofen": [
        "materials", "compliance", "service_patterns"
    ],
    "gasflaschenlagerung": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "gas_sicherheit_wartung": [
        "compliance", "service_patterns", "materials"
    ],
    # 26_xx = Heizung/Klima
    "heizung_grundlagen": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "diesel_heizung": [
        "materials", "structural", "service_patterns"
    ],
    "klimaanlage": [
        "materials", "structural", "service_patterns"
    ],
    "isolation_lueftung": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "waermepumpe": [
        "materials", "structural", "service_patterns"
    ],
    "heizung_klima_wartung": [
        "service_patterns", "materials"
    ],
    # 27_xx = Persenning
    "persenning_grundlagen": [
        "materials", "production", "service_patterns"
    ],
    "bimini_sprayhood": [
        "materials", "structural", "production", "service_patterns"
    ],
    "cockpitverdecke": [
        "materials", "production", "service_patterns"
    ],
    "winterplanen": [
        "materials", "service_patterns"
    ],
    "sonnensegel_polster": [
        "materials", "production", "service_patterns"
    ],
    "persenning_wartung": [
        "service_patterns", "materials"
    ],
    # 28_xx = Interieur-Materialien
    "interieur_holz": [
        "materials", "production", "service_patterns"
    ],
    "polstermaterialien": [
        "materials", "production", "service_patterns"
    ],
    "bodenbelaege": [
        "materials", "production", "service_patterns"
    ],
    "oberflaechen_lacke": [
        "materials", "production", "service_patterns"
    ],
    "beschlaege_interieur": [
        "materials", "structural", "service_patterns"
    ],
    "countertops_arbeitsflaechen": [
        "materials", "production", "service_patterns"
    ],
    "interieur_wartung": [
        "service_patterns", "materials"
    ],
    # 29_xx = Sicherheitsausrüstung
    "rettungswesten": [
        "compliance", "service_patterns", "materials"
    ],
    "rettungsinseln": [
        "compliance", "service_patterns", "materials"
    ],
    "sicherheitsleinen": [
        "compliance", "structural", "service_patterns", "materials"
    ],
    "signalmittel": [
        "compliance", "service_patterns"
    ],
    "feuerloesch": [
        "compliance", "service_patterns", "materials"
    ],
    "erste_hilfe": [
        "compliance", "service_patterns"
    ],
    "mann_ueber_bord": [
        "compliance", "service_patterns", "materials"
    ],
    "lenzpumpen_notausruestung": [
        "compliance", "structural", "service_patterns", "materials"
    ],
    "sicherheit_wartung": [
        "compliance", "service_patterns"
    ],
    # 30_xx = Trailer/Transport
    "bootstrailer": [
        "materials", "structural", "compliance", "service_patterns"
    ],
    "kranarbeiten_slippen": [
        "structural", "compliance", "service_patterns"
    ],
    "transport_lagerung": [
        "service_patterns", "materials"
    ],
    # 31_xx = Design/Konstruktion
    "rumpfformen": [
        "structural", "materials"
    ],
    "hydrostatik": [
        "structural", "compliance"
    ],
    "strukturberechnung": [
        "structural", "materials", "compliance"
    ],
    "rigg_dimensionierung": [
        "structural", "materials"
    ],
    "gewichtsmanagement": [
        "structural"
    ],
    "propellerauslegung": [
        "structural", "materials"
    ],
    "tankplanung": [
        "structural", "compliance", "materials"
    ],
    "kielkonstruktion": [
        "structural", "materials", "compliance"
    ],
    "ruder_design": [
        "structural", "materials"
    ],
    "deck_layout": [
        "structural", "compliance"
    ],
    "interieur_layout": [
        "structural", "production"
    ],
    "laminatplan": [
        "structural", "materials", "production"
    ],
    "cad_tools": [
        "production"
    ],
    "design_konstruktion_wartung": [
        "service_patterns"
    ],
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
