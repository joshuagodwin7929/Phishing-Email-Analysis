#!/bin/sh
# Usage: tools/newcase.sh case-002-short-name
set -e
[ -n "$1" ] || { echo "usage: $0 case-NNN-short-name"; exit 1; }
base="cases/$1"
[ ! -e "$base" ] || { echo "$base already exists"; exit 1; }
for d in raw evidence iocs attack detections report; do mkdir -p "$base/$d"; done
cp templates/case-intake.md "$base/INTAKE.md"
cp templates/iocs-template.csv "$base/iocs/iocs.csv"
cp templates/report-template.md "$base/report/report.md"
echo "Created $base"
echo "Next: copy the sample into $base/raw/, hash it, compare with the source."
