# SPDX-FileCopyrightText: 2023 Liv Dywan <liv@twotoasts.de>
#
# SPDX-License-Identifier: EUPL-1.2

FROM python:3.11-alpine
COPY statiqa ./statiqa
COPY pyproject.toml poetry.lock README.md .
RUN apk add --no-cache poetry && \
    poetry install --no-cache --without dev
ENTRYPOINT ["poetry", "run", "statiqa"]