#!/bin/bash
set -e

# You must have read access to this repo because of already set up git creds or keys.
REPO="https://github.com/dashlers/app-lab"
SUBDIR="monitoring_stack"

# Setup unique temp dir and auto-cleanup
DIR=$(mktemp -d)
trap 'rm -rf "$DIR"' EXIT

# Execute workflow
git clone "$REPO" "$DIR"
cd "$DIR/$SUBDIR"
docker compose up -d
