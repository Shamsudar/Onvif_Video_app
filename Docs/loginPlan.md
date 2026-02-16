# VMS Phase 1 Login Implementation Plan

## 1. Objective
Implement a secure and architecture-aligned login phase for Phase 1:
- Always start at login.
- Authenticate against local SQLite.
- Force password change on first login.
- Route to dashboard only after successful authentication.
- Fully reset app session/state on logout and idle timeout.

Implementation priority for immediate next step:
- Build the application shell/router and baseline AppState first.

## 2. Current-State Summary
- UI mock for login exists (`LoginWidget.ui`) and is loaded by `main.py`.
- Password show/hide toggle exists.
- No application shell/router exists yet.
- No `AppState`, `Session`, `AuthService`, or SQLite integration yet.
- No logout flow, timeout handling, or role/capability enforcement yet.

## 3. Target Architecture for Login Phase
Create these runtime modules and keep strict separation:
- `Session` model: immutable object with auth status, identity, role, capabilities, flags.
- `AppState`: single source of truth; stores current `Session`; emits auth/state events.
- `AuthService`: SQLite-backed credential validation, password change, lockout policy hooks.
- `MainWindow` router: listens to `AppState` auth changes and switches screens.
- `LoginWidget` controller logic: gathers inputs and delegates auth to `AuthService`.
- `PolicyService` (minimal in Phase 1): role to capability mapping.

### 3.1 First Deliverable (Now): Application Shell + Router + Default AppState
Scope for the first implementation slice:
- Introduce `MainWindow` as the application shell and route owner.
- Host screens in a central stack/container controlled only by router decisions.
- Define and instantiate default `AppState` at startup.
- Subscribe router to AppState events (`auth.changed` minimum).
- Ensure startup route always resolves to Login for unauthenticated session.

Out of scope for this first slice:
- Real credential validation and SQLite auth checks.
- Password-change execution logic.
- Role permission enforcement beyond baseline placeholders.

## 4. Login Flow Design
1. App startup:
- Initialize `AppState` with unauthenticated immutable session.
- Build `MainWindow`.
- `MainWindow` subscribes to `auth.changed`.
- Route to login screen by default.

2. Login submission:
- Validate non-empty username/password on UI side.
- Call `AuthService.authenticate(username, password)`.
- On failure: return generic error and increment attempt tracking.
- On success: create new immutable authenticated `Session`.
- Replace session in `AppState`.

3. First-login password change:
- If session flag `must_change_password` is true, route to password-change screen.
- Block dashboard access until password update succeeds.
- On success: clear flag in SQLite and refresh `Session` in `AppState`.

4. Post-auth routing:
- `MainWindow` receives auth change event.
- Route to dashboard only when authenticated and password-change requirement is cleared.

5. Logout/timeout:
- Prompt on unsaved layout state (when applicable).
- Stop streams/services.
- Replace session with fresh unauthenticated session.
- Clear volatile runtime state and route to login.

## 4A. Default AppState Data Contract (Phase 1 Baseline)
Define a stable startup state before auth integration:
- `session`:
  - `is_authenticated = false`
  - `user_id = null`
  - `username = ""`
  - `role = "guest"`
  - `capabilities = []`
  - `must_change_password = false`
  - `auth_source = "local"`
- `connection_status = "disconnected"`
- `layout_state = "default"`
- `has_unsaved_layout = false`
- `last_error = null`

Rules:
- Session is immutable and replaced atomically on auth/logout transitions.
- AppState is the only source read by router for screen decisions.

## 5. SQLite/Auth Data Plan
Use a local database with at least:
- `users`: `id`, `username` (unique), `password_hash`, `salt` (if required), `role`, `is_active`, `must_change_password`, `failed_attempts`, `locked_until`, `created_at`, `updated_at`.

Operational requirements:
- Seed default admin user on first run (forced password change enabled).
- Store only password hashes, never plaintext.
- Normalize username matching rules (case sensitivity policy fixed and documented).
- Add migration/version strategy for schema evolution.

## 6. Security and Policy Baseline
- Enforce credential checks and account state in `AuthService`, not in UI.
- Return generic login failure messages (avoid user enumeration).
- Keep role/capability checks in service layer.
- On logout/timeout, purge sensitive in-memory fields.
- Add basic throttling/temporary lock after repeated failures.

## 7. Idle Timeout Plan
- Add global activity tracking (keyboard/mouse/focus events).
- Reset inactivity timer on activity.
- Trigger standard logout flow after configured threshold.
- Make timeout value configurable in local settings.

## 8. Delivery Milestones
1. Core runtime scaffolding (current priority):
- `Session`, `AppState`, `MainWindow` router, screen host.
- Startup initializes baseline AppState contract.
- Router is event-driven from AppState and not hard-wired to a widget.
- Login is shown through router resolution, not direct bootstrapping.

2. Auth foundation:
- SQLite schema setup, seed default user, password hash/verify path, `AuthService`.

3. Login integration:
- Wire `LoginWidget` to `AuthService` and `AppState`; handle errors/states.

4. First-login password change:
- Add screen/flow; enforce pre-dashboard gating.

5. Logout and timeout:
- Centralized reset flow; idle timeout trigger.

6. Hardening and QA:
- Negative tests, lockout behavior, startup/login/logout timeout regression checks.

## 8A. Acceptance Criteria for First Slice (Shell + Router + AppState)
- Application starts through shell/router entry point.
- AppState exists at startup with the full default data contract.
- Router subscribes to AppState auth event and resolves initial Login route.
- Screen transitions are centralized in router methods only.
- No UI component directly owns global auth state.
- State reset path can restore baseline unauthenticated AppState shape.

## 9. Validation Checklist
- App always opens on login when unauthenticated.
- Valid credentials create authenticated session and route correctly.
- Invalid credentials never expose sensitive details.
- First login forces password change before dashboard.
- Logout always returns to clean unauthenticated state.
- Idle timeout behaves exactly like logout.
- Service-layer permission checks remain effective even if UI controls are bypassed.
