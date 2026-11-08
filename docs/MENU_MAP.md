# Menu Map (Baseline)

Date: 2026-09-24
Scope: Baseline documentation map for menu/action ownership and audit follow-up.

## Purpose

Provide a single place to track menu items, their intended behavior, and owning module/function.

## Menu Ownership Baseline

| Menu | Intended Scope | Primary Owner File | Status |
|---|---|---|---|
| File | session/file operations | `src/myloai/ui/main_window.py` + controllers | LIKELY_DEFINED |
| Models | model lifecycle operations | `src/myloai/ui/main_window.py` + `ui/controllers/model_controller.py` | LIKELY_DEFINED |
| Agents | agent profile flows | `src/myloai/ui/main_window.py` + dialogs/managers | UNKNOWN_DETAILS |
| Plugins | plugin management flows | `src/myloai/ui/main_window.py` + `ui/controllers/plugin_controller.py` | LIKELY_DEFINED |
| Settings | endpoints/parameters/prompt management/theme/config | `src/myloai/ui/main_window.py` + dialogs + `core/config.py` | IMPLEMENTED_UNVERIFIED |
| View | panel visibility/layout | `src/myloai/ui/main_window.py` | UNKNOWN_DETAILS |
| Developer | diagnostics/request/token/log tools | `src/myloai/ui/main_window.py` | UNKNOWN_DETAILS |
| Help | app/help/about diagnostics | `src/myloai/ui/main_window.py` | UNKNOWN_DETAILS |

## CONFIRMED
- Menu construction is centralized in `src/myloai/ui/main_window.py`.
- Settings now exposes `Prompt Manager`, which opens `PromptManagerDialog` and refreshes the System Prompts dock after the dialog closes.

## LIKELY
- Some actions delegate to controller/dialog layers instead of inline logic.

## UNKNOWN
- Exact item-level duplication or ambiguous action naming between View and Developer menus.
- Runtime behavior of the Prompt Manager remains unverified until the PySide6 GUI is run interactively.

## TODO
- Add per-item rows (Action label, handler, expected behavior, current status).
- Mark every action as CONFIRMED_WORKING / UNKNOWN / NEEDS_FIX once manually verified.
