# E-Commerce Data Platform

An end-to-end, production-oriented data platform for ingesting,
validating, transforming, and serving e-commerce data for analytics.

The project demonstrates modern data engineering practices including:

- Python data ingestion
- Apache Airflow orchestration
- PostgreSQL
- dbt analytics engineering
- Data quality validation
- Bronze → Silver → Gold architecture
- Docker-based development
- Automated pipeline execution
- Idempotent data loading
- Analytics-ready data models
- Testing and observability foundations

---

## Architecture

```text
                    ┌──────────────────────┐
                    │   E-Commerce Sources │
                    │   CSV / Operational  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │     Ingestion        │
                    │      Python          │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      Bronze          │
                    │     Raw Data         │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Data Validation    │
                    │     Quality Checks   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │       Silver         │
                    │ Cleaned / Standardized│
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │        dbt           │
                    │ Transformations      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │        Gold          │
                    │ Analytics Models     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Analytics / BI       │
                    │ Trusted Metrics      │
                    └──────────────────────┘