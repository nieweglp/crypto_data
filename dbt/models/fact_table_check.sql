{{ config(materialized='view') }}

select *
from fact_spot_price
order by fetched_timestamp
limit 5

/*
    Uncomment the line below to remove records with null `id` values
*/

-- where id is not null
