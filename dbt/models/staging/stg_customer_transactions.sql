select
    customer_id,
    customer_name,
    amount,
    loaded_at
from {{ source("raw", "customer_transactions") }}
