from typing import Iterable, List


KEYWORDS = {
    "Docker": ["docker", "ghcr", "container", "compose"],
    "GitHub": ["github", "actions", "ghcr"],
    "Kubernetes": ["kubernetes", "k8s", "helm"],
    "DevOps": ["devops", "pipeline", "deployment", "ci/cd"],
    "Troubleshooting": ["error", "failed", "fix", "troubleshooting", "異常", "錯誤"],
    "API": ["api", "rest", "graphql"],
    "Database": ["database", "sql", "mysql", "postgres", "mongodb"],
    "Linux": ["linux", "ubuntu", "debian", "alpine", "bash"],
}


def merge_tags(explicit_tags: Iterable[str], *content_blocks: str) -> List[str]:
    merged = []
    seen = set()

    for tag in explicit_tags or []:
        if tag and tag not in seen:
            merged.append(tag)
            seen.add(tag)

    haystack = "\n".join(block for block in content_blocks if block).lower()

    for tag, keywords in KEYWORDS.items():
        if tag in seen:
            continue
        if any(keyword.lower() in haystack for keyword in keywords):
            merged.append(tag)
            seen.add(tag)

    if "技術筆記" not in seen:
        merged.insert(0, "技術筆記")

    return merged[:6]