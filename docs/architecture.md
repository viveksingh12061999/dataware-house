# Retail Data Warehouse Architecture

## Overview

The Retail Data Warehouse is a production-oriented analytics platform that integrates sales, customer, and product data from multiple source systems into a centralized PostgreSQL data warehouse.

The project demonstrates enterprise ETL architecture, dimensional modeling, metadata-driven loading, and business intelligence reporting using Power BI.

---

## Technology Stack

- Python
- PostgreSQL
- SQLAlchemy
- FastAPI
- Pandas
- Power BI
- Git
- Docker (planned)

---

## Source Systems

- CSV Files (Sales)
- Excel Files (Customers)
- REST API (Products)

---

## Data Flow

Source Systems
        ↓
Extract Layer
        ↓
Staging Schema
        ↓
Validation
        ↓
Transformation
        ↓
Warehouse Schema
        ↓
Reporting Views
        ↓
Power BI Dashboard

---

## PostgreSQL Schemas

- staging
- warehouse
- metadata
- audit
- reporting

---

## Design Principles

- Star Schema
- Surrogate Keys
- Metadata-driven ETL
- Modular SQL Scripts
- Audit Logging
- Batch Processing