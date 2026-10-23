#!/usr/bin/env python3
"""Prepara o conteúdo do catálogo para publicação via Quartz.

- Copia *.md do repo para o diretório de destino (quartz/content), preservando subpastas.
- Remove a seção '## Comentários' (anotações pessoais — ficam só no vault).
- _index.md vira index.md (home do site); _template.md é excluído.
"""
import re
import shutil
import sys
from pathlib import Path

SKIP_FILES = {"_template.md"}
RENAME = {"_index.md": "index.md"}
SKIP_DIRS = {".git", ".github", "node_modules", "quartz"}

# '## Comentários' até o próximo heading '## ' ou fim do arquivo
COMENTARIOS_RE = re.compile(r"^## Comentários\s*\n.*?(?=^## |\Z)", re.MULTILINE | re.DOTALL)


def main() -> None:
    if len(sys.argv) < 2:
        print("uso: prepare_content.py <dir_destino>", file=sys.stderr)
        sys.exit(1)
    root = Path(__file__).resolve().parent.parent
    dest = Path(sys.argv[1]).resolve()
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)

    count = 0
    for src in sorted(root.rglob("*.md")):
        rel_dirs = [p for p in src.relative_to(root).parts[:-1]]
        if any(d in SKIP_DIRS or d.startswith(".") for d in rel_dirs):
            continue
        if src.name in SKIP_FILES:
            continue
        text = src.read_text(encoding="utf-8")
        text = COMENTARIOS_RE.sub("", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        out_name = RENAME.get(src.name, src.name)
        out = dest / Path(*rel_dirs) / out_name if rel_dirs else dest / out_name
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text.rstrip() + "\n", encoding="utf-8")
        count += 1
    print(f"{count} notas publicadas em {dest} (seção Comentários removida)")


if __name__ == "__main__":
    main()
