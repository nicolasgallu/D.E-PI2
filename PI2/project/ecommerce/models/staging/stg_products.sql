{{ config(materialized='view') }}

with source as (
  select * from {{ source('raw','productos') }}
),

renamed as (
  select
    cast(id as integer)  as product_id,
    trim(nombre) as product_name,
    trim(descripcion) as product_description,
    cast(precio as numeric) as price,
    cast(stock as integer) as stock,
    cast(categoria_id as integer) as category_id
  from source
  where id is not null
)

select * from renamed
