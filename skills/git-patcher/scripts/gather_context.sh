#!/usr/bin/env bash
set -e
echo "=== REPOSITORY CONTEXT ==="
echo "Branch: $(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo 'main')"
echo "Status: $(git status --short 2>/dev/null || echo 'clean')"
