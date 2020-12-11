"""CLI module."""

import argparse
import pathlib
import sys

from pygments import highlight
from pygments.lexers import MarkdownLexer
from pygments.formatters import TerminalFormatter

from plerr import __version__


def main():
    """Get a pylint error description by an error code."""

    parser = argparse.ArgumentParser(
        description=(
            'Get a verbose description of a pylint error by an error code.'
        )
    )
    parser.add_argument(
        'code',
        metavar='error code',
        type=str,
        help='a pylint error code either r1710 or R1710'
    )
    parser.add_argument(
        '-v',
        '--version',
        action='version',
        version='plerr v{}'.format(__version__)
    )
    args = parser.parse_args()

    root = pathlib.Path(__file__).resolve().parent
    try:
        error = next(root.rglob('*{}.md'.format(args.code.upper())))
        content = error.read_bytes()
        print(highlight(content, MarkdownLexer(), TerminalFormatter()))
        sys.exit(0)
    except StopIteration:
        print(
            'Cannot find {} pylint error by such error code.'.format(
                args.code
            ),
            file=sys.stderr
        )
        sys.exit(1)
