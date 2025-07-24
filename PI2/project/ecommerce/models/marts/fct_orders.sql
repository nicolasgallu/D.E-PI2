{{ config(materialized='table') }}
select
  order_id,
  user_id,
  date_id,
  order_at,
  total,
  order_status,
  total_items,
  payment_method_count,
  payment_status,
  shipping_address_id
from {{ ref('int_orders') }}
