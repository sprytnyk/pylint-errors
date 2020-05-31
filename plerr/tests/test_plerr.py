import pathlib
import subprocess
import unittest


class TestPlErr(unittest.TestCase):
    def test_plerr_error_getter(self):
        # Given: a command to get a description of a pylint error by an
        # error code.
        command = ['python3', '-m', 'plerr', 'R1710']

        # When: the command invokes.
        proc = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        stdout, stderr = proc.communicate()
        expected_stdout = (
            (
                pathlib.Path(__file__).resolve().parent /
                'command_output_fixture.txt'
            )
            .read_bytes()
        )

        # Then: it produces a highlighted output to stdout of the given error
        # with the exit code 0.
        assert stdout == expected_stdout
        assert not stderr
        assert proc.returncode == 0


    def test_plerr_non_existent_error(self):
        # Given: a command to get a description of a pylint error with an
        # existent error code.
        command = ['python3', '-m', 'plerr', 'R0000']

        # When: the command invokes.
        proc = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        stdout, stderr = proc.communicate()
        expected_stdout = (
            b'Cannot find R0000 pylint error by such error code.\n'
        )

        # Then: it produces an error message to stderr with the exit code 1.
        assert stderr == expected_stdout
        assert not stdout
        assert proc.returncode == 1
