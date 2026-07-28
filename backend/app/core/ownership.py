"""Zugriffsregeln für Einträge mit einer Besitzerspalte.

Hintergrund: Materialien, Serviceberichte, Wettbewerbsmodelle und
Markenreferenzen verlangten zwar eine Anmeldung, prüften danach aber nicht,
*wem* ein Eintrag gehört. Jedes angemeldete Konto konnte damit die Einträge
jedes anderen Kontos lesen, ändern und löschen — auch die Werft-internen
Serviceberichte fremder Betriebe.

Das Modell hat zwei Arten von Einträgen:

``owner_id IS NULL``
    Mitgelieferter Referenzbestand (53 Materialien, 51 Wettbewerbsmodelle aus
    der Grundausstattung). Diese Sammlung ist der eigentliche Zweck der
    Materialdatenbank, also darf sie jedes angemeldete Konto lesen. Ändern
    und löschen darf sie nur die Verwaltung, sonst verändert ein einzelner
    Nutzer die Datengrundlage aller anderen.

``owner_id = <Konto>``
    Selbst angelegter Eintrag. Nur dieses Konto — und die Verwaltung — darf
    ihn sehen, ändern und löschen.

Nicht gefunden und nicht erlaubt werden beide mit 404 beantwortet. Ein 403
würde bestätigen, dass es die Kennung gibt, und damit verraten, welche
Einträge fremde Konten führen.
"""

from __future__ import annotations

from typing import Any, Protocol
from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy import or_
from sqlalchemy.sql import Select

from app.models.models import User

#: Rollen, die den gesamten Bestand verwalten dürfen.
ADMIN_ROLES = frozenset({"admin"})


class _HasOwner(Protocol):
    owner_id: Any
    id: Any


def is_admin(user: User) -> bool:
    return user.role in ADMIN_ROLES


def visible_to(query: Select, model: type[_HasOwner], user: User) -> Select:
    """Begrenze eine Abfrage auf das, was ``user`` sehen darf.

    Die Verwaltung sieht alles. Alle anderen sehen den gemeinsamen
    Referenzbestand und ihre eigenen Einträge.
    """
    if is_admin(user):
        return query
    return query.where(
        or_(model.owner_id.is_(None), model.owner_id == user.id)
    )


def ensure_readable(entry: Any, user: User, *, name: str) -> Any:
    """Gib ``entry`` zurück, wenn ``user`` ihn lesen darf, sonst 404."""
    if entry is None:
        raise HTTPException(status_code=404, detail=f"{name} nicht gefunden")
    if is_admin(user):
        return entry
    if entry.owner_id is None or entry.owner_id == user.id:
        return entry
    raise HTTPException(status_code=404, detail=f"{name} nicht gefunden")


def ensure_writable(entry: Any, user: User, *, name: str) -> Any:
    """Gib ``entry`` zurück, wenn ``user`` ihn ändern darf, sonst 404 oder 403.

    Der gemeinsame Referenzbestand (``owner_id`` ist NULL) ist ausdrücklich
    lesbar, aber nicht änderbar — dort meldet die Antwort 403 mit Begründung,
    weil die Existenz des Eintrags ohnehin öffentlich ist und ein 404 den
    Nutzer nur in die Irre führen würde.
    """
    if entry is None:
        raise HTTPException(status_code=404, detail=f"{name} nicht gefunden")
    if is_admin(user):
        return entry
    if entry.owner_id is None:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=(
                f"{name} gehört zum gemeinsamen Referenzbestand und kann nicht "
                "geändert werden. Bitte einen eigenen Eintrag anlegen."
            ),
        )
    if entry.owner_id == user.id:
        return entry
    raise HTTPException(status_code=404, detail=f"{name} nicht gefunden")


def owner_id_for(user: User | None) -> UUID | None:
    """Besitzer für einen neu angelegten Eintrag."""
    return user.id if user is not None else None
