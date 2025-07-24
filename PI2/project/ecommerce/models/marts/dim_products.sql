{{ config(materialized='table') }}
select
  product_id,
  product_name   as name,
  product_description as description,
  price,
  stock,
  category_id,
  category_name,
  category_description
from {{ ref('int_products') }}
