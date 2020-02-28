#!/usr/bin/env python

"""Tests for the `nemo_cf.cli` package."""

from click.testing import CliRunner

from nemo_cf import cli


def test_cli_download_data_help():
    """Test the CLI."""
    runner = CliRunner()
    help_result = runner.invoke(cli.download_data, ["--help"])
    assert help_result.exit_code == 0
    assert "Download NEMO example data." in help_result.output


def test_cli_print_info_help():
    """Test the CLI."""
    runner = CliRunner()
    help_result = runner.invoke(cli.print_info, ["--help"])
    assert help_result.exit_code == 0
    assert "Print info about NEMO cf." in help_result.output
