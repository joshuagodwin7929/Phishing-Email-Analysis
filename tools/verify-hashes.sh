#!/bin/sh
# Verify every published file against SHA256SUMS. Run from the repo root.
set -e
[ -f SHA256SUMS ] || { echo "no SHA256SUMS here"; exit 1; }
sha256sum -c SHA256SUMS
