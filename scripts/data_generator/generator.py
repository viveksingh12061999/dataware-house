"""
Master Data Generator

Responsible for running all source data generation jobs
for the Retail Data Warehouse project.
"""

#
from config.settings import NUM_CUSTOMERS

print(f"Customers to generate: {NUM_CUSTOMERS}")


#
from config.settings import (
    SALES_DIR,
    CUSTOMER_DIR,
    PRODUCT_DIR,
)
from scripts.data_generator.utils import create_directory

create_directory(SALES_DIR)
create_directory(CUSTOMER_DIR)
create_directory(PRODUCT_DIR)


def generate_customers():
    print("Generating customers...")


def generate_products():
    print("Generating products...")


def generate_sales():
    print("Generating sales...")


def main():
    print("=" * 60)
    print("Retail Data Warehouse")
    print("Source Data Generation")
    print("=" * 60)

    # Create required directories
    create_directory(CUSTOMER_DIR)
    create_directory(PRODUCT_DIR)
    create_directory(SALES_DIR)

    generate_customers()
    generate_products()
    generate_sales()

    print("\nData generation completed successfully.")


if __name__ == "__main__":
    main()
