# E-Commerce Data Platform

An end-to-end production-oriented data platform for ingesting,
transforming, validating, and serving e-commerce data for analytics.

## Problem

E-commerce businesses generate data across customers, products,
orders, order items, and payments.

Without a reliable data platform, analytical teams can struggle
with inconsistent data, manual reporting, data quality issues,
and slow access to trusted metrics.

This project demonstrates how to build a reliable analytical
data platform from raw operational data.

## Architecture

The platform follows a Bronze → Silver → Gold architecture.

```text
Source Data
    ↓
Ingestion
    ↓
Bronze
    ↓
Spark Transformations
    ↓
Silver
    ↓
Business Transformations
    ↓
Gold
    ↓
Analytics
