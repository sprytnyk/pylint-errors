import argparse
import pathlib
import sys

from pygments import highlight
from pygments.lexers import MarkdownLexer
from pygments.formatters import TerminalFormatter


def main():
    """Get a pylint error description by an error code."""

    parser = argparse.ArgumentParser(
        description=(
            'Get a verbose description of a pylint error by an error code.'
        )
    )
    parser.add_argument(
        'code',
        metavar='code',
        type=str,
        help='A pylint error code e.g. R1710'
    )
    args = parser.parse_args()

    root = pathlib.Path(__file__).resolve().parent
    error = list(root.rglob('*{}.md'.format(args.code)))
    try:
        print(
            highlight(
                error[0].read_bytes(),
                MarkdownLexer(),
                TerminalFormatter()
            )
        )
        sys.exit(0)
    except IndexError:
        print(
            'Cannot find {} pylint error by such error code.'.format(
                args.code
            ),
            file=sys.stderr
        )
        sys.exit(1)
