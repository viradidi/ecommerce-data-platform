# E-Commerce Data Model

## Overview

The E-Commerce Data Platform uses a layered data model designed to support
reliable ingestion, analytical workloads, reporting, and downstream data
products.

The model separates operational entities from analytical representations so
that source data can evolve without directly breaking downstream consumers.

---

## Core Business Entities

The platform is centered around the following entities:

- Customers
- Products
- Categories
- Orders
- Order Items
- Payments
- Shipments

---

## Entity Relationships

```text
Customer
   │
   │ 1:N
   ▼
Orders
   │
   │ 1:N
   ▼
Order Items
   │
   ├──────────────► Products
   │                    │
   │                    ▼
   │                Categories
   │
   ├──────────────► Payments
   │
   └──────────────► Shipments# E-Commerce Data Model

## Overview

The E-Commerce Data Platform uses a layered data model designed to support
reliable ingestion, analytical workloads, reporting, and downstream data
products.

The model separates operational entities from analytical representations so
that source data can evolve without directly breaking downstream consumers.

---

## Core Business Entities

The platform is centered around the following entities:

- Customers
- Products
- Categories
- Orders
- Order Items
- Payments
- Shipments

---

## Entity Relationships

```text
Customer
   │
   │ 1:N
   ▼
Orders
   │
   │ 1:N
   ▼
Order Items
   │
   ├──────────────► Products
   │                    │
   │                    ▼
   │                Categories
   │
   ├──────────────► Payments
   │
   └──────────────► Shipments
