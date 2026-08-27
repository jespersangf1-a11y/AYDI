import DOMPurify from 'dompurify'

/**
 * Wissensartikel liefern vorformatiertes HTML (`content_html`). Dieses HTML
 * wurde bisher unveraendert per `dangerouslySetInnerHTML` eingehaengt — wer
 * einen Artikel schreiben konnte, konnte damit Skriptcode im Browser jedes
 * Lesers ausfuehren.
 *
 * Erlaubt ist nur das, was ein Fachartikel wirklich braucht: Ueberschriften,
 * Absaetze, Listen, Tabellen, Hervorhebungen und Links. Alles andere —
 * insbesondere `script`, `style`, `iframe`, Event-Attribute wie `onerror`
 * und `javascript:`-Adressen — wird entfernt.
 */
const ALLOWED_TAGS = [
  'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
  'p', 'br', 'hr', 'span', 'div',
  'strong', 'b', 'em', 'i', 'u', 'sub', 'sup', 'small', 'mark',
  'ul', 'ol', 'li', 'dl', 'dt', 'dd',
  'blockquote', 'code', 'pre',
  'table', 'thead', 'tbody', 'tfoot', 'tr', 'th', 'td', 'caption', 'colgroup', 'col',
  'a', 'abbr', 'figure', 'figcaption',
]

const ALLOWED_ATTR = ['href', 'title', 'lang', 'dir', 'colspan', 'rowspan', 'scope', 'class']

export function sanitizeHtml(html: string): string {
  return DOMPurify.sanitize(html, {
    ALLOWED_TAGS,
    ALLOWED_ATTR,
    // Keine Datenquellen von aussen, keine Formulare, keine eingebetteten Objekte.
    FORBID_TAGS: ['script', 'style', 'iframe', 'object', 'embed', 'form', 'input', 'link', 'meta'],
    FORBID_ATTR: ['style', 'srcset', 'formaction', 'ping'],
    // Nur http(s) und mailto — schliesst javascript: und data: aus.
    ALLOWED_URI_REGEXP: /^(?:https?:|mailto:|[^a-z]|[a-z+.\-]+(?:[^a-z+.\-:]|$))/i,
    RETURN_TRUSTED_TYPE: false,
  })
}

// Externe Links sollen das Ursprungsfenster nicht ansprechen koennen.
if (typeof window !== 'undefined') {
  DOMPurify.addHook('afterSanitizeAttributes', (node) => {
    if (node instanceof HTMLAnchorElement && node.hasAttribute('href')) {
      node.setAttribute('target', '_blank')
      node.setAttribute('rel', 'noopener noreferrer nofollow')
    }
  })
}
