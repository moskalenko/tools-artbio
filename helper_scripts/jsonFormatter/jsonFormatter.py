#!/usr/bin/env python
# Example usage: python jsonFormatter.py
#     -i unformatted.json
#     -o formatted.json

from argparse import ArgumentParser
import json


def indent_json(input_file, output_file, indent=4, sort_keys=False):
    with open(input_file, "r") as input:
        unformatted = input.read()
    d = json.loads(unformatted)
    with open(output_file, "w") as output:
        # output.write(json.dumps({int(x):d[x] for x in d.keys()},
        output.write(json.dumps(d,
                                indent=indent,
                                sort_keys=sort_keys))
    return


def _parse_cli_options():
    """
    Parse command line options, returning `parse_args` from `ArgumentParser`.
    """
    parser = ArgumentParser(
        description='Indent or re-indent json files',
        usage=" python %(prog)s <options>")
    parser.add_argument("-i", "--input",
                        dest="input",
                        required=True,
                        help="json file to indent")
    parser.add_argument("-o", "--output",
                        required=True,
                        dest="output",
                        help="Indented json file")
    parser.add_argument('--sort-keys', dest='sort_keys',
                        default=False, action='store_true',
                        help="Sort dictionary keys if specified")
    parser.add_argument('--indent', dest='indent', type=int,
                        default=4,
                        help="Indentation value")
    return parser.parse_args()


def __main__():
    args = _parse_cli_options()
    input = args.input
    output = args.output
    indent_json(input, output)
    print(args.sort_keys)


if __name__ == "__main__":
    __main__()
