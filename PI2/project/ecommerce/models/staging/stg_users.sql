{{ config(materialized='view') }}

with source as (
    select * from {{ source('raw', 'usuarios') }}
),

renamed as (
    select
        cast(id as integer) as user_id,
        initcap(trim(nombre)) as name,
        lower(trim(email)) as email
    from source
    where email is not null and email like '%@%'
)

select * from renamed
