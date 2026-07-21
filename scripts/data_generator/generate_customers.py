"""
Customer data generator.

Simulates CRM customer master data for the
Retail Data Warehouse project.
"""

import pandas as pd
from random import seed
from faker import Faker

from config.settings import NUM_CUSTOMERS
from config.settings import RANDOM_SEED
from scripts.data_generator.logger import setup_logger

logger = setup_logger(__name__)

seed(RANDOM_SEED)
Faker.seed(RANDOM_SEED)


class CustomerGenerator:
    """
    Generate customer master data.
    """

    def __init__(self):
        self.fake = Faker("en_IN")
        self.num_customers = NUM_CUSTOMERS
        self.start_customer_id = 10001

    def generate_dataset(self) -> list[dict]:
        """
        Generate the complete customer dataset.
        """

        customers = []

        for customer_id in range(
            self.start_customer_id, self.start_customer_id + self.num_customers
        ):
            customers.append(self.generate_customer(customer_id))

        logger.info("Generated %d customer records.", len(customers))

        return customers

    def generate_customer(self, customer_id: int) -> dict:
        """
        Generate one customer record.
        """

        return {
            "customer_id": customer_id,
            "first_name": self.fake.first_name(),
            "last_name": self.fake.last_name(),
            "email": self.fake.email(),
            "phone": self.fake.msisdn()[:10],
            "city": self.fake.city(),
            "state": self.fake.state(),
            "country": "India",
            "registration_date": self.fake.date_between(
                start_date="-5y", end_date="today"
            ),
        }

    def create_dataframe(self, customers: list[dict]) -> pd.DataFrame:
        """
        Convert customer records into a pandas DataFrame.
        """

        dataframe = pd.DataFrame(customers)

        logger.info(
            "Customer DataFrame created with %d rows and %d columns.",
            len(dataframe),
            len(dataframe.columns),
        )

        return dataframe


def main():
    generator = CustomerGenerator()

    customers = generator.generate_dataset()

    customer_df = generator.create_dataframe(customers)

    logger.info("Preview of customer data:\n%s", customer_df.head())

    logger.info("Data types:\n%s", customer_df.dtypes)

    logger.info("Column order: %s", customer_df.columns.tolist())

    logger.info("Sample customer: %s", customers[0])


if __name__ == "__main__":
    main()
