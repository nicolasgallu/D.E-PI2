{{ config(materialized='table') }}

with dates as (
  select
    generate_series(
      date_trunc('year', current_date) - interval '1 year',
      date_trunc('year', current_date) + interval '1 year',
      interval '1 day'
    )::date as full_date
)

select
  to_char(full_date,'YYYYMMDD')::int as date_id,
  full_date,
  extract(day   from full_date)::int  as day,
  extract(month from full_date)::int  as month,
  extract(year  from full_date)::int  as year,
  to_char(full_date,'Day')           as weekday,
  (extract(dow from full_date) in (0,6)) as is_weekend
from dates
