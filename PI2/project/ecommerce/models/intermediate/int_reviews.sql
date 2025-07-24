{{ config(materialized='view') }}

select
  review_id,
  user_id,
  product_id,
  review_score,
  comment,
  reviewed_at,
  to_char(reviewed_at,'YYYYMMDD')::int as date_id
from {{ ref('stg_reviews') }}
