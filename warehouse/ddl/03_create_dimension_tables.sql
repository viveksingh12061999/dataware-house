CREATE TABLE IF NOT EXISTS warehouse.dim_customer
(
    customer_key           BIGSERIAL PRIMARY KEY,

    customer_id            INTEGER NOT NULL UNIQUE,

    customer_name          VARCHAR(150) NOT NULL,

    email                  VARCHAR(255),

    phone                  VARCHAR(30),

    city                   VARCHAR(100),

    state                  VARCHAR(100),

    country                VARCHAR(100),

    registration_date      DATE,

    is_active              BOOLEAN DEFAULT TRUE,

    created_at             TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at             TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



CREATE TABLE IF NOT EXISTS warehouse.dim_product
(
    product_key            BIGSERIAL PRIMARY KEY,

    product_id             INTEGER NOT NULL UNIQUE,

    product_name           VARCHAR(255),

    category               VARCHAR(100),

    supplier_name          VARCHAR(150),

    unit_cost              NUMERIC(12,2),

    selling_price          NUMERIC(12,2),

    is_active              BOOLEAN DEFAULT TRUE,

    created_at             TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at             TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE IF NOT EXISTS warehouse.dim_region
(
    region_key          BIGSERIAL PRIMARY KEY,

    city                VARCHAR(100),

    state               VARCHAR(100),

    country             VARCHAR(100),

    region_name         VARCHAR(100)
);


CREATE TABLE IF NOT EXISTS warehouse.dim_date
(
    date_key            INTEGER PRIMARY KEY,

    full_date           DATE UNIQUE,

    day_number          INTEGER,

    day_name            VARCHAR(20),

    week_number         INTEGER,

    month_number        INTEGER,

    month_name          VARCHAR(20),

    quarter_number      INTEGER,

    year_number         INTEGER,

    is_weekend          BOOLEAN
);