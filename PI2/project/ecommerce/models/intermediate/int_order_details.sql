{{ config(materialized='view') }}

with od as (
  select
    order_detail_id,
    order_id,
    product_id,
    quantity,
    unit_price
  from {{ ref('stg_orders_details') }}
),

prod as (
  select
    product_id,
    product_name,
    product_description,
    category_id,
    category_name
  from {{ ref('int_products') }}
),

ord as (
  select
    order_id,
    order_at
  from {{ ref('int_orders') }}
)

select
  od.order_detail_id,
  od.order_id,
  od.product_id,
  prod.category_id,
  prod.product_name,
  prod.product_description,
  prod.category_name,
  od.quantity,
  od.unit_price,
  od.quantity * od.unit_price as subtotal,
  to_char(ord.order_at,'YYYYMMDD')::int as date_id
from od
join ord on od.order_id = ord.order_id
left join prod on od.product_id = prod.product_id
