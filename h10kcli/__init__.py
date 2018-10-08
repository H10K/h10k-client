#!/usr/bin/env python
"""__init__.py: CLI entry point for H10K Client."""
import argparse
import json
import os
import pprint
import requests
import sys
import yaml

from h10kparser import ParseConfig
from version import __version__


def show_response_error(response):
    """Show the error message from the requests call."""
    print "ERROR: Response code = %d" % response.status_code

    try:
        print response.json()
    except ValueError:
        print response.text

    if response.status_code < 0:
        status = response.status_code * (-1)
    else:
        status = response.status_code

    sys.exit(response.status_code)


def main():
    """Parse the command line arguments and process the request."""
    parser = argparse.ArgumentParser(description='H10K Client')

    # Required arguments.
    parser.add_argument('action',
                        choices=[
                            'create',
                            'delete',
                            'lint',
                            'status'
                        ])

    # Optional arguments.
    parser.add_argument("-V", "--version", version=__version__,
                        help="Print the version and exit.", action="version")
    parser.add_argument("-f", "--configfile", default='h10k.yml',
                        help="Config file for H10K (default: h10k.yml).")
    parser.add_argument("-t", "--token",
                        help="API token.")
    parser.add_argument("-w", "--wapi", default="https://api.h10k.io/v1",
                        help="Web API endpoint (for development only).")
    args = parser.parse_args()

    if args.action == 'lint':
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

    if h10k_config.status() > 0 or lint_only:
        sys.exit(h10k_config.status())

    if "H10K_API_TOKEN" in os.environ:
        apitoken = os.environ['H10K_API_TOKEN']
    elif args.token is not None:
        apitoken = args.token
    else:
        sys.stderr.write("You must specify an API token.\n")
        sys.exit(1)

    url = args.wapi
    data = h10k_config.data()
    headers = {'Authorization': 'Token %s' % apitoken}

    try:
        if args.action == 'create':
            response = requests.post('%s/create' % url, data=json.dumps(data),
                                     headers=headers)
        elif args.action == 'delete':
            response = requests.delete('%s/delete' % url,
                                       data=json.dumps(data),
                                       headers=headers)
        elif args.action == 'status':
            response = requests.get('%s/status' % url, data=json.dumps(data),
                                    headers=headers)
    except Exception as err:
        print("Exception error: {0}".format(err))
        sys.exit(2)

    if args.action == 'create' and response.status_code != 204:
        show_response_error(response)
    elif args.action == 'delete' and response.status_code != 204:
        show_response_error(response)
    elif args.action == 'status' and response.status_code != 200:
        show_response_error(response)


if __name__ == "__main__":
    main()
