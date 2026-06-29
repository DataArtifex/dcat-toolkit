#!/usr/bin/env bash
set -e

# Detect if we have an active virtual environment
if [ -n "$VIRTUAL_ENV" ]; then
    # In monorepo/shared-env mode, use --active to run in the active venv
    exec uv run --active "$@"
else
    # In standalone mode, let uv run manage/create its own local environment if needed
    exec uv run "$@"
fi
