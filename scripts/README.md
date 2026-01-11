# Scripts

Utility scripts for testing and development.

## Test Scripts

### `run-tests.sh`
Runs all tests (unit + benchmark). Used by both CI and git hooks.

```bash
./scripts/run-tests.sh
```

## Git Hooks

### `install-hooks.sh`
Installs git hooks for the repository.

```bash
./scripts/install-hooks.sh
```

Currently installs:
- **pre-push**: Runs all tests before pushing to remote

### `pre-push`
The actual pre-push hook script. Automatically installed by `install-hooks.sh`.
