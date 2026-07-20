"""
Master Data Generator

Responsible for running all source data generation jobs
for the Retail Data Warehouse project.
"""

# Create logger
from scripts.data_generator.logger import setup_logger

logger = setup_logger(__name__)

#
from config.settings import NUM_CUSTOMERS

logger.info(f"Customers to generate: {NUM_CUSTOMERS}")


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
    logger.info("Generating customers...")


def generate_products():
    logger.info("Generating products...")


def generate_sales():
    logger.info("Generating sales...")


def main():
    def main():
        try:
            logger.info("=" * 60)
            logger.info("Retail Data Warehouse")
            logger.info("Source Data Generation")
            logger.info("=" * 60)

            logger.info("Starting source data generation.")

            generate_customers()
            generate_products()
            generate_sales()

            logger.info("Source data generation completed successfully.")

        except Exception as exc:
            logger.exception("Data generation failed.")
            raise


if __name__ == "__main__":
    main()
