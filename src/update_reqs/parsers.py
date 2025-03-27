import argparse
from .commands import clean, check

parser = argparse.ArgumentParser(
        description="A smart CLI tool that automatically updates your requirements.txt by fetching the latest versions of outdated libraries from PyPI."
    )


parent_parser = argparse.ArgumentParser(add_help=False)
parent_parser.add_argument("--file", required=True, help="Path to requirements file")


# Subparsers
sub_parsers = parser.add_subparsers(dest="command", required=True)

#clean command parser
clean_parser = sub_parsers.add_parser("clean", parents=[parent_parser], help="Remove version numner from requirements.txt")
clean_parser.set_defaults(func=clean)

# Check command parser
check_parser = sub_parsers.add_parser("check", parents=[parent_parser], help="Check for outdated packages")
check_parser.set_defaults(func=check)
check_parser._actions[-1].required=False

