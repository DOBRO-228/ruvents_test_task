#!/usr/bin/env python3

""""""

import argparse


def main():
    """CLI command."""
    parser = argparse.ArgumentParser(
        usage='calculate <filepath>',
        description='Do some calculations.',
        argument_default=argparse.SUPPRESS,
        add_help=False,
    )
    parser.add_argument(
        'first_file',
        help=argparse.SUPPRESS,
    )
    return 1


if __name__ == '__main__':
    main()
