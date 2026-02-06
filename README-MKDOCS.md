# ISO 9001:2015 Audit Preparation Documentation

[![MkDocs](https://img.shields.io/badge/docs-mkdocs-blue)](https://www.mkdocs.org/)
[![Material](https://img.shields.io/badge/theme-material-green)](https://squidfunk.github.io/mkdocs-material/)

Comprehensive audit preparation package for ISO 9001:2015 certification — **DDD Unit (Data Driven Development | AD/ADAS Tooling)**

---

## 📚 Documentation Structure

This MkDocs site organizes all ISO 9001:2015 audit preparation materials:

- **Getting Started**: Audit catalogue, process maps, preparation checklist
- **QMS Framework (Clauses 4-5)**: Context, stakeholders, scope, policy, RACI
- **Planning (Clause 6)**: Risks and quality objectives
- **Support (Clause 7)**: Competency and communication
- **Operations (Clause 8)**: Supplier evaluation
- **Performance (Clause 9)**: Audits and management review
- **Improvement (Clause 10)**: CAPA log

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Install MkDocs and dependencies:**

```bash
pip install mkdocs mkdocs-material mkdocs-minify-plugin
```

2. **Clone/navigate to this repository:**

```bash
cd /path/to/iso-9001
```

### Usage

#### Serve locally (with live reload)

```bash
mkdocs serve
```

Then open your browser to: **http://127.0.0.1:8000**

The site will automatically reload when you edit any markdown files.

#### Build static site

```bash
mkdocs build
```

This creates a `site/` directory with static HTML files.

#### Deploy to GitHub Pages

```bash
mkdocs gh-deploy
```

This builds and pushes the site to the `gh-pages` branch.

---

## 📂 Repository Structure

```
iso-9001/
├── mkdocs.yml                          # MkDocs configuration
├── docs/                               # Documentation source files
│   ├── index.md                        # Homepage
│   ├── getting-started/                # Audit catalogue, process map, checklist
│   ├── qms-framework/                  # Clauses 4-5 documents
│   ├── planning/                       # Clause 6 documents
│   ├── support/                        # Clause 7 documents
│   ├── operations/                     # Clause 8 documents
│   ├── performance/                    # Clause 9 documents
│   └── improvement/                    # Clause 10 documents
├── reference-documents/                # Original REF-XX files (archived)
├── diagrams/                           # Supporting diagrams
├── README.md                           # This file
└── .gitignore                          # Git ignore rules

```

---

## 🎨 Features

- **Material Theme**: Modern, responsive design with dark/light mode
- **Search**: Full-text search across all documentation
- **Mermaid Diagrams**: Embedded process flows and visualizations
- **Code Highlighting**: Syntax highlighting for code examples
- **Navigation**: Organized sidebar with expandable sections
- **Mobile Friendly**: Responsive design for all devices

---

## 📝 Editing Documentation

All documentation files are in Markdown format within the `docs/` directory:

1. Edit any `.md` file in the `docs/` folder
2. If running `mkdocs serve`, changes appear immediately in your browser
3. Commit changes to git:

```bash
git add .
git commit -m "Update documentation"
git push
```

### Adding New Pages

1. Create a new `.md` file in the appropriate `docs/` subfolder
2. Update `mkdocs.yml` to add the page to the navigation:

```yaml
nav:
  - Section Name:
    - Page Title: path/to/file.md
```

---

## 🌐 Deployment Options

### Option 1: GitHub Pages (Recommended)

1. Create a GitHub repository
2. Push this code to the repository
3. Run: `mkdocs gh-deploy`
4. Enable GitHub Pages in repository settings
5. Your site will be available at: `https://yourusername.github.io/iso-9001`

### Option 2: Other Hosting

Build the static site with `mkdocs build` and upload the `site/` directory to any web host:

- Netlify
- Vercel
- AWS S3 + CloudFront
- Azure Static Web Apps
- Self-hosted web server

---

## 🔧 Configuration

Edit `mkdocs.yml` to customize:

- **Site name and description**
- **Theme colors** (primary, accent)
- **Navigation structure**
- **Plugins** (search, minify, etc.)
- **Markdown extensions**

See [MkDocs documentation](https://www.mkdocs.org/) and [Material theme docs](https://squidfunk.github.io/mkdocs-material/) for details.

---

## 📋 Original Files

The original markdown files are preserved in:

- Root directory: `ISO-9001-Audit-Catalogue.md`, `QMS-Process-Map.md`, `Audit-Preparation-Checklist.md`
- `reference-documents/`: All `REF-XX-*.md` files

These can be kept for archival purposes or removed once you're satisfied with the MkDocs site.

---

## 🤝 Contributing

To update documentation:

1. Edit files in the `docs/` directory
2. Test locally with `mkdocs serve`
3. Commit changes with descriptive messages
4. Push to repository

---

## 📄 License

Internal documentation for DDD Unit audit preparation.

---

## 📞 Contact

- **Quality Management Representative (QMR):** _[Name]_ — _[email]_
- **Repository Maintainer:** _[Name]_ — _[email]_

---

## 🎯 Next Steps

1. **Install dependencies**: `pip install mkdocs mkdocs-material mkdocs-minify-plugin`
2. **Start local server**: `mkdocs serve`
3. **Review content**: Navigate to http://127.0.0.1:8000
4. **Customize**: Update `mkdocs.yml` with your repo URL and site URL
5. **Deploy**: Push to GitHub and run `mkdocs gh-deploy`

---

*Last updated: 2026-02-06*
