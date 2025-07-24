{{ config(materialized='view') }}

with o as (
  select
    order_id,
    user_id,
    order_at,
    total,
    order_status
  from {{ ref('stg_orders') }}
),

items as (
  select
    order_id,
    sum(quantity) as total_items
  from {{ ref('stg_orders_details') }}
  group by order_id
),

pm as (
  select
    order_id,
    count(distinct payment_method_id) as payment_method_count,
    max(payment_status)             as payment_status
  from {{ ref('stg_payments') }}
  group by order_id
),

addr as (
  select
    shipping_address_id,
    user_id,
    shipping_address,
    order_id
  from (
    select
      a.shipping_address_id,
      a.user_id,
      concat_ws(', ',
        a.street, a.city, a.province, a.country
      ) as shipping_address,
      o.order_id
    from {{ ref('stg_shipping_address') }} as a
    join {{ ref('stg_orders') }} as o
      using(user_id)
  )
)

select
  o.order_id,
  o.user_id,
  to_char(o.order_at,'YYYYMMDD')::int as date_id,
  o.order_at,
  o.total,
  o.order_status,
  coalesce(i.total_items,0)         as total_items,
  coalesce(pm.payment_method_count,0) as payment_method_count,
  pm.payment_status,
  addr.shipping_address_id
from o
left join items as i   using(order_id)
left join pm          using(order_id)
left join addr        using(order_id)
