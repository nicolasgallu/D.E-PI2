{{ config(materialized='table') }}
select
  order_detail_id,
  order_id,
  product_id,
  category_id,
  product_name,
  product_description,
  category_name,
  quantity,
  unit_price,
  subtotal,
  date_id
from {{ ref('int_order_details') }}
