# SPDX-FileCopyrightText: 2023 Liv Dywan <liv@twotoasts.de>
#
# SPDX-License-Identifier: EUPL-1.2

"""Rendering of results to consumable formats"""


class Renderer:
    """Serialize and format unprocessed results"""

    results: str

    def __init__(self, results: str):
        self.results = results

    def process(self) -> {}:
        """Process results and return details"""
        details = {"results": self.results}
        return details

    def output(self) -> None:
        """ "Output details to stdout"""
        print(f"Let's process {self.results}, shall we?")
        print(self.process())
