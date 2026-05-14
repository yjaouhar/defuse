
from pathlib import Path

def remove_files(files_path : list):
     for file in files_path:
        path = Path(file)
        try:
            if path.exists() and path.is_file():
                path.unlink()
        except Exception as e:
            print(f"Failed to delete {path}: {e}")