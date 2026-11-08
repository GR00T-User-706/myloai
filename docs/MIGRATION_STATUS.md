# MyLoAI Migration Status

## Current state

The active repository is **GR00T-User-706/myloai**. The former **GR00T-User-706/locallama-gui** repository is the historical archive and is not the active development target.

The intentional source-tree break changed the application from:

```text
locallama_gui/
    ...
```

to the conventional Python source layout:

```text
repo-root/
└── src/
    └── myloai/
        ├── __init__.py
        ├── __main__.py
        ├── app.py
        ├── backends/
        ├── core/
        ├── plugins/
        └── ui/
```

The repository root is **not** intended to become `myloai/myloai/`. The outer directory is the repository checkout; `src/` is the source-layout boundary; `myloai/` is the actual Python package namespace.

## Intentional breaking contract

The former `locallama_gui` namespace and `locallama-gui` source-path contract are no longer compatibility targets.

The migration intentionally breaks:

- Python imports using `locallama_gui.*`
- `python -m locallama_gui`
- package discovery for `locallama_gui`
- the legacy `locallama-gui` console entry point
- source-tree paths rooted at `locallama_gui/`
- build scripts that assume the old repository name or source directory

The canonical Python namespace is now `myloai`.

The canonical development entry point is:

```bash
python -m myloai
```

The canonical installed command is:

```text
myloai
```

## Repairs completed in this pass

- Moved the Python source package from `src/*` to `src/myloai/*`.
- Updated active Python imports and test imports from `locallama_gui` to `myloai`.
- Updated setuptools discovery to search `src/` for `myloai*`.
- Removed the legacy `locallama-gui` console-script entry point.
- Updated PyInstaller to discover and freeze `src/myloai/`.
- Corrected the PyInstaller repository-root calculation.
- Updated the Linux, Windows, and macOS packaging workflow to stop invoking the obsolete icon generator.
- Updated Linux repository/archive URLs to the active repository.
- Updated development launcher installation to install `myloai` instead of `run-locallama`.
- Updated desktop-entry installation to use the canonical `myloai.desktop`.
- Moved the brand-board reference to `docs/branding/myloai-brand-board.png`.
- Assigned canonical names to the seven MyLoAI artwork assets.
- Made the main window own its canonical `MyLoAI Control Center` title instead of applying that title later through `production_fixes.py`.
- Synchronized runtime package version metadata with `2.0.0`.
- Changed the runtime application identity and log filename to MyLoAI.

## Known remaining migration debt

This pass deliberately did **not** perform the entire documentation and legacy-artifact purge.

Remaining work includes:

1. Rewrite current documentation that still describes `locallama_gui` as the active package.
2. Audit and update `MIGRATION_MANIFEST.md`, which describes the previous compatibility strategy.
3. Remove the obsolete generated-icon utility after all build references are gone.
4. Remove obsolete generated SVG/icon artifacts after packaging has been verified against the canonical PNG assets.
5. Remove or rewrite stale historical compatibility language in current project documents.
6. Audit platform-specific installer icon handling, especially Windows/Inno Setup, because the supplied canonical artwork is PNG while Inno Setup's setup-icon mechanism expects an ICO.
7. Run the full Python import, compile, lint, test, and packaging verification suite from a clean checkout.

## Compatibility policy for this reset

This development reset does **not** preserve old per-user configuration/data locations as a migration requirement. The application is currently treated as a controlled development project with no meaningful external user base. Compatibility can be reconsidered later if the distribution model changes.
