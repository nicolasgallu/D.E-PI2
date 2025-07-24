{{ config(materialized='table') }}
select
  review_id,
  product_id,
  user_id,
  date_id,
  review_score,
  comment,
  reviewed_at
from {{ ref('int_reviews') }}
