from datetime import datetime
from decimal import Decimal
from pathlib import Path
import uuid


def create_directory(path: Path):
    """
    Create a directory if it doesn't exist.

    Args:
        path (Path): The path of the directory to create.
    """
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
