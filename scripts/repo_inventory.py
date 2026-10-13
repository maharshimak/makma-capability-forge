#!/usr/bin/env python3
"""Read-only repository inventory. Does not open or print file contents.

Usage: python scripts/repo_inventory.py /path/to/repo [--output inventory.json]
Only walks the supplied root; does not follow symbolic links. Excludes common
build/dependency directories and avoids enumerating .git internals.
"""
import argparse
import collections
import datetime
import json
import os
from pathlib import Path

EXCLUDED = {'.git', 'node_modules', '.next', '.nuxt', 'dist', 'build', '.venv', 'venv', '__pycache__', '.pytest_cache', '.mypy_cache', '.turbo', 'coverage', '.cache', 'target', '.gradle', '.idea'}
ENTRYPOINT_NAMES = {'package.json', 'pyproject.toml', 'requirements.txt', 'Cargo.toml', 'go.mod', 'pom.xml', 'build.gradle', 'next.config.ts', 'next.config.js', 'vite.config.ts', 'vite.config.js', 'Dockerfile', 'docker-compose.yml', 'compose.yaml', 'README.md', 'AGENTS.md', 'CLAUDE.md', 'SKILL.md', 'main.py', 'app.py', 'index.ts', 'index.tsx', 'page.tsx', 'Makefile'}
PRIVATE_NAME_TOKENS = ('.env', '.pem', '.key', 'credentials', 'secret', 'id_rsa', 'id_ed25519', 'token')
MAX_FILES = 150000


def is_private(filename):
    low = filename.lower()
    return any(token in low for token in PRIVATE_NAME_TOKENS)


def inventory(root):
    root = root.resolve(strict=True)
    if not root.is_dir():
        raise ValueError(f'Not a directory: {root}')
    ext_count = collections.Counter()
    dirs_count = collections.Counter()
    entries, file_count, private_omitted = [], 0, 0
    total_bytes = 0
    truncated = False
    for current, dirs, files in os.walk(root, topdown=True, followlinks=False):
        dirs[:] = sorted(d for d in dirs if d not in EXCLUDED and not Path(current, d).is_symlink())
        relative_dir = Path(current).relative_to(root)
        for name in sorted(files):
            path = Path(current, name)
            if path.is_symlink() or not path.is_file():
                continue
            if is_private(name):
                private_omitted += 1
                continue
            file_count += 1
            if file_count > MAX_FILES:
                truncated = True
                break
            try:
                size = path.stat().st_size
            except OSError:
                continue
            total_bytes += size
            ext_count[path.suffix.lower() or '[none]'] += 1
            dirs_count[str(relative_dir)] += 1
            if name in ENTRYPOINT_NAMES or '.github/workflows' in str(path.relative_to(root)).replace('\\', '/'):
                entries.append({'path': path.relative_to(root).as_posix(), 'bytes': size})
        if truncated:
            break
    return {
        'root': str(root),
        'generated_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'read_only': True,
        'content_examined': False,
        'private_names_omitted': private_omitted,
        'file_count': min(file_count, MAX_FILES),
        'total_bytes': total_bytes,
        'truncated': truncated,
        'extensions': dict(ext_count.most_common()),
        'top_directories': [{'directory': k, 'files': v} for k, v in dirs_count.most_common(30)],
        'entrypoints_and_configs': entries[:200],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('repository', type=Path)
    parser.add_argument('--output', type=Path, help='write JSON to chosen location; otherwise stdout')
    args = parser.parse_args()
    try:
        result = inventory(args.repository)
    except (OSError, ValueError) as e:
        parser.error(str(e))
    payload = json.dumps(result, indent=2, ensure_ascii=False) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload, encoding='utf-8')
        print(f'Wrote inventory to {args.output} ({result["file_count"]} files)')
    else:
        print(payload, end='')


if __name__ == '__main__':
    main()
