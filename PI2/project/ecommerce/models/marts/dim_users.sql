{{ config(materialized='table') }}
select
  user_id,
  name,
  email,
  country,
  state,
  province,
  city,
  district,
  street,
  apartment,
  zip_code
from {{ ref('int_users') }}
