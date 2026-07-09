CREATE TABLE IF NOT EXISTS staging.stg_sales
(
    staging_id      BIGSERIAL PRIMARY KEY,

    order_id        INTEGER NOT NULL,
    customer_id     INTEGER NOT NULL,
    product_id      INTEGER NOT NULL,

    quantity        INTEGER NOT NULL,

    unit_price      NUMERIC(12,2) NOT NULL,

    discount        NUMERIC(12,2) DEFAULT 0,

    revenue         NUMERIC(12,2),

    order_date      DATE,

    source_system   VARCHAR(50),

    batch_id        UUID,

    file_name       VARCHAR(255),

    load_timestamp  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    row_status      VARCHAR(20) DEFAULT 'PENDING',

    error_message   TEXT
);

CREATE TABLE IF NOT EXISTS staging.stg_customers
(
    staging_id          BIGSERIAL PRIMARY KEY,

    customer_id         INTEGER,

    customer_name       VARCHAR(150),

    email               VARCHAR(255),

    phone               VARCHAR(30),

    city                VARCHAR(100),

    state               VARCHAR(100),

    country             VARCHAR(100),

    registration_date   DATE,

    source_system       VARCHAR(50),

    batch_id            UUID,

    file_name           VARCHAR(255),

    load_timestamp      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    row_status          VARCHAR(20) DEFAULT 'PENDING',

    error_message       TEXT
);

CREATE TABLE IF NOT EXISTS staging.stg_products
(
    staging_id      BIGSERIAL PRIMARY KEY,

    product_id      INTEGER,

    product_name    VARCHAR(255),

    category        VARCHAR(100),

    unit_cost       NUMERIC(12,2),

    selling_price   NUMERIC(12,2),

    supplier_name   VARCHAR(150),

    source_system   VARCHAR(50),

    batch_id        UUID,

    file_name       VARCHAR(255),

    load_timestamp  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    row_status      VARCHAR(20) DEFAULT 'PENDING',

    error_message   TEXT
);