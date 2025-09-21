from __future__ import annotations
import re
from typing import List, Tuple

FINDINGS = [
    (r"aws_secret_access_key\s*[:=]\s*['\"]([A-Za-z0-9/+=]{40})['\"]", "Possible AWS secret key", "high"),
    (r"(?i)api[_-]?key\s*[:=]\s*['\"][A-Za-z0-9_-]{16,}['\"]", "Possible API key", "high"),
    (r"(?i)password\s*[:=]\s*['\"][^'\"]+['\"]", "Hardcoded password", "high"),
    (r"(?i)token\s*[:=]\s*['\"][A-Za-z0-9._-]{16,}['\"]", "Hardcoded token", "medium"),
    (r"(?i)(todo|fixme)\b:?.*", "TODO/FIXME left in code", "low"),
]

def scan_text(name: str, text: str) -> List[Tuple[str, int, str, str, str]]:
    results: List[Tuple[str, int, str, str, str]] = []
    lines = text.splitlines()
    for i, line in enumerate(lines, start=1):
        for pattern, desc, sev in FINDINGS:
            if re.search(pattern, line):
                results.append((name, i, desc, sev, line.strip()))
    return results
