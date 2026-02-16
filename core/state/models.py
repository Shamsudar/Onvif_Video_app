from __future__ import annotations

from dataclasses import dataclass, field
from typing import Tuple


@dataclass(frozen=True, slots=True)
class Session:
    is_authenticated: bool
    user_id: int | None
    username: str
    role: str
    capabilities: Tuple[str, ...] = field(default_factory=tuple)
    must_change_password: bool = False
    auth_source: str = "local"


@dataclass(frozen=True, slots=True)
class AppStateSnapshot:
    session: Session
    connection_status: str = "disconnected"
    layout_state: str = "default"
    has_unsaved_layout: bool = False
    last_error: str | None = None


def default_unauthenticated_session() -> Session:
    return Session(
        is_authenticated=False,
        user_id=None,
        username="",
        role="guest",
        capabilities=(),
        must_change_password=False,
        auth_source="local",
    )


def default_app_state() -> AppStateSnapshot:
    return AppStateSnapshot(session=default_unauthenticated_session())
