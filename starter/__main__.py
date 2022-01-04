# -*- coding: utf-8 -*-
# pylint: disable=expression-not-assigned,line-too-long,missing-module-docstring
import sys

from starter.cli import cli

if __name__ == '__main__':
    sys.exit(cli.main(argv=sys.argv[1:]))  # pragma: no cover
