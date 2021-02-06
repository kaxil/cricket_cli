#!/usr/bin/env python

"""Tests for `cricket_cli` package."""


import unittest
from typer.testing import CliRunner

from cricket_cli import live_score
from cricket_cli import cli


class TestCricketCli(unittest.TestCase):
    """Tests for `cricket_cli` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.app)
        assert result.exit_code == 0
        assert "cricket_cli.cli.main" in result.output
        help_result = runner.invoke(cli.app, ["--help"])
        assert help_result.exit_code == 0
        assert "Show this message and exit." in help_result.output
