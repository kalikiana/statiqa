# SPDX-FileCopyrightText: 2023 Liv Dywan <liv@twotoasts.de>
#
# SPDX-License-Identifier: EUPL-1.2

"""Processing of command-line interactions"""
import argparse
from . import renderer


class CLI:
    """Parse arguments given on the CLI"""

    args: argparse.ArgumentParser

    def __init__(self):
        self.parse()

    def parse(self, args=None) -> None:
        """Setup up parsing with optional input override"""
        parser = argparse.ArgumentParser(description="Render openQA results")
        parser.add_argument("results", type=str, help='results or "pool"')
        self.args = parser.parse_args(args)

    def run(self) -> None:
        """Provide a main entry point"""
        return renderer.Renderer(self.args.results).process()
