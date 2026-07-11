-- =====================================================
-- File: 04_create_fact_tables.sql
-- Schema: warehouse
-- Table : fact_sales
-- Description: Sales fact table
-- =====================================================

CREATE TABLE IF NOT EXISTS warehouse.fact_sales
(
    sales_key BIGSERIAL PRIMARY KEY,

    customer_key BIGINT NOT NULL,

    product_key BIGINT NOT NULL,

    region_key BIGINT NOT NULL,

    date_key INTEGER NOT NULL,

    order_id INTEGER NOT NULL,

    quantity INTEGER NOT NULL CHECK (quantity > 0),

    unit_price NUMERIC(12,2) NOT NULL CHECK (unit_price >= 0),

    discount NUMERIC(12,2) DEFAULT 0 CHECK (discount >= 0),

    revenue NUMERIC(12,2) NOT NULL,

    cost NUMERIC(12,2),

    profit NUMERIC(12,2),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_fact_customer
        FOREIGN KEY (customer_key)
        REFERENCES warehouse.dim_customer(customer_key),

    CONSTRAINT fk_fact_product
        FOREIGN KEY (product_key)
        REFERENCES warehouse.dim_product(product_key),

    CONSTRAINT fk_fact_region
        FOREIGN KEY (region_key)
        REFERENCES warehouse.dim_region(region_key),

    CONSTRAINT fk_fact_date
        FOREIGN KEY (date_key)
        REFERENCES warehouse.dim_date(date_key)
);