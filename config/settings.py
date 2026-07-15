from pathlib import Path

## process to retrieve the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

## Assigning the data directory path TO VariableS

DATA_DIR = BASE_DIR / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

SALES_DIR = RAW_DATA_DIR / "sales"

CUSTOMER_DIR = RAW_DATA_DIR / "customers"

PRODUCT_DIR = RAW_DATA_DIR / "products"

ARCHIVE_DIR = RAW_DATA_DIR / "archive"

VALIDATED_DIR = DATA_DIR / "validated"

PROCESSED_DIR = DATA_DIR / "processed"

REJECTED_DIR = DATA_DIR / "rejected"

EXPORT_DIR = DATA_DIR / "exports"

LOG_DIR = BASE_DIR / "logs"

# Dataset Sizes

NUM_CUSTOMERS = 10000

NUM_PRODUCTS = 2000

NUM_SALES = 100000

# Random Seed

RANDOM_SEED = 42

# Date Format

DATE_FORMAT = "%d-%m-%Y"
