"""Tests CLI modules to provide factual coverage."""

import io
import pathlib
import sys
import unittest
from unittest.mock import patch

from plerr.cli import main

ROOT = pathlib.Path(__file__).resolve().parent


class TestPlErrModule(unittest.TestCase):
    def setUp(self):
        # Redirect stdout/stderr to mock objects to read later.
        self.stdout = patch('plerr.cli.sys.stdout', new=io.StringIO())
        self.stderr = patch('plerr.cli.sys.stderr', new=io.StringIO())
        self.stdout.start()
        self.stderr.start()

    def tearDown(self):
        self.stdout.stop()
        self.stderr.stop()

    @patch('plerr.cli.sys.argv', new=['plerr', 'r1710'])
    def test_plerr_error_getter_with_lower_case_letter(self):
        # Given: a command to get a description of a pylint error by an
        # error code with a lower case letter.

        # When: the command invokes.
        with self.assertRaises(SystemExit) as err:
            main()
        expected_stdout = (ROOT / 'command_output_fixture.txt').read_bytes()

        # Then: it produces a highlighted output to stdout of the given error
        # with the exit code 0.
        assert sys.stdout.getvalue().encode() == expected_stdout
        assert not sys.stderr.getvalue().encode()
        assert err.exception.code == 0

    @patch('plerr.cli.sys.argv', new=['plerr', 'R1710'])
    def test_plerr_error_getter_with_capital_letter(self):
        # Given: a command to get a description of a pylint error by an
        # error code with a capital letter.

        # When: the command invokes.
        with self.assertRaises(SystemExit) as err:
            main()
        expected_stdout = (ROOT / 'command_output_fixture.txt').read_bytes()

        # Then: it produces a highlighted output to stdout of the given error
        # with the exit code 0.
        assert sys.stdout.getvalue().encode() == expected_stdout
        assert not sys.stderr.getvalue().encode()
        assert err.exception.code == 0

    @patch('plerr.cli.sys.argv', new=['plerr', 'R0000'])
    def test_plerr_non_existent_error(self):
        # Given: a command to get a description of a pylint error with a
        # non-existent error code.

        # When: the command invokes.
        with self.assertRaises(SystemExit) as err:
            main()
        expected_stderr = (
            b'Cannot find R0000 pylint error by such error code.\n'
        )

        # Then: it produces an error message to stderr with the exit code 1.
        assert sys.stderr.getvalue().encode() == expected_stderr
        assert not sys.stdout.getvalue().encode()
        assert err.exception.code == 1
