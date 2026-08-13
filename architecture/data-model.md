# E-Commerce Data Platform — Data Model

## 1. Purpose

This document defines the logical data model used by the E-Commerce Data Platform.

The model represents core transactional entities and provides the foundation for downstream analytical processing.

The design separates operational entities from analytical models so that raw source data can be transformed into trusted business datasets.

---

## 2. Core Entities

The initial platform contains six core entities:

- Customers
- Products
- Categories
- Orders
- Order Items
- Payments

---

## 3. Entity Relationship

```text
                    +----------------+
                    |   CATEGORIES   |
                    |----------------|
                    | category_id PK |
                    | category_name  |
                    +-------+--------+
                            |
                            |
                            v
                    +----------------+
                    |    PRODUCTS    |
                    |----------------|
                    | product_id PK  |
                    | category_id FK |
                    | product_name   |
                    | price          |
                    | cost           |
                    +-------+--------+
                            |
                            |
                            v
                    +----------------+
                    |  ORDER_ITEMS   |
                    |----------------|
                    | order_item_id  |
                    | order_id FK     |
                    | product_id FK   |
                    | quantity        |
                    | unit_price      |
                    +-------+---------+
                            |
                            |
                            v
                    +----------------+
                    |     ORDERS     |
                    |----------------|
                    | order_id PK    |
                    | customer_id FK |
                    | order_date     |
                    | status         |
                    | region         |
                    | total_amount   |
                    +-------+---------+
                            |
                            |
                            v
                    +----------------+
                    |   CUSTOMERS    |
                    |----------------|
                    | customer_id PK |
                    | first_name     |
                    | last_name      |
                    | email          |
                    | country        |
                    | created_at     |
                    +----------------+

                    +----------------+
                    |    PAYMENTS    |
                    |----------------|
                    | payment_id PK  |
                    | order_id FK    |
                    | payment_method |
                    | payment_status |
                    | amount         |
                    | paid_at        |
                    +----------------+
