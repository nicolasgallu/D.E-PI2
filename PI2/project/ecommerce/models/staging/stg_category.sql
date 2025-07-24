{{ config(materialized='view') }}

with source as (
    select * from {{ source('raw', 'categorias') }}
),

renamed as (
    select
        id as category_id,	
        nombre as category_name,	
        descripcion as category_description
    from source
    where id is not null
)

select * from renamed
