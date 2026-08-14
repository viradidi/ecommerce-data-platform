# Production Data Platform

An end-to-end, containerized data engineering platform demonstrating
batch ingestion, data quality validation, PostgreSQL warehousing,
dbt analytics engineering, orchestration, and reproducible deployment.

## Architecture

```text
CSV Source
    │
    ▼
Apache Airflow
    │
    ├── Extract
    │
    ├── Validate
    │
    └── Load
          │
          ▼
     PostgreSQL
          │
          ▼
      dbt Staging
          │
          ▼
      dbt Mart
          │
          ▼
Customer Transaction Summary