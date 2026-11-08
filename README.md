# MyLoAI Control Center

MyLoAI Control Center is a PySide6 desktop control center for local Ollama and remote/provider-compatible LLM backends.

## Repository layout

`src/` is the Python source-layout boundary. The application package lives at `src/myloai/` and is imported as `myloai`.

`tests/`, `packaging/`, and `docs/` contain the active test, release, and documentation surfaces.

The former `GR00T-User-706/locallama-gui` repository is the historical archive. The active repository is `GR00T-User-706/myloai`.

## Development entry point

`python -m myloai`

## Installed command

`myloai`

See [docs/BUILDING.md](docs/BUILDING.md) for production packaging and [docs/MIGRATION_STATUS.md](docs/MIGRATION_STATUS.md) for the current migration state.
