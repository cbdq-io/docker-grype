#!/usr/bin/env python
"""Parse the JSON output of the Anchore Grype command."""
import logging
import sys

from pygrype.params import Params
from pygrype.parser import ParseGrypeJSON


def main(filename: str = None) -> int:
    """
    Process a command line request.

    Parameters
    ----------
    filename : str,optional
        The name of the JSON file to be parsed.

    Returns
    -------
    int
        The return code from ParseGrypeJSON.report().
    """
    params = Params()

    logging.basicConfig(
        format='%(levelname)s:%(message)s',
        level=params.log_level)

    widget = ParseGrypeJSON(params)
    logging.debug(f'argv {",".join(sys.argv)}')

    if len(filename) > 1:
        widget.filename(filename)

    return widget.report()


if __name__ == '__main__':
    sys.exit(main())
