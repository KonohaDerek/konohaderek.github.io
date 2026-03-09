import re
from typing import Any


PATTERNS = [
    (re.compile(r"ghp_[A-Za-z0-9_]+"), "ghp_********"),
    (re.compile(r"github_pat_[A-Za-z0-9_]+"), "github_pat_********"),
    (re.compile(r"Bearer\s+[A-Za-z0-9._-]+", re.IGNORECASE), "Bearer ********"),
    (re.compile(r"\b\d{1,3}(?:\.\d{1,3}){3}\b"), "10.x.x.x"),
    (re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"), "user@example.com"),
    (re.compile(r"(?i)(password|secret|token)\s*[:=]\s*['\"]?[^'\"\s]+['\"]?"), r"\1=********"),
]


def mask_text(value: str) -> str:
    masked = value
    for pattern, replacement in PATTERNS:
        masked = pattern.sub(replacement, masked)
    return masked


def mask_data(data: Any) -> Any:
    if isinstance(data, str):
        return mask_text(data)
    if isinstance(data, list):
        return [mask_data(item) for item in data]
    if isinstance(data, dict):
        return {key: mask_data(value) for key, value in data.items()}
    return data