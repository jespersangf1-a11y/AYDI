/**
 * Strict German-aware number parsing for form inputs.
 *
 * parseFloat silently mis-reads German formats: '2.000' (two thousand)
 * becomes 2, '1.234,5' becomes 1.234, and trailing garbage ('240abc') is
 * accepted. In a UI that DISPLAYS numbers via toLocaleString('de-DE'), that
 * teaches users exactly the format the input then parses wrong — corrupting
 * analysis inputs without any error.
 *
 * Accepted formats (whitespace-trimmed, optional leading minus):
 *   "1234"        → 1234
 *   "1234.5"      → 1234.5   (dot as decimal separator)
 *   "1234,5"      → 1234.5   (comma as decimal separator)
 *   "1.234"       → 1234     (German thousands grouping)
 *   "1.234,5"     → 1234.5   (German grouping + decimal comma)
 *   "1.234.567"   → 1234567
 * Everything else (mixed/ambiguous separators, letters) → null.
 */
export function parseLocaleNumber(raw: string): number | null {
  const text = raw.trim()
  if (text === '') return null

  // German grouping: 1.234 / 1.234.567 / 1.234,5
  if (/^-?\d{1,3}(\.\d{3})+(,\d+)?$/.test(text)) {
    return Number(text.replace(/\./g, '').replace(',', '.'))
  }
  // Plain number with a single decimal separator (dot or comma)
  if (/^-?\d+([.,]\d+)?$/.test(text)) {
    return Number(text.replace(',', '.'))
  }
  return null
}
