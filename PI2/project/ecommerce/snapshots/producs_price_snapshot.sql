{% snapshot products_price_snapshot %}

{{
  config(
    target_schema=target.schema,
    target_database=target.database,
    strategy='check',
    unique_key='product_id',
    check_cols=['price']
  )
}}

select
  product_id,
  product_name as name,
  product_description as description,
  price

from {{ ref('int_products') }}

{% endsnapshot %}
