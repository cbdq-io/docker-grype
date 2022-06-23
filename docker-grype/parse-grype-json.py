#!/usr/bin/env python
"""Parse the JSON output of the Anchore Grype command."""
import logging
import sys

from pygrype.parser import ParseGrypeJSON


def main():
    """Process a command line request."""
    widget = ParseGrypeJSON()
    logging.debug(f'argv {",".join(sys.argv)}')

    if len(sys.argv) > 1:
        widget.filename(sys.argv[1])

    sys.exit(widget.report())


if __name__ == '__main__':
    main()
