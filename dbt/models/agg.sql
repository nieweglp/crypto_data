{{ config(materialized='view') }}

select
	date_trunc('minute',
	fetched_timestamp) as casted_fetched_timestamp,
	round(cast(avg(price) as numeric),
	2) as avg_minutes_price
from
	fact_spot_price
group by
	date_trunc('minute',
	fetched_timestamp)
order by
	1