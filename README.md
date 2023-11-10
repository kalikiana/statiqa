<!--
SPDX-FileCopyrightText: 2023 Liv Dywan <liv@twotoasts.de>

SPDX-License-Identifier: EUPL-1.2
-->

## statiqa

![GitHub Actions](https://github.com/kalikiana/statiqa/actions/workflows/test.yaml/badge.svg)
![GitHub Actions](https://github.com/kalikiana/statiqa/actions/workflows/container.yaml/badge.svg)

### What's this project about?

Render the results of your [openQA](https://open.qa) tests directly in your CI. No need to have access to a full web UI. This is also handy to backup just the results without keeping all of the original data around.

### How do I build and run this?

The quickest way to run statiqa is via the container:

```bash
podman run -it --rm -v $(pwd):/w -w /w ghcr.io/kalikiana/statiqa/min:latest
```

For a typical development setup the necessary dependencies can be installed via [poetry](https://python-poetry.org):

```bash
poetry install
poetry run pytest -v