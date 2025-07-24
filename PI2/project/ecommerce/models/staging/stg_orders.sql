{{ config(materialized='view') }}

with source as (
    select * from {{ source('raw', 'ordenes') }}
),

renamed as (
    select
        cast(id as integer) as order_id,
        cast(usuario_id as integer) as user_id,
        cast(fecha_orden as timestamp) as order_at,
        cast(total as numeric) as total,
        trim(estado) as order_status
    from source
    where id is not null
)

select * from renamed
