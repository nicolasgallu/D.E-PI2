{{ config(materialized='view') }}

with source as (
    select * from {{ source('raw', 'historial_pagos') }}
),

renamed as (
    select
        cast(id as integer) as payment_id,
        cast(orden_id as integer) as order_id,
        cast(metodo_pago_id as integer) as payment_method_id,
        cast(monto as numeric) as amount,
        cast(fecha_pago as timestamp) as payment_date,
        trim(estado_pago) as payment_status
    from source
    where id is not null
)

select * from renamed
