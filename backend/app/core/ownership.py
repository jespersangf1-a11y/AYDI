"""Zugriffsregeln für Einträge mit einer Besitzerspalte.

Hintergrund: Materialien, Serviceberichte, Wettbewerbsmodelle und
Markenreferenzen verlangten zwar eine Anmeldung, prüften danach aber nicht,
*wem* ein Eintrag gehört. Jedes angemeldete Konto konnte damit die Einträge
jedes anderen Kontos lesen, ändern und löschen — auch die Werft-internen
Serviceberichte fremder Betriebe.

Das Modell hat zwei Arten von Einträgen:

Besitzerspalte IS NULL
    Mitgelieferter Referenzbestand (53 Materialien, 51 Wettbewerbsmodelle aus
    der Grundausstattung). Diese Sammlung ist der eigentliche Zweck der
    Materialdatenbank, also darf sie jedes angemeldete Konto lesen. Ändern
    und löschen darf sie nur die Verwaltung, sonst verändert ein einzelner
    Nutzer die Datengrundlage aller anderen.

Besitzerspalte = <Konto>
    Selbst angelegter Eintrag. Nur dieses Konto — und die Verwaltung — darf
    ihn sehen, ändern und löschen.

Nicht gefunden und nicht erlaubt werden beide mit 404 beantwortet. Ein 403
würde bestätigen, dass es die Kennung gibt, und damit verraten, welche
Einträge fremde Konten führen.

Zur Benennung der Spalte
------------------------
Die Besitzerspalte heißt nicht überall gleich: ``Material``,
``CompetitorModel`` und ``BrandReferenceModel`` führen sie als
``created_by_user_id``, ``ServiceReport`` als ``user_id``,
``QuickAnalysisResult`` als ``owner_id``. Die Zuordnung steht hier an *einer*
Stelle (``OWNER_ATTR``) statt verteilt über die Routen — sonst entstehen
wieder zwei Wahrheiten darüber, wem ein Eintrag gehört.
"""

from __future__ import annotations

from typing import Any
from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy import or_
from sqlalchemy.sql import Select

from app.models.models import User

#: Rollen, die den gesamten Bestand verwalten dürfen.
ADMIN_ROLES = frozenset({"admin"})

#: Modellname -> Name der Besitzerspalte.
#:
#: ``BrandReferenceModel`` steht hier bewusst NICHT: Markenreferenzen sind
#: org-weit sichtbar, und diese Regel steht als einziger Satz in
#: ``app.core.brand_visibility`` — geteilt zwischen den CRUD-Endpunkten und
#: dem Lader der ``brand_dna``-Analyse. Eine zweite, nur besitzerbezogene
#: Regel hier würde von jener abweichen, und genau dieses Auseinanderlaufen
#: lässt die Analyse fremde private Marken-DNA lesen.
OWNER_ATTR: dict[str, str] = {
    "Material": "created_by_user_id",
    "CompetitorModel": "created_by_user_id",
    "ServiceReport": "user_id",
    "QuickAnalysisResult": "owner_id",
}

#: Modelle, bei denen ein Eintrag ohne Besitzer der gemeinsame
#: Referenzbestand ist und deshalb von jedem gelesen werden darf.
#: ``ServiceReport`` steht bewusst NICHT hier: ein Servicebericht ohne
#: erkennbaren Besitzer ist kein Allgemeingut, sondern ein Datenrest — er
#: bleibt der Verwaltung vorbehalten.
SHARED_WHEN_UNOWNED = frozenset(
    {"Material", "CompetitorModel", "QuickAnalysisResult"}
)

#: Vorgabe, falls ein Modell nicht eingetragen ist.
DEFAULT_OWNER_ATTR = "owner_id"


def is_admin(user: User | None) -> bool:
    return user is not None and user.role in ADMIN_ROLES


def _model_name(model_or_entry: Any) -> str:
    if isinstance(model_or_entry, type):
        return model_or_entry.__name__
    return type(model_or_entry).__name__


def owner_attr(model_or_entry: Any) -> str:
    """Name der Besitzerspalte für dieses Modell."""
    return OWNER_ATTR.get(_model_name(model_or_entry), DEFAULT_OWNER_ATTR)


def owner_of(entry: Any) -> UUID | None:
    """Besitzer eines Eintrags, unabhängig davon, wie die Spalte heißt."""
    return getattr(entry, owner_attr(entry))


def _shared_stock(model_or_entry: Any) -> bool:
    return _model_name(model_or_entry) in SHARED_WHEN_UNOWNED


def visible_to(query: Select, model: type, user: User) -> Select:
    """Begrenze eine Abfrage auf das, was ``user`` sehen darf.

    Die Verwaltung sieht alles. Alle anderen sehen ihre eigenen Einträge —
    und, wo es einen gemeinsamen Referenzbestand gibt, auch diesen.
    """
    if is_admin(user):
        return query
    column = getattr(model, owner_attr(model))
    if _shared_stock(model):
        return query.where(or_(column.is_(None), column == user.id))
    return query.where(column == user.id)


def ensure_readable(entry: Any, user: User, *, name: str) -> Any:
    """Gib ``entry`` zurück, wenn ``user`` ihn lesen darf, sonst 404."""
    if entry is None:
        raise HTTPException(status_code=404, detail=f"{name} nicht gefunden")
    if is_admin(user):
        return entry
    besitzer = owner_of(entry)
    if besitzer is None and _shared_stock(entry):
        return entry
    if besitzer is not None and user is not None and besitzer == user.id:
        return entry
    raise HTTPException(status_code=404, detail=f"{name} nicht gefunden")


def ensure_writable(entry: Any, user: User, *, name: str) -> Any:
    """Gib ``entry`` zurück, wenn ``user`` ihn ändern darf, sonst 404 oder 403.

    Der gemeinsame Referenzbestand (Besitzerspalte ist NULL) ist ausdrücklich
    lesbar, aber nicht änderbar — dort meldet die Antwort 403 mit Begründung,
    weil die Existenz des Eintrags ohnehin öffentlich ist und ein 404 den
    Nutzer nur in die Irre führen würde.
    """
    if entry is None:
        raise HTTPException(status_code=404, detail=f"{name} nicht gefunden")
    if is_admin(user):
        return entry
    besitzer = owner_of(entry)
    if besitzer is None:
        if _shared_stock(entry):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=(
                    f"{name} gehört zum gemeinsamen Referenzbestand und kann nicht "
                    "geändert werden. Bitte einen eigenen Eintrag anlegen."
                ),
            )
        raise HTTPException(status_code=404, detail=f"{name} nicht gefunden")
    if user is not None and besitzer == user.id:
        return entry
    raise HTTPException(status_code=404, detail=f"{name} nicht gefunden")


def owner_id_for(user: User | None) -> UUID | None:
    """Besitzer für einen neu angelegten Eintrag."""
    return user.id if user is not None else None


def owner_kwargs(model: type, user: User | None) -> dict[str, Any]:
    """Schlüsselwort-Argument, um einen neuen Eintrag dem Nutzer zuzuordnen.

    Nimmt dem Aufrufer ab, den Spaltennamen zu kennen:
    ``Material(**data.model_dump(), **owner_kwargs(Material, user))``.
    """
    return {owner_attr(model): owner_id_for(user)}
