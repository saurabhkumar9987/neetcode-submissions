-- Write your query below
with base as (
select log_id, 
       rank() OVER (order by log_id) as rk
from logs) , 

intermediate as 
(
select log_id, 
       (log_id - rk) as island_id
from base 
), 
final as (
select island_id, 
       min(log_id) as start_id,
       max(log_id) as end_id
from intermediate
group by 1) 

select start_id, 
       end_id 
from final 
order by 1



