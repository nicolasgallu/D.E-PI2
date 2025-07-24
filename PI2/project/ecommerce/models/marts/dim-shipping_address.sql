{{ config(materialized='table') }}
select
  shipping_address_id,
  user_id,
  country,
  state,
  province,
  city,
  district,
  street,
  apartment,
  zip_code
from {{ ref('stg_shipping_address') }}
