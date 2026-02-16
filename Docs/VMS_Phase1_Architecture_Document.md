# VMS Desktop Application
## Phase 1 Architecture Document

---

## 1. Goals and Scope

This document defines the architecture for Phase 1 of the Video Management System (VMS) desktop application.

**Phase 1 Characteristics:**
- Single-user desktop application
- Local authentication using SQLite
- Always show Login screen on startup
- Default credentials on first run
- Force password change after first login
- Full reset on logout or idle timeout

The architecture is designed to scale later into a multi-user, server-based enterprise deployment.

---

## 2. Architectural Principles

- Clear separation of concerns
- Centralized application state
- Push-based state updates
- Immutable session model
- Business logic separated from UI
- Security enforced at service layer

---

## 3. Layered Architecture Overview

### UI Layer (Views)
- Qt Widgets
- Responsible for presentation only
- Maintains local micro-state only

### Routing Layer (MainWindow)
- Controls screen transitions
- Subscribes to AppState events
- Handles logout prompts

### AppState Layer
- Central runtime state manager
- Always contains a Session object
- Broadcasts state changes
- Defines a stable default state shape from app startup

### Authentication Service
- Validates credentials against SQLite
- Returns immutable Session object

### Policy/Authorization Service
- Defines fixed capability vocabulary
- Maps roles to capabilities (Phase 1)

### Application Services
- Business logic layer
- Enforces permissions via Policy Service

### Streaming/Connection Service
- Owns connect/reconnect logic
- Reports aggregated status to AppState

### Persistence Layer
- SQLite database (users, credentials)
- Local settings file (UI preferences)

---

## 4. Session Model

The Session object is:

- Immutable
- Always present (authenticated or unauthenticated)
- Replaced entirely on login/logout
- Contains identity, role, and authentication state

### Default Unauthenticated Session (Startup)
At application startup, AppState must initialize with a default unauthenticated session:
- `is_authenticated = false`
- `user_id = null`
- `username = ""`
- `role = "guest"`
- `capabilities = []`
- `must_change_password = false`
- `auth_source = "local"`

This object must be treated as immutable and replaced, never mutated in place.

---

## 5. State Broadcasting Events

AppState broadcasts:

- Authentication Changed
- Connection Status Changed
- Layout Changed
- Unsaved Layout Changed

### AppState Default Structure (Phase 1 Baseline)
Before authentication is integrated, AppState should expose a default runtime structure:
- `session`: unauthenticated immutable session (always present)
- `connection_status`: `"disconnected"` at startup
- `layout_state`: default layout identifier/value
- `has_unsaved_layout`: `false` at startup
- `last_error`: `null` at startup

This baseline enables router/view wiring before business services are added.

---

## 6. Core Runtime Flows

### Startup
- Initialize AppState with unauthenticated session
- Route to Login screen
- Router decision at startup is based only on AppState (not direct widget creation)

### Login
- LoginWidget calls AuthService
- AuthService validates via SQLite
- AppState replaces session
- MainWindow routes to Dashboard

### Logout
- Prompt if unsaved layout changes
- Stop all streams
- Replace session with unauthenticated session
- Route to Login

### Idle Timeout
- Detect inactivity via user input
- Trigger logout flow

### Connection Drop
- Streaming service attempts reconnect
- UI remains usable with limited functionality

---

## 7. Phase 1 Delivery Order

The delivery order for implementation should be:

1. Application Shell + Router + Default AppState
- Create MainWindow shell/router and central screen host.
- Initialize full default AppState structure at startup.
- Subscribe router to AppState events and enforce startup route to Login.

2. Authentication Service + SQLite integration
- Add credential validation and session creation.

3. Login flow integration
- Connect Login UI submission to AuthService and AppState replacement.

4. First-login password change gate
- Enforce pre-dashboard password update path.

5. Logout and idle-timeout reset
- Ensure full reset to unauthenticated baseline state.

---

## 8. Security Model

- UI hides/disables restricted actions
- Services enforce permissions strictly
- Full reset on logout or idle timeout

---

## 9. Future Scalability

- Replace SQLite auth with server-based PostgreSQL
- Add token-based authentication
- Expand from role-based to capability-based permissions
- Support per-camera connection status
- Add enterprise configuration policies

---

**End of Phase 1 Architecture Document**
