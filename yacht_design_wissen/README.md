# Yacht-Designsprachen & Stile — Studien-Übersicht

Diese Wissensbasis zu **Exterieur- und Interieur-Designsprachen von Yachten** (Marken, Epochen, Jahre) ist **in den AYDI-Wissenskorpus verdrahtet** als **Kategorie 32 „Designsprachen und Stile"**. Die Dossiers liegen als kanonische Korpus-Dokumente unter [`backend/app/services/knowledge/`](../backend/app/services/knowledge/) (`32_01…32_09`) und werden dadurch automatisch geladen und über die Lexikon-API ausgespielt.

> Dieses Verzeichnis enthält bewusst nur diese Übersicht — der Inhalt lebt **einmal** im Korpus (keine Duplikate, kein Drift).

---

## Wo die Inhalte leben

**Geladen vom Korpus-Loader** (`markdown_knowledge_loader.py`, Muster `NN_MM_slug.md`) und im **`KNOWLEDGE_INDEX`** unter `22.33_designsprachen_stile` registriert:

| Dok | Datei | Inhalt |
|---|---|---|
| 32_08 | [32_08_epochen_taxonomie_designer.md](../backend/app/services/knowledge/32_08_epochen_taxonomie_designer.md) | **Konzeptioneller Unterbau:** 7 Epochen, 13 Stil-Kategorien, Design-Vokabular, legendäre Designer |
| 32_01 | [32_01_serien_segelcruiser.md](../backend/app/services/knowledge/32_01_serien_segelcruiser.md) | Serien-Segelcruiser |
| 32_02 | [32_02_blauwasser_cruiser.md](../backend/app/services/knowledge/32_02_blauwasser_cruiser.md) | Blauwasser-/Qualitätscruiser |
| 32_03 | [32_03_performance_cruiser.md](../backend/app/services/knowledge/32_03_performance_cruiser.md) | Performance-Cruiser + Rating-Rule-Evolution |
| 32_04 | [32_04_multihulls_katamarane.md](../backend/app/services/knowledge/32_04_multihulls_katamarane.md) | Katamarane (Segel & Motor) |
| 32_05 | [32_05_motor_sportcruiser.md](../backend/app/services/knowledge/32_05_motor_sportcruiser.md) | Motor-Sportcruiser/Flybridge |
| 32_06 | [32_06_trawler_explorer_downeast.md](../backend/app/services/knowledge/32_06_trawler_explorer_downeast.md) | Trawler/Explorer/Downeast |
| 32_07 | [32_07_superyachten_studios.md](../backend/app/services/knowledge/32_07_superyachten_studios.md) | Superyachten (24 m+) & Design-Studios |
| 32_09 | [32_09_synthese_designmuster.md](../backend/app/services/knowledge/32_09_synthese_designmuster.md) | **Quer-Synthese:** 7 universelle Muster + Klassifikator-Signale (Pipeline-B-Cues, `brand_dna`-Priors) |

**Über die API erreichbar** (öffentlich, Lexikon/Säule 1):
- `GET /api/v1/knowledge/corpus/categories` → Kategorie `32` „Designsprachen und Stile" mit 9 Dokumenten
- `GET /api/v1/knowledge/corpus/documents/{slug}` → z. B. `.../serien_segelcruiser`
- `GET /api/v1/knowledge/search?q=…` → Voll­text über Titel & Korpus

---

## Zweck (AYDI-Anbindung)
Speist Säule 1 (Lexikon), Säule 2 (Kaufberatung: Epochen-/Stil-Einordnung eines konkreten Boots), die visuelle Pipeline B (Erkennungs-Cues in 32_09) und die Module `brand_dna`, `emotional`, `production`, `materials`. **Vertrauensregel bleibt in Kraft:** Stil-/Epochen-Zuordnung ist eine *Einordnung*, keine Messung → im Zweifel `estimated`/`benchmark`, nie als Fakt; „ca./unbestätigt"-Angaben vor produktiver Nutzung gegen Primärquellen prüfen.

---

## Zielerreichung der Studie (Mindestwerte)

| Achse | Ziel | Erreicht |
|---|---|---|
| **Marken/Werften** | ≥ 30 | **~75** über alle Segmente |
| **Epochen** | ≥ 7 | **7** Segel-Epochen (32_08) + 4 Motor-Wellen + 4 Kat-Epochen |
| **Design-Dimensionen** | Ext+Int+Designer+Evolution je Marke | erfüllt |
| **Stil-Taxonomie** | ≥ 12 benannte Designsprachen | **13** (B1–B13 in 32_08) |
| **Umfang** | strukturierte Wissensbasis | 9 Korpus-Dokumente, ~1.900 Zeilen, echte Modelle/Jahre/Designer mit Unsicherheits-Flags |

**Alle Mindestziele erreicht bzw. übertroffen.**

---

## Methodik & Grenzen
- **Recherche:** acht parallele Fach-Rechercheagenten (Web-Suche gegen Werft-Historien und Fachpresse — Yacht, Yachting World, SAIL, PBO, Boat International, SuperYacht Times —, sailboatdata, Wikipedia, Studioseiten). Verbreitete Irrtümer wurden korrigiert (u. a. Oyster SJ35 = Stephen Jones; Hylas 42/44 = Frers statt S&S; Eclipse & Motor Yacht A = Blohm+Voss statt Lürssen; ClubSwan 36 = Juan K statt Verdier).
- **Grenzen:** Design-Sprach-Zuordnung ist interpretativ; einzelne Jahres-/Autor-Angaben sind mit „ca./unbestätigt" markiert. Private Eigner werden bewusst nicht genannt. Verbleibende Lücken sind als Unsicherheit ausgewiesen, nicht geraten.
- **Nächste Ausbaustufen (optional):** Verknüpfung der 32_09-Erkennungs-Cues mit den `brand_dna`-Referenzmodellen; Bild-Cue-Katalog für Pipeline B; strukturierte Firmenprofile im Korpus-Format (für den Hersteller-Extraktor).
