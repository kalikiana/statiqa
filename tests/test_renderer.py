# SPDX-FileCopyrightText: 2023 Liv Dywan <liv@twotoasts.de>
#
# SPDX-License-Identifier: EUPL-1.2

"""Tests related to processing of results and rendering"""
import unittest
from statiqa import renderer


class TestDetails(unittest.TestCase):
    """Verify format of processed results"""

    def setUp(self):
        self.renderer = renderer.Renderer("example")

    def test_details(self):
        """Verify the expected format"""
        details = self.renderer.process()
        self.assertEqual(details["results"], "example", "Expected results")
