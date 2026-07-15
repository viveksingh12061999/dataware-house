# ETL Flow

## Extract

Read data from:

- CSV
- Excel
- REST API

---

## Load to Staging

Insert raw records into:

- staging.stg_sales
- staging.stg_customers
- staging.stg_products

---

## Validation

Validate:

- NULL values
- Duplicate records
- Invalid dates
- Negative quantities
- Price consistency

---

## Transformation

Generate:

- Surrogate keys
- Revenue
- Profit

---

## Warehouse Loading

Populate:

- Dimension tables
- Fact table

---

## Reporting

Refresh SQL Views

Power BI consumes reporting schema only.

## Data Generation

The project includes a configurable data generation framework that simulates multiple enterprise source systems.

Generated Sources

- POS Sales (CSV)
- CRM Customers (Excel)
- Product Service (JSON)

All generated datasets follow the Source Data Contract and are used as input for the Extract Layer.