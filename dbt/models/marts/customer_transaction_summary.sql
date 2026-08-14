select
    customer_id,
    customer_name,
    amount as total_amount,
    loaded_at
from {{ ref("stg_customer_transactions") }}
