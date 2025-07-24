{{ config(materialized='view') }}

select
  p.product_id,
  p.product_name,
  p.product_description,
  p.price,
  p.stock,
  p.category_id,
  c.category_name,
  c.category_description
from {{ ref('stg_products') }} as p
left join {{ ref('stg_category') }} as c
  using(category_id)
