{{ config(materialized='view') }}

with source as (
    select * from {{ source('raw', 'direcciones_envio') }}
),

renamed as (
    select
        cast(id as  integer) as shipping_address_id,
        cast(usuario_id as integer) as user_id,
        initcap(trim(pais)) as country,
        initcap(trim(estado)) as state,
        initcap(trim(provincia)) as province,
        initcap(trim(ciudad)) as city,
        initcap(trim(distrito)) as district,
        initcap(trim(calle)) as street,
        upper(trim(departamento)) as apartment,
        trim(codigo_postal) as zip_code
    from source
    where id is not null
)

select * from renamed
