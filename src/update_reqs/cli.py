import os, sys, argparse
from pathlib import Path
from .helpers import _file_exists_
from .parsers import parser as PARSER

def main():
    args = PARSER.parse_args()
    file_path = None
    
    if args.file:
        file_path = Path(args.file).resolve()
        file_exists = _file_exists_(file_path)

        if not file_exists:
            print(f" Error: {file_path} does not exist.")
            sys.exit(1)

    args.func(file_path)


if __name__ == "__main__":
    main()