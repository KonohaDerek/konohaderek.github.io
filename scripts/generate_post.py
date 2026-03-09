import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
import sys


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))

from mask_sensitive import mask_data
from slugify import slugify
from tagger import merge_tags


def parse_date(raw_date: str | None) -> datetime:
    if not raw_date:
        return datetime.now(timezone.utc)

    raw_date = raw_date.strip()
    if len(raw_date) == 10:
        return datetime.strptime(raw_date, "%Y-%m-%d").replace(tzinfo=timezone.utc)

    return datetime.fromisoformat(raw_date.replace("Z", "+00:00"))


def yaml_quote(value: str) -> str:
    return '"' + value.replace('\\', '\\\\').replace('"', '\\"') + '"'


def render_list(items: list[str], ordered: bool = False) -> str:
    if not items:
        return ""
    lines = []
    for index, item in enumerate(items, start=1):
        prefix = f"{index}." if ordered else "-"
        lines.append(f"{prefix} {item.strip()}")
    return "\n".join(lines)


def render_references(references: list[dict]) -> str:
    if not references:
        return ""
    lines = []
    for reference in references:
        title = reference.get("title", "參考資料")
        url = reference.get("url", "")
        if url:
            lines.append(f"- [{title}]({url})")
        else:
            lines.append(f"- {title}")
    return "\n".join(lines)


def build_front_matter(data: dict, source_path: Path, published_at: datetime, tags: list[str], slug: str) -> str:
    lines = [
        "---",
        f"title: {yaml_quote(data['title'])}",
        f"date: {published_at.astimezone(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}",
        f"slug: {yaml_quote(slug)}",
    ]

    subtitle = data.get("summary")
    if subtitle:
        lines.append(f"subtitle: {yaml_quote(subtitle)}")

    lines.append("tags:")
    for tag in tags:
        lines.append(f"  - {yaml_quote(tag)}")

    lines.append(f"source: {yaml_quote(source_path.as_posix())}")
    lines.append("draft: false")
    lines.append("---")
    return "\n".join(lines)


def build_markdown(data: dict, source_path: Path) -> str:
    published_at = parse_date(data.get("date"))
    fallback_slug = published_at.strftime("post-%Y%m%d")
    slug = slugify(data.get("slug") or data["title"], fallback=fallback_slug)
    investigation_steps = data.get("investigation_steps") or []
    lessons = data.get("lessons_learned") or []
    references = data.get("references") or []

    tags = merge_tags(
        data.get("tags") or [],
        data.get("title", ""),
        data.get("summary", ""),
        data.get("background", ""),
        data.get("problem", ""),
        data.get("solution", ""),
    )

    front_matter = build_front_matter(data, source_path, published_at, tags, slug)

    sections = [
        front_matter,
        "",
        "## 背景",
        "",
        data.get("background", "").strip(),
        "",
        "## 問題",
        "",
        data.get("problem", "").strip(),
        "",
        "## 調查過程",
        "",
        render_list(investigation_steps, ordered=True),
        "",
        "## 解決方案",
        "",
        data.get("solution", "").strip(),
        "",
        "## 經驗總結",
        "",
        render_list(lessons),
    ]

    references_block = render_references(references)
    if references_block:
        sections.extend(["", "## 參考資料", "", references_block])

    return "\n".join(part for part in sections if part is not None).strip() + "\n"


def output_path(output_dir: Path, data: dict) -> Path:
    published_at = parse_date(data.get("date"))
    slug = slugify(data.get("slug") or data["title"], fallback=published_at.strftime("post-%Y%m%d"))
    return output_dir / published_at.strftime("%Y") / published_at.strftime("%m") / slug / "index.md"


def process_file(input_path: Path, output_dir: Path) -> Path:
    raw = json.loads(input_path.read_text(encoding="utf-8"))
    data = mask_data(raw)

    for required in ["title", "background", "problem", "solution"]:
        if not data.get(required):
            raise ValueError(f"{input_path.as_posix()} 缺少必要欄位: {required}")

    target = output_path(output_dir, data)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(build_markdown(data, input_path.relative_to(REPO_ROOT)), encoding="utf-8")
    return target


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate Hugo posts from curated conversation JSON files.")
    parser.add_argument("--input-dir", default="conversations")
    parser.add_argument("--output-dir", default="src/content/posts")
    args = parser.parse_args()

    input_dir = REPO_ROOT / args.input_dir
    output_dir = REPO_ROOT / args.output_dir

    if not input_dir.exists():
        raise SystemExit(f"input directory not found: {input_dir}")

    generated = []
    for input_path in sorted(input_dir.rglob("*.json")):
        generated.append(process_file(input_path, output_dir))

    if not generated:
        print("No conversation JSON files found.")
        return

    for path in generated:
        print(path.relative_to(REPO_ROOT).as_posix())


if __name__ == "__main__":
    main()