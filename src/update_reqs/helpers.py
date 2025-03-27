import os

def _file_exists_(file_path) -> bool:
    if not os.path.exists(file_path):
        return False
    return True

