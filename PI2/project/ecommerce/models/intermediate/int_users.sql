{{ config(materialized='view') }}

select
  u.user_id,
  u.name,
  u.email,
  a.shipping_address_id,
  a.country,
  a.state,
  a.province,
  a.city,
  a.district,
  a.street,
  a.apartment,
  a.zip_code
from {{ ref('stg_users') }} as u
left join {{ ref('stg_shipping_address') }} as a
  using(user_id)
