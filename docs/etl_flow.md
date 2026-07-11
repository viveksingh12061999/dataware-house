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