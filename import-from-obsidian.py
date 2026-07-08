import sys
import frontmatter
import re
from pathlib import Path
import shutil
from PIL import Image
from datetime import datetime, date
import fnmatch
import unicodedata

"""
Imports markdown files from Obsidian notebook to Hugo-based website.

- Cleans up target directories before import (removing all files)
- Exports Markdown files from specified Obsidian directories, given that `publish` is set to true
- Cleans up frontmatter (allowing only specified keys, ensuring required fields)
- Removes comments from content (%% ... %%)
- Collects and copies linked images to a static directory
- Sets new filename (and thus URL) based on the "title" frontmatter property
"""

# Define directories
WEBSITE_ROOT  = Path("~/Repositories/Website").expanduser()

if sys.platform.startswith("linux"):
    OBSIDIAN_ROOT = Path("~/Repositories/Notebook").expanduser()
else:
    OBSIDIAN_ROOT = Path("~/Obsidian/Notebook").expanduser()

CONTENT_DIR = WEBSITE_ROOT / "content"

ATTACHMENTS_SOURCE_DIR = OBSIDIAN_ROOT / "+" / "media"
ATTACHMENTS_TARGET_DIR = WEBSITE_ROOT / "static" / "attachments"

# Define content to be imported
SOURCES = [
    {
        # PORTFOLIO
        "publish": True,
        "source_dirs": [ OBSIDIAN_ROOT / "projects" / "portfolio" ],
        "target_dir": CONTENT_DIR / "portfolio",
        "include_subdirs": True,
    },
    {
        # NOTES
        "publish": True,
        "source_dirs": [ OBSIDIAN_ROOT / "w" ],
        "target_dir": CONTENT_DIR / "notebook",
        "include_subdirs": False,
    },
    {
        # FRESH FINDS
        "publish": True,
        "source_dirs": [ OBSIDIAN_ROOT / "gallery", OBSIDIAN_ROOT / "library" ],
        "target_dir": CONTENT_DIR / "finds",
        "include_subdirs": False,
    },
]

# Define frontmatter properties/keys that should be imported; rest will be removed
ALLOWED_KEYS = { "publish", "title", "description", "feature-image", "thumb-image", "project-type", 
                 "anchors", "created", "last updated", "captured", "year", "date", "opened", "closed", "image", "images", }

# Define media link patterns for handling attached media files
IMAGE_LINK_PATTERN = re.compile(r'\[\[(.+?\.(?:webp|jpg|jpeg|png|svg))\]\]', re.IGNORECASE)
VIDEO_LINK_PATTERN = re.compile(r'\[\[(.+?\.(?:webm|mp4|gif))\]\]', re.IGNORECASE)
PDF_LINK_PATTERN = re.compile(r'\[\[(.+?\.(?:pdf))\]\]', re.IGNORECASE)



def clean_target_dir(target_dir: Path, preserve_patterns):
    """
    Delete all files and folders in target_dir except those matching preserve_patterns.
    Patterns can be:
      - "_index.md"
      - "subfolder/*"
    """
    for item in target_dir.rglob("*"):
        rel_path = item.relative_to(target_dir).as_posix()

        # If path is protected through preserve_patterns
        if any(fnmatch.fnmatch(rel_path, pattern) for pattern in preserve_patterns):
            continue

        # Delete
        if item.is_file():
            item.unlink()
        elif item.is_dir():
            shutil.rmtree(item, ignore_errors=True)



def clean_attachments_dir():
    """
    Delete all files and folders in attachments dir.
    """
    for item in ATTACHMENTS_TARGET_DIR.glob("*"):
        if item.is_file():
            item.unlink()
        elif item.is_dir():
            shutil.rmtree(item)



def collect_md_files(source_dir: Path):
    """Collect all markdown files recursively from given source directory."""
    return list(source_dir.rglob("*.md"))



def collect_attachment_filenames(frontmatter_data, content):
    """Extract all attachment filenames from content and frontmatter."""
    filenames = set()

    def add_from_text(text):
        if not text:
            return
        for match in re.finditer(r'!\[\[([^\]]+)\]\]|\[\[([^\]]+)\]\]', text):
            ref = match.group(1) or match.group(2)
            if not ref:
                continue
            if re.search(r'\.(?:webp|jpg|jpeg|png|svg|webm|mp4|gif|pdf)$', ref, re.IGNORECASE):
                filenames.add(ref)

    def add_from_value(value):
        if isinstance(value, (list, tuple)):
            for item in value:
                add_from_value(item)
            return

        if isinstance(value, dict):
            for item in value.values():
                add_from_value(item)
            return

        if isinstance(value, str):
            add_from_text(value)

    # From content
    add_from_text(content)

    # From frontmatter
    for property in frontmatter_data:
        add_from_value(frontmatter_data[property])

    return filenames



def find_and_copy_attachments(filenames):
    """Find and copy images from source to target dir."""
    for filename in filenames:
        # Recursively look through attachments folder to find file
        found = None
        for source_path in ATTACHMENTS_SOURCE_DIR.rglob("*"):
            if source_path.name.lower() == filename.lower():
                found = source_path
                break

        if not found:
            print(f"⚠ File not found: {filename}")
            continue
    
        extension = source_path.suffix.lower()

        # --- Images ---
        if extension in [".jpg", ".jpeg", ".png", ".svg", ".webp"]:
            target_path = ATTACHMENTS_TARGET_DIR / f"{source_path.stem}.webp"

            if extension != ".webp":
                try:
                    img = Image.open(source_path)
                    img.save(target_path, "webp")
                    print(f"→ Image converted & imported: {source_path.name} → {target_path.name}")
                except Exception as e:
                    print(f"Error converting image {source_path}: {e}")
            else:
                shutil.copy2(source_path, target_path)
                print(f"→ Image imported: {filename}")

        # --- Videos ---
        elif extension in [".mp4", ".gif", ".webm"]:
            target_path = ATTACHMENTS_TARGET_DIR / f"{source_path.stem}.webm"

            if extension == ".webm":
                shutil.copy2(source_path, target_path)
                print(f"→ Video imported: {filename}")
            else:
                # TODO: needs ffmpeg for real conversion
                print(f"⚠ Skipping video conversion (requires ffmpeg): {source_path.name}")
        
        # --- PDFs ---
        elif extension == ".pdf":
            target_path = ATTACHMENTS_TARGET_DIR / f"{source_path.name}"
            shutil.copy2(source_path, target_path)
            print(f"→ PDF imported: {filename}")



def strip_comments(text: str) -> str:
    """Remove Obsidian-style comments from content."""
    return re.sub(r"%%.*?%%", "", text, flags=re.DOTALL)


def prepare_content(text: str) -> str:
    """Prepare & clean up content."""
    text = strip_comments(text)

    # Convert attachment links (ensure WebP/WebM)
    def replace_image(match):
        filename = Path(match.group(1))
        new_filename = f"{filename.stem}.webp"
        return f"[[{new_filename}]]"

    def replace_video(match):
        filename = Path(match.group(1))
        new_filename = f"{filename.stem}.webm"
        return f"[[{new_filename}]]"

    text = re.sub(IMAGE_LINK_PATTERN, replace_image, text)
    text = re.sub(VIDEO_LINK_PATTERN, replace_video, text)

    return text



def prepare_frontmatter(post: frontmatter.Post, filepath: Path) -> frontmatter.Post:
    """Prepare & clean up frontmatter."""
    # Keep only allowed frontmatter keys
    keys_to_remove = set(post.metadata.keys()) - ALLOWED_KEYS
    for key in keys_to_remove:
        del post.metadata[key]

    # Ensure minimum required frontmatter fields exist
    if "title" not in post.metadata:
        post.metadata["title"] = filepath.stem
    if "publish" not in post.metadata:
        post.metadata["publish"] = False

    # Convert attachment links
    relative_attach_dir = ATTACHMENTS_TARGET_DIR.relative_to(WEBSITE_ROOT / "static")

    def normalize_value(value):
        if isinstance(value, (list, tuple)):
            return [normalize_value(item) for item in value]

        if not isinstance(value, str):
            return value

        raw_str = value
        if raw_str.startswith("/"):
            return raw_str

        def replace_reference(match):
            filename = Path(match.group(1))
            ext = filename.suffix.lower()

            if ext in [".jpg", ".jpeg", ".png", ".svg", ".webp"]:
                new_name = f"{filename.stem}.webp"
            elif ext in [".mp4", ".gif", ".webm"]:
                new_name = f"{filename.stem}.webm"
            elif ext == ".pdf":
                new_name = filename.name
            else:
                new_name = filename.name

            return "/" + (relative_attach_dir / new_name).as_posix()

        updated = re.sub(IMAGE_LINK_PATTERN, replace_reference, raw_str)
        updated = re.sub(VIDEO_LINK_PATTERN, replace_reference, updated)
        updated = re.sub(PDF_LINK_PATTERN, replace_reference, updated)
        return updated

    for property in list(post.metadata.keys()):
        post.metadata[property] = normalize_value(post.metadata[property])

    return post


def parse_captured_date(value):
    """Parse a captured date from frontmatter into a datetime object."""
    if isinstance(value, datetime):
        return value
    if isinstance(value, date):
        return datetime.combine(value, datetime.min.time())
    if not isinstance(value, str):
        return None

    text = value.strip()
    if not text:
        return None

    for fmt in (
        "%Y-%m-%d",
        "%Y-%m-%d %H:%M",
        "%Y-%m-%d %H:%M:%S",
        "%Y/%m/%d",
        "%Y/%m/%d %H:%M",
        "%Y/%m/%d %H:%M:%S",
    ):
        try:
            return datetime.strptime(text, fmt)
        except ValueError:
            continue

    try:
        return datetime.fromisoformat(text.replace("Z", "+00:00"))
    except ValueError:
        return None


def apply_content_indices(group, imported_files):
    """Add a year-based index prefix to the content of imported finds notes."""
    if group["target_dir"].name != "finds":
        return

    items = []
    for path in imported_files:
        post = frontmatter.load(path)
        captured = parse_captured_date(post.metadata.get("captured"))
        if captured:
            items.append((captured, path))

    items.sort(key=lambda item: (item[0].year, item[0].month, item[0].day, item[0].hour, item[0].minute, item[0].second, str(item[1])))

    counts_by_year = {}
    for captured, path in items:
        year = captured.year
        count = counts_by_year.get(year, 0) + 1
        counts_by_year[year] = count
        prefix = f"[{str(year)[-2:]}.{count}]"

        post = frontmatter.load(path)
        content = (post.content or "").lstrip()
        content = re.sub(r"^\[[0-9]{1,4}\.\d+\]\s*", "", content, count=1)
        post.content = f"{prefix} {content}" if content else prefix

        with open(path, "w", encoding="utf-8") as f:
            f.write(frontmatter.dumps(post))


def import_notes():
    # Check & clean target image attachments directory
    ATTACHMENTS_TARGET_DIR.mkdir(parents=True, exist_ok=True)
    clean_attachments_dir()
    print(f"Cleaned target attachments directory: {ATTACHMENTS_TARGET_DIR}")

    for group in SOURCES:
        dst_root = group["target_dir"]
        if group["publish"]:
            dst_root.mkdir(parents=True, exist_ok=True)
            clean_target_dir(dst_root, ["_index.md"])
            print(f"Cleaned target content directory: {dst_root}")

            imported_files = []
            for src in group["source_dirs"]:
                for file in collect_md_files(src):

                    post = frontmatter.load(file)

                    if post.metadata.get("publish", False):
                        # Collect attachments from content with comments removed, but before changing filenames.
                        attachment_filenames = collect_attachment_filenames(post.metadata, strip_comments(post.content))
                        find_and_copy_attachments(attachment_filenames)

                        # Remove comments and normalize content links for the exported note.
                        post.content = prepare_content(post.content)
                        # Filter properties & convert links
                        post = prepare_frontmatter(post, file)

                        # Generate new file names from "title" property
                        safe_title = post.metadata["title"].strip().lower()
                        safe_title = unicodedata.normalize("NFKD", safe_title)
                        safe_title = safe_title.replace(" ", "-")
                        safe_title = re.sub(r"[^\w\-]", "", safe_title)
                        target_file = dst_root / f"{safe_title}.md"

                        # Set target file path based on whether subdirectories are included
                        rel_path = file.relative_to(src)

                        if group["include_subdirs"]:
                            rel_path = file.relative_to(src)
                            target_file = dst_root / rel_path.parent / f"{safe_title}.md"
                        else:
                            target_file = dst_root / f"{safe_title}.md"

                        target_file.parent.mkdir(parents=True, exist_ok=True)

                        with open(target_file, "w", encoding="utf-8") as f:
                            f.write(frontmatter.dumps(post))

                        imported_files.append(target_file)
                        print(f"Imported: {file.relative_to(OBSIDIAN_ROOT)} → {target_file.relative_to(CONTENT_DIR)}")
                    else:
                        print(f"Skipped (publish: false): {file.relative_to(OBSIDIAN_ROOT)}")

            apply_content_indices(group, imported_files)


if __name__ == "__main__":
    import_notes()
