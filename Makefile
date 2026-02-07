.PHONY: setup serve build clean help

VENV := .venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip
MKDOCS := $(VENV)/bin/mkdocs
HOST := 0.0.0.0
PORT := 8000

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

setup: $(VENV) ## Install Python venv and all MkDocs dependencies
$(VENV):
	python3 -m venv $(VENV)
	$(PIP) install --quiet --upgrade pip
	$(PIP) install --quiet \
		mkdocs-material \
		mkdocs-minify-plugin \
		mkdocs-static-i18n

serve: setup ## Serve docs locally with live-reload (0.0.0.0:8000)
	$(MKDOCS) serve --dev-addr $(HOST):$(PORT)

build: setup ## Build static site into site/
	$(MKDOCS) build --clean

clean: ## Remove venv and build artifacts
	rm -rf $(VENV) site/
