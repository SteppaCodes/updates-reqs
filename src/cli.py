import argparse
import re
import os
import sys

def clean_requirements(file_path):
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

    print("File Cleaned Successfully")


def main():
    parser = argparse.ArgumentParser(description="A smart CLI tool that automatically updates your requirements.txt by fetching the latest versions of outdated libraries from PyPI.")
    parser.add_argument("--file", required=True, help="path to requirements file")
    args = parser.parse_args()

    file_path = args.file

    if not os.path.exists(file_path):
        print(f" Error: {file_path} does not exist.")
        sys.exit(1)  
    clean_requirements(args.file)


if __name__ == "__main__":
    main()