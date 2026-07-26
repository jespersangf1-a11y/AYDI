import { useEffect, useRef, type ReactNode } from 'react'
import { X, BookOpen, FileText } from 'lucide-react'
import type { CorpusSection, CorpusTable, KnowledgeDocument } from '../../types'

interface KnowledgeArticleProps {
  doc: KnowledgeDocument
  onClose: () => void
}

/**
 * Modal article view for one research document — renders the parsed
 * section hierarchy (headings, body text, tables). All content is rendered
 * as React nodes (escaped), never as HTML; links are restricted to http(s).
 */
export default function KnowledgeArticle({ doc, onClose }: KnowledgeArticleProps) {
  const sections = rootContent(doc.sections)
  const closeRef = useRef<HTMLButtonElement>(null)
  const panelRef = useRef<HTMLDivElement>(null)

  // A11y: focus the dialog, close on Escape, trap Tab, lock body scroll,
  // restore focus to the triggering element on unmount.
  useEffect(() => {
    const previouslyFocused = window.document.activeElement as HTMLElement | null
    closeRef.current?.focus()

    const onKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        onClose()
        return
      }
      if (e.key === 'Tab' && panelRef.current) {
        const focusables = panelRef.current.querySelectorAll<HTMLElement>(
          'button, a[href], summary, [tabindex]:not([tabindex="-1"])',
        )
        if (focusables.length === 0) return
        const first = focusables[0]
        const last = focusables[focusables.length - 1]
        if (e.shiftKey && window.document.activeElement === first) {
          e.preventDefault()
          last.focus()
        } else if (!e.shiftKey && window.document.activeElement === last) {
          e.preventDefault()
          first.focus()
        }
      }
    }

    window.document.addEventListener('keydown', onKeyDown)
    const prevOverflow = window.document.body.style.overflow
    window.document.body.style.overflow = 'hidden'
    return () => {
      window.document.removeEventListener('keydown', onKeyDown)
      window.document.body.style.overflow = prevOverflow
      previouslyFocused?.focus?.()
    }
  }, [onClose])

  return (
    <div
      className="fixed inset-0 z-50 bg-navy-950/70 backdrop-blur-sm overflow-y-auto overscroll-contain"
      role="dialog"
      aria-modal="true"
      aria-label={doc.title}
      onMouseDown={(e) => {
        // Close only when press AND release happen on the backdrop itself —
        // a text selection ending over the backdrop must not close the modal.
        if (e.target === e.currentTarget) onClose()
      }}
    >
      <div
        ref={panelRef}
        className="max-w-4xl mx-auto my-6 sm:my-10 bg-white rounded-xl shadow-2xl overflow-hidden"
      >
        {/* Header */}
        <div className="sticky top-0 z-10 bg-white/95 backdrop-blur border-b border-sand-200 px-6 sm:px-10 py-5">
          <div className="flex items-start justify-between gap-4">
            <div className="min-w-0">
              <p className="text-xs font-medium text-ocean-600 uppercase tracking-wide mb-1">
                {doc.category} — {doc.category_name}
              </p>
              <h2 className="font-serif text-xl sm:text-2xl font-medium text-navy-900 leading-snug">
                {doc.title}
              </h2>
              <p className="mt-2 flex items-center gap-3 text-xs text-navy-600 font-mono">
                <span className="flex items-center gap-1">
                  <FileText className="w-3.5 h-3.5" />
                  {doc.file}
                </span>
                <span>{doc.line_count.toLocaleString('de-DE')} Zeilen</span>
              </p>
            </div>
            <button
              ref={closeRef}
              onClick={onClose}
              aria-label="Artikel schließen"
              className="flex-shrink-0 p-2 rounded-lg text-navy-600 hover:text-navy-900 hover:bg-sand-100 focus:outline-none focus:ring-2 focus:ring-ocean-500 transition-colors"
            >
              <X className="w-5 h-5" />
            </button>
          </div>
        </div>

        {/* Body */}
        <div className="px-6 sm:px-10 py-8">
          {sections.length === 0 ? (
            <div className="text-center py-12 text-navy-600">
              <BookOpen className="w-10 h-10 mx-auto mb-3" />
              <p className="text-sm">Dieser Artikel enthält keine darstellbaren Abschnitte.</p>
            </div>
          ) : (
            sections.map((section, idx) => <SectionView key={idx} section={section} />)
          )}
        </div>
      </div>
    </div>
  )
}

/**
 * The loader wraps the document in a level-0 root; the first child is the
 * title H1. Unwrap that layer (title is already in the modal header), keep
 * its intro text, and append any further H1 siblings (e.g. appendices).
 */
function rootContent(root: CorpusSection): CorpusSection[] {
  const subs = root.subsections ?? []
  if (subs.length > 0 && subs[0].level === 1) {
    const h1 = subs[0]
    const intro: CorpusSection[] =
      h1.text || h1.tables.length > 0
        ? [{ title: '', level: 2, text: h1.text, tables: h1.tables, subsections: [] }]
        : []
    return [...intro, ...h1.subsections, ...subs.slice(1)]
  }
  return subs
}

function SectionView({ section }: { section: CorpusSection }) {
  const hasContent =
    section.text || section.tables.length > 0 || section.subsections.length > 0
  if (!hasContent && !section.title) return null

  const body = (
    <>
      {section.text && <TextBlocks text={section.text} />}
      {section.tables.map((table, i) => (
        <TableView key={i} table={table} />
      ))}
      {section.subsections.map((sub, i) => (
        <SectionView key={i} section={sub} />
      ))}
    </>
  )

  // Deep sections are collapsible to keep long articles navigable
  if (section.level >= 3 && section.title) {
    return (
      <details className="mb-4 group">
        <summary className="cursor-pointer font-medium text-navy-800 hover:text-ocean-600 transition-colors py-1 select-none">
          {renderInline(section.title)}
        </summary>
        <div className="pl-4 border-l-2 border-sand-200 mt-2">{body}</div>
      </details>
    )
  }

  return (
    <section className="mb-6">
      {section.title && (
        <h3 className="font-serif text-lg font-medium text-navy-900 mb-3 pb-2 border-b border-sand-200">
          {renderInline(section.title)}
        </h3>
      )}
      {body}
    </section>
  )
}

interface Block {
  type: 'p' | 'ul' | 'quote' | 'audit'
  lines: string[]
}

/**
 * Structural rendering of the markdown body: paragraphs, bullet lists,
 * blockquotes and — clearly labelled — internal audit review notes
 * (⚠️ ZU PRÜFEN), which are deliberate uncertainty markers in the corpus.
 */
function TextBlocks({ text }: { text: string }) {
  const blocks: Block[] = []
  let open = false // whether the last block accepts continuation lines

  for (const raw of text.split('\n')) {
    const line = raw.trim()
    if (line === '' || line === '---') {
      open = false
      continue
    }
    let type: Block['type']
    let content = line
    if (line.startsWith('>')) {
      content = line.replace(/^>\s?/, '')
      type = 'quote'
    } else if (/^[-*]\s+/.test(line)) {
      content = line.replace(/^[-*]\s+/, '')
      type = 'ul'
    } else {
      type = 'p'
    }
    const last = blocks[blocks.length - 1]
    if (open && last && last.type === type) {
      last.lines.push(content)
    } else {
      blocks.push({ type, lines: [content] })
      open = true
    }
  }

  // Blockquotes carrying corpus audit flags become labelled callouts
  for (const block of blocks) {
    if (block.type === 'quote' && /ZU[\s-]?PRÜFEN/i.test(block.lines.join(' '))) {
      block.type = 'audit'
    }
  }

  return (
    <>
      {blocks.map((block, i) => {
        switch (block.type) {
          case 'ul':
            return (
              <ul key={i} className="list-disc pl-5 mb-4 space-y-1 text-sm text-navy-800 leading-relaxed">
                {block.lines.map((line, j) => (
                  <li key={j}>{renderInline(line)}</li>
                ))}
              </ul>
            )
          case 'audit':
            return (
              <div
                key={i}
                className="mb-4 border-l-4 border-amber-400 bg-amber-50 rounded-r px-4 py-3 text-xs text-amber-900 leading-relaxed"
              >
                <p className="font-semibold mb-1">Interner Prüfvermerk (Qualitätssicherung)</p>
                {block.lines.map((line, j) => (
                  <p key={j}>{renderInline(line)}</p>
                ))}
              </div>
            )
          case 'quote':
            return (
              <div
                key={i}
                className="mb-4 border-l-4 border-sand-300 pl-4 text-sm text-navy-600 italic leading-relaxed"
              >
                {block.lines.map((line, j) => (
                  <p key={j}>{renderInline(line)}</p>
                ))}
              </div>
            )
          default:
            return (
              <p key={i} className="mb-4 text-sm text-navy-800 leading-relaxed">
                {renderInline(block.lines.join(' '))}
              </p>
            )
        }
      })}
    </>
  )
}

/**
 * Minimal, safe inline markdown: **bold**, `code`, [label](https://…).
 * Everything is emitted as React nodes; URLs are restricted to http(s).
 */
function renderInline(text: string): ReactNode[] {
  const pattern = /(\*\*[^*]+\*\*|`[^`]+`|\[[^\]]+\]\(https?:\/\/[^\s)]+\))/g
  const nodes: ReactNode[] = []
  let last = 0
  let i = 0
  let match: RegExpExecArray | null
  while ((match = pattern.exec(text)) !== null) {
    if (match.index > last) nodes.push(text.slice(last, match.index))
    const token = match[0]
    if (token.startsWith('**')) {
      nodes.push(
        <strong key={`b${i}`} className="font-semibold text-navy-900">
          {token.slice(2, -2)}
        </strong>,
      )
    } else if (token.startsWith('`')) {
      nodes.push(
        <code key={`c${i}`} className="px-1 py-0.5 bg-sand-100 rounded text-[0.85em] font-mono">
          {token.slice(1, -1)}
        </code>,
      )
    } else {
      const labelEnd = token.indexOf('](')
      const label = token.slice(1, labelEnd)
      const url = token.slice(labelEnd + 2, -1)
      nodes.push(
        <a
          key={`a${i}`}
          href={url}
          target="_blank"
          rel="noopener noreferrer"
          className="text-ocean-600 underline hover:text-ocean-700"
        >
          {label}
        </a>,
      )
    }
    last = match.index + token.length
    i += 1
  }
  if (last < text.length) nodes.push(text.slice(last))
  return nodes
}

function TableView({ table }: { table: CorpusTable }) {
  if (!table.columns.length || !table.rows.length) return null
  return (
    <div className="overflow-x-auto mb-4 rounded-lg border border-sand-200">
      <table className="min-w-full text-sm">
        <thead>
          <tr className="bg-sand-50">
            {table.columns.map((col, i) => (
              <th
                key={i}
                className="px-3 py-2 text-left font-medium text-navy-800 whitespace-nowrap"
              >
                {renderInline(col)}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {table.rows.map((row, i) => (
            <tr key={i} className="border-t border-sand-100">
              {row.map((cell, j) => (
                <td key={j} className="px-3 py-2 text-navy-700 align-top">
                  {renderInline(cell)}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
