# Database Design

## Business Process

Retail Sales Analytics

---

## Grain

One record in the fact table represents one product sold in one order.

---

## Star Schema

dim_customer
      |
dim_region --- fact_sales --- dim_product
      |
   dim_date

---

## Schemas

### staging

Raw imported data.

### warehouse

Dimension and Fact tables.

### metadata

ETL tracking.

### audit

Audit logging.

### reporting

Power BI SQL Views.

---

## Dimension Tables

- dim_customer
- dim_product
- dim_region
- dim_date

---

## Fact Table

fact_sales

Measures

- quantity
- revenue
- discount
- profit
- discount

Foreign Keys

- customer_key
- product_key
- region_key
- date_key