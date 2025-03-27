import re
import requests
import subprocess
# from .helpers import validate_file_added

def clean(file_path):
    """
        Function to remove all version number from requirements and write file back
    """
    if file_path == None:
        print("This command requires a file")
        return False
        
    with open(file_path, "r") as file:
        lines = file.readlines()
    
    # Split the text at any of the specified characters <>=
    # Returns a list of two values ["library", "version"]
    cleaned_lines = [re.split(r"[<>=]+", line.strip())[0] for line in lines]

    with open(file_path, "w") as file:
        file.write("\n".join(cleaned_lines) + "\n")

    print("Requirements Cleaned Successfully")

def get_all_installed_packages():
    # Run a subprocess to get all installed packages using pip freeze
    result = subprocess.run(["pip", "freeze"], capture_output=True, text=True)
    packages = {}

    for line in result.stdout.splitlines():
        if "==" in line:
            package, version = line.split("==")
            packages[package] = version

    return packages

def get_latest_version(package):
    url = f"https://pypi.org/pypi/{package}/json"
    response = requests.get(url)
    
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.json()["info"]["version"]
        else:
            print(f"Could not fetch version for {package}")
    except requests.RequestException:
        print(f"Network error while checking {package}")

    return None


def get_outdated(packages):
    """
    function to get outdated packages
    """
    outdated = []
    
    for package, installed_version in packages.items():
        # get latest version
        latest_version = get_latest_version(package)
        if latest_version and latest_version != installed_version:
            outdated.append((package, installed_version, latest_version))

    if outdated:
        print("\nOutdated Packages Found:\n")
        for package, installed, latest in outdated:
            print(f"{package}: Installed {installed} → Latest {latest}")
    else:
        print("All installed packages are up to date")

    return True
        
def check(file_path=None):
    packages = get_all_installed_packages()
    get_outdated(packages)
    
    

