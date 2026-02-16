from __future__ import annotations

from collections.abc import Callable
from dataclasses import replace

from .models import AppStateSnapshot, Session, default_app_state

StateSubscriber = Callable[[AppStateSnapshot, str], None]


class AppStateStore:
    def __init__(self, initial_state: AppStateSnapshot | None = None) -> None:
        self._state = initial_state or default_app_state()
        self._subscribers: list[StateSubscriber] = []

    @property
    def state(self) -> AppStateSnapshot:
        return self._state

    def subscribe(self, callback: StateSubscriber) -> Callable[[], None]:
        if callback not in self._subscribers:
            self._subscribers.append(callback)

        def _unsubscribe() -> None:
            self.unsubscribe(callback)

        return _unsubscribe

    def unsubscribe(self, callback: StateSubscriber) -> None:
        self._subscribers = [sub for sub in self._subscribers if sub != callback]

    def reset(self) -> None:
        self._set_state(default_app_state(), event="state.reset")

    def set_session(self, session: Session) -> None:
        self._set_state(replace(self._state, session=session), event="auth.changed")

    def set_connection_status(self, status: str) -> None:
        self._set_state(
            replace(self._state, connection_status=status),
            event="connection.changed",
        )

    def set_layout_state(self, layout_state: str) -> None:
        self._set_state(replace(self._state, layout_state=layout_state), event="layout.changed")

    def set_unsaved_layout(self, has_unsaved_layout: bool) -> None:
        self._set_state(
            replace(self._state, has_unsaved_layout=has_unsaved_layout),
            event="layout.unsaved.changed",
        )

    def set_last_error(self, error: str | None) -> None:
        self._set_state(replace(self._state, last_error=error), event="error.changed")

    def _set_state(self, new_state: AppStateSnapshot, event: str) -> None:
        if new_state == self._state:
            return
        self._state = new_state
        for callback in list(self._subscribers):
            callback(self._state, event)
