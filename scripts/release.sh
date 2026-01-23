#!/bin/sh

set -e

git switch main
$EDITOR ../CHANGELOG.md
git add ../CHANGELOG.md
uv version "$1"
git add ../pyproject.toml
git add ../uv.lock
git commit -m "release $1"
git push
git tag "$1" -m "$1"
git push origin "$1"
