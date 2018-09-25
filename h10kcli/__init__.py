#!/usr/bin/env python
"""__init__.py: CLI entry point for H10K Client."""
import argparse
import sys
import yaml

from h10kparser import ParseConfig
from version import __version__


def main():
    """Parse the command line arguments and process the request."""
    parser = argparse.ArgumentParser('H10K Client')
    actions = parser.add_mutually_exclusive_group(required=True)
    parser.add_argument("-V", "--version", version=__version__,
                        help="Print the version and exit.", action="version")
    actions.add_argument("-c", "--create", action="store_true",
                         help="Create a cluster.")
    actions.add_argument("-d", "--delete", action="store_true",
                         help="Delete a cluster.")
    parser.add_argument("-f", "--configfile", default='h10k.yml',
                        help="Config file for H10K (default: h10k.yml)")
    actions.add_argument("-l",
                         "--lint", help="Check the H10K file format only.",
                         action="store_true")
    actions.add_argument("-s", "--status", action="store_true",
                         help="Get the status a cluster.")
    args = parser.parse_args()

    if args.lint:
        lint_only = True
    else:
        lint_only = False

    try:
        stream = file(args.configfile, 'r')
    except IOError as err:
        print("IO error: {0}".format(err))
        sys.exit(err.errno)

    dict = yaml.load(stream)
    h10k_config = ParseConfig(dict, args.configfile)


if __name__ == "__main__":
    main()
