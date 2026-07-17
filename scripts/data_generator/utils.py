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


def current_date() -> str:
    """
    Return today's date in format "dd-mm-yyyy
    """
    return datetime.now().strftime("%d-%m-%Y")


def current_timestamp() -> str:
    """
    Return the current timestamp in ISO format.
    """
    return datetime.now().isoformat()


def generate_uuid() -> str:
    """
    Generate a unique string
    """
    return str(uuid.uuid4())


def calculate_revenue(quantity: int, unit_price: Decimal, discount: Decimal) -> Decimal:
    """
    Calculate sales revenue.

    Formula:
    Revenue = (Quantity * Unit Price)- Discount

    """
    return (unit_price * quantity) - discount
