{{ config(materialized='view') }}

with source as (
    select * from {{ source('raw', 'resenas_productos') }}
),

renamed as (
    select
        cast(id  as integer) as review_id,
        cast(usuario_id as integer) as user_id,
        cast(producto_id  as integer) as product_id,
        cast(calificacion as  decimal) as review_score,
        trim(comentario) as comment,
        cast(fecha as date) as reviewed_at
    from source
    where id is not null
)

select * from renamed
