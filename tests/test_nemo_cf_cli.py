#!/usr/bin/env python

"""Tests for the `nemo_cf.cli` package."""

from click.testing import CliRunner

from nemo_cf import cli


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert 'Download NEMO example data.' in help_result.output
