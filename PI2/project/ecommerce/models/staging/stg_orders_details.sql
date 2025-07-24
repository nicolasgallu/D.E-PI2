{{ config(materialized='view') }}

with source as (
    select * from {{ source('raw', 'detalle_ordenes') }}
),

renamed as (
    select
        cast(id as integer) as order_detail_id,
        cast(orden_id as integer) as order_id,
        cast(producto_id as integer) as product_id,
        cast(cantidad as integer) as quantity,
        cast(precio_unitario as numeric) as unit_price
    from source
    where id is not null
)

select * from renamed
