
from pathlib import Path
import os

def remove_exe(path_str):
    try:
        path = Path(path_str)

        if path.exists() and path.is_file():
            os.remove(path)

    except Exception as e:
        print(f"Failed to remove {path_str}: {e}")