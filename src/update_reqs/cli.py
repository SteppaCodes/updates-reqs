import re, os, sys, argparse
from pathlib import Path

def clean(file_path):
    """
        Function to remove all version number from requirements and write file back
    """
    with open(file_path, "r") as file:
        lines = file.readlines()
    
    # Split the text at any of the specified characters <>=
    # Returns a list of two values ["library", "version"]
    cleaned_lines = [re.split(r"[<>=]+", line.strip())[0] for line in lines]

    with open(file_path, "w") as file:
        file.write("\n".join(cleaned_lines) + "\n")

    print("Requirements Cleaned Successfully")
    

def main():
    parser = argparse.ArgumentParser(
        description="A smart CLI tool that automatically updates your requirements.txt by fetching the latest versions of outdated libraries from PyPI."
    )

    # Parent parser for global commands
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument("--file", required=True, help="Path to requirements file")

    sub_parsers = parser.add_subparsers(dest="command", required=True)

    # Clean command
    clean_parser = sub_parsers.add_parser("clean", parents=[parent_parser], help="Remove version numner from requirements.txt")
    clean_parser.set_defaults(func=clean)

    args = parser.parse_args()

    file_path = Path(args.file).resolve()
    if not os.path.exists(file_path):
        print(f" Error: {file_path} does not exist.")
        sys.exit(1)

    args.func(file_path)


if __name__ == "__main__":
    main()