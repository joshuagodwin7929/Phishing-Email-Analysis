#!/usr/bin/env python3
"""Defang or refang indicators read from stdin.

  echo 'http://bad.example/x user@bad.example 203.0.113.7' | python3 tools/defang.py
  echo 'hxxp://bad[.]example' | python3 tools/defang.py --refang
"""
import re
import sys

def defang(text: str) -> str:
    text = re.sub(r"(?i)\bhttp(s?)://", r"hxxp\1://", text)
    text = text.replace("@", "[@]")
    # dots inside hostnames and IPv4 addresses
    text = re.sub(r"(?<=[A-Za-z0-9])\.(?=[A-Za-z0-9])", "[.]", text)
    return text

def refang(text: str) -> str:
    text = re.sub(r"(?i)\bhxxp(s?)://", r"http\1://", text)
    return text.replace("[@]", "@").replace("[.]", ".")

if __name__ == "__main__":
    data = sys.stdin.read()
    sys.stdout.write(refang(data) if "--refang" in sys.argv else defang(data))
