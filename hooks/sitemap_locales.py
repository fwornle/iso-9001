"""Replicate root sitemap.xml into locale directories after build.

mkdocs-static-i18n only generates a single root sitemap.xml, but
mkdocs-material's JS expects a per-locale sitemap (e.g. de/sitemap.xml).
"""

import shutil
from pathlib import Path


def on_post_build(config, **kwargs):
    site_dir = Path(config["site_dir"])
    root_sitemap = site_dir / "sitemap.xml"
    if not root_sitemap.exists():
        return

    for child in site_dir.iterdir():
        if child.is_dir() and (child / "index.html").exists():
            dest = child / "sitemap.xml"
            if not dest.exists():
                shutil.copy2(root_sitemap, dest)
