# Entscheidungsvorlage: Team-Modell (Säule 4 — Werft-Teams)

## Warum jetzt

Die Realtime-Collaboration ist technisch fertig, aber per Definition unbenutzbar: `_user_owns_layout` (collaborate.py:19-30) lässt nur den Owner in den WebSocket-Kanal — ein zweiter Teilnehmer wird mit 4003 abgewiesen, obwohl Broadcast/Exclude bereits für Mehrbenutzer gebaut ist. Gleichzeitig verkaufen wir mit ENTERPRISE die Features `multi_tenancy` und `fleet_management`, die im Code nichts als Enum-Werte sind (subscription.py:75/78, keine einzige `require_feature`-Stelle). Für die Werft-Personas (Sarah, die Konstrukteurin im Team; Elena, die Werft-Leiterin mit mehreren Projekten und Abrechnungsverantwortung) ist AYDI damit heute ein Einzelplatz-Werkzeug — Säule 4 löst dieses Versprechen ein.

## Ist-Zustand in Kürze

- **Strikt Single-Owner:** Alles hängt an `Project.user_id` (models.py:22). Keine Member-, Share- oder Team-Tabelle existiert. Ownership-Kette: Layout → Project → genau ein User.
- **Zwei Chokepoints statt 33 Baustellen:** Alle Zugriffschecks laufen über zwei Helper-Muster (`_get_project`, `_verify_project_ownership`) — 8 Definitionen in 8 Route-Dateien, 33 Aufrufstellen. Für ein Team-Modell müssen nur die 8 Helper-Definitionen angepasst werden, nicht die Callsites.
- **`User.shipyard_id` ist toter Freitext:** String ohne FK, ohne Shipyard-Tabelle, nur bei Registrierung client-supplied gesetzt (auth.py:49/152), nirgendwo in Autorisierung oder Queries genutzt. Zwei User mit gleicher `shipyard_id` sehen heute exakt nichts voneinander.
- **Collaboration: nur das Berechtigungsmodell fehlt:** WS-Mechanik (cursor, zone_edit, comment, broadcast) ist mehrteilnehmerfähig; owner-only-Gate ist eine bewusste, dokumentierte Sicherheitsentscheidung (collaborate.py:42-44). Zusätzlich offen: kein Tier-Gate `Feature.COLLABORATION` am WS-Endpoint, keine Kanal-Rollen, comment/zone_edit nicht persistiert.
- **ENTERPRISE-Flags ohne Substanz:** `FLEET_MANAGEMENT`/`MULTI_TENANCY` werden außer in subscription.py selbst nirgendwo referenziert.
- **`BrandReferenceModel.shipyard_id` ist ein bekanntes Leck:** Freitext ohne Ownership — jeder eingeloggte User sieht/löscht alle Brand-References (Audit-Befund audit_report_code_2026-07-14.md:198).
- **Migrations-Infrastruktur bereit:** Lineare Alembic-Kette 000→001→002; ein Team-Modell wäre schlicht `003_*`.
- **Tenancy-Absicherung nur applikationsseitig:** VERIFICATION_PROTOCOL.md Punkte 15 (RLS: OPEN) und 16 (Multi-Tenancy: PARTIAL) dokumentieren, dass es keine DB-seitige Trennung gibt.

## Option A — Projekt-Sharing (leichtgewichtig)

**Modell:** Eine Tabelle `project_members` (`project_id`, `user_id`, `role` ∈ viewer/editor, unique auf project+user). Owner bleibt `Project.user_id`; Membership ergänzt, ersetzt nicht.

**Schaltet frei:**
- Collab-Beitritt für Eingeladene: `_user_owns_layout` → `_user_can_access_layout` (Owner ODER Member) — die WS-Mechanik läuft danach sofort mit mehreren Teilnehmern.
- Geteilte Projekte in der Projektliste („mit mir geteilt").
- Erste echte Rollen-Semantik: viewer = lesend (GET-Pfade), editor = schreibend (Mutationen); Owner-only bleibt Löschen/Teilen.

**Aufwand: S–M.**
- 1 Tabelle + Migration `003` (S).
- Die 8 Helper-Definitionen um Membership-Check erweitern; Signatur bekommt einen `required_role`-Parameter, damit viewer nicht schreiben kann. Callsites bleiben weitgehend unberührt (M, weil read/write pro Callsite klassifiziert werden muss).
- Minimaler Einladungs-Flow: Endpoint „Mitglied per E-Mail hinzufügen/entfernen" (S).

**Löst NICHT:**
- Keine Werft als Entität — Elena kann kein Team verwalten, nur Sarah kann Projekt für Projekt einzeln teilen.
- Keine Werft-Abrechnung / Sitzplatz-Lizenzierung; ENTERPRISE-`multi_tenancy`/`fleet_management` bleiben uneingelöst.
- `shipyard_id`-Freitext und Brand-Reference-Leck bleiben bestehen.

## Option B — Organisations-Modell (Werft als Entität)

**Modell:** `organizations`-Tabelle + `organization_members` (user_id, org_role ∈ owner/admin/member) + `Project.org_id` (nullable — private Projekte bleiben möglich). `User.shipyard_id` wird durch echten FK abgelöst; `BrandReferenceModel.shipyard_id` wird auf `org_id` migriert und damit das Audit-Leck geschlossen.

**Schaltet frei:**
- `multi_tenancy` und `fleet_management` werden real: Werft sieht alle Org-Projekte, Flottensicht, org-weite Brand-DNA.
- Werft-Abrechnung: ENTERPRISE-Tier hängt an der Org, nicht am Einzeluser — Sitzplätze verwaltbar.
- Elenas Use Case vollständig: Team einladen, Rollen vergeben, Projekte gehören der Werft.

**Aufwand: L.**
- 2–3 Tabellen + Migration inkl. Datenmigration der bestehenden Freitext-`shipyard_id` (M).
- Alle 8 Helper plus Query-Pfade („meine Projekte" → „meine + Org-Projekte"), Tier-Auflösung User→Org in `context.tier`, Invitation-Flow mit Pending-State, Org-Verwaltungs-UI (L).
- Berührt Abrechnungslogik und Registrierung — höchstes Regressionsrisiko, und RLS-Frage (Protokoll-Punkt 15) wird drängender.

## Option C — Hybrid/Stufenplan

**Stufe 1 = Option A jetzt** (project_members, Helper-Erweiterung, Collab-Freischaltung, minimaler Invite).
**Stufe 2 = Option B darauf**, wenn zahlende Werft-Nachfrage da ist: `organizations` kommt hinzu, `project_members` bleibt unverändert gültig als feingranulare Ebene (Org-Zugehörigkeit gibt Basiszugriff, project_members regelt Einzelfreigaben und externe Gäste — ein etabliertes Muster, z. B. GitHub Org + Repo-Collaborators).

Kein Wegwerf-Code: Die in Stufe 1 gebaute Rolle-im-Projekt-Semantik (viewer/editor) und der erweiterte Helper (`can_access(project, user, required_role)`) sind exakt die Stelle, an der Stufe 2 nur eine weitere OR-Bedingung (Org-Membership) einhängt.

## Auswirkungs-Tabelle

| | Migration | Routen-/Helper-Änderungen | Collab-Freischaltung | ENTERPRISE-Einlösung | Risiko |
|---|---|---|---|---|---|
| **A** | S (1 Tabelle, `003`) | M (8 Helper-Defs + read/write-Klassifikation, 33 Callsites fast unberührt) | Ja, sofort (`_user_can_access_layout`) | Nein | Niedrig — additiv, Single-Owner-Pfad bleibt Default |
| **B** | M–L (2–3 Tabellen + Datenmigration Freitext-`shipyard_id`) | L (8 Helper + Listen-Queries + Tier-Auflösung + Invite-Flow) | Ja | Ja, vollständig (`multi_tenancy`, `fleet_management`, Werft-Billing) | Mittel–hoch — berührt Auth, Billing, Registrierung; RLS-Frage wird akut |
| **C** | S jetzt, M–L später | M jetzt, Rest später | Ja, sofort | Ja, in Stufe 2 | Niedrig jetzt; Stufe-2-Risiko entkoppelt und bei Bedarf |

## Empfehlung: Option C — Option A jetzt bauen, B als definierte Ausbaustufe

Begründung aus der Ist-Aufnahme:

1. **Die Architektur belohnt A überproportional.** Der gesamte Zugriffsschutz konzentriert sich auf 8 Helper-Definitionen — der teuerste Teil eines Sharing-Modells (33 Stellen absichern) ist hier ungewöhnlich billig. A liefert das sichtbarste tote Kapital (fertige Collab-Infrastruktur) mit S–M-Aufwand aus.
2. **B jetzt wäre eine Wette ohne Daten.** Es gibt heute keinen einzigen zahlenden Werft-Tenant; `shipyard_id` wurde nie mit Semantik nachgefragt. Ein Org-Modell vorab zu bauen hieße, Billing-, Invite- und Tenancy-Komplexität für eine Hypothese zu tragen — inklusive der offenen RLS-Baustelle (Protokoll 15/16), die bei echter Multi-Tenancy nicht mehr aufschiebbar ist.
3. **C ist kein fauler Kompromiss, weil A unter B weiterlebt.** project_members bleibt im Org-Modell die Einzelfreigabe-Ebene; nichts wird zurückgebaut. Die Entscheidung „B ja/nein" wird auf den Zeitpunkt verschoben, an dem eine Werft dafür bezahlt — mit A als funktionierendem Proof für den Verkauf.
4. **Zwei Aufräumarbeiten gehören unabhängig von der Wahl dazu:** das Tier-Gate `Feature.COLLABORATION` am WS-Endpoint (fehlt heute schlicht) und das Brand-Reference-Leck (jeder User löscht alles) — Letzteres wird in Stufe 1 mindestens auf Ownership gezogen, in Stufe 2 auf die Org.

Einzige Bedingung: Beim Bau von A **keine** Abkürzungen, die B blockieren — konkret: Rollen als Enum (erweiterbar), Helper-Signatur mit `required_role`, Einladung per User-Referenz statt E-Mail-Freitext in der Tabelle.

## Was ich nach deiner Entscheidung sofort umsetzen würde (bei C / A-zuerst)

- **Migration `003_project_members`:** Tabelle (project_id FK CASCADE, user_id FK CASCADE, role viewer/editor, created_at, unique project+user) — reiht sich in die bestehende Alembic-Kette 000→002 ein.
- **Helper-Umbau:** `_get_project`/`_verify_project_ownership` in allen 8 Route-Dateien auf gemeinsamen Kern `can_access(project_id, user, min_role)` ziehen (Owner ⇒ immer; Member ⇒ Rolle prüfen); Callsites nach read (viewer reicht) vs. write (editor) klassifizieren, Löschen/Teilen bleibt owner-only.
- **Collab scharfschalten:** `_user_owns_layout` → `_user_can_access_layout` (collaborate.py), gleichzeitig `require_feature(Feature.COLLABORATION)` am WS-Endpoint nachziehen (heute ungeprüft).
- **Sharing-Endpoints:** `POST/DELETE /projects/{id}/members` (owner-only) + Membership in `GET /projects`-Listing als „mit mir geteilt".
- **Frontend minimal:** Teilen-Dialog am Projekt (E-Mail + Rolle), Badge „geteilt", viewer-Modus read-only.
- **Brand-Reference-Leck stopfen:** Create/Delete an `user_id` binden (Vorgriff auf Org-Ownership in Stufe 2), Audit-Befund schließen.
- **VERIFICATION_PROTOCOL aktualisieren:** Punkt 16 auf den neuen Stand heben, RLS (Punkt 15) explizit als Vorbedingung für Stufe 2 (Org-Modell) markieren + Tests: Fremdzugriff 404, viewer-Schreibversuch 403, WS-Beitritt als Member.
