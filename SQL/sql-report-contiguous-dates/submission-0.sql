-- Write your query below
with base as ( 
    select 'failed' as status, 
            fail_date as event_date
    from failed
    WHERE fail_date >= '2019-01-01'  and fail_date <= '2019-12-31'
    UNION ALL 
    select 'succeeded' as status, 
            success_date as event_date
    from succeeded
    WHERE success_date >= '2019-01-01'  and success_date <= '2019-12-31'
), 
intermediate as ( 
select status , 
       event_date, 
       row_number() over (partition by status order by event_date) as status_rk, 
       row_number() over (order by event_date) as rk 
from base 
order by event_date), 

final as (
select status , 
       event_date, 
       rk - status_rk as grp 
from intermediate
)

select t.period_state, 
       t.start_date, 
       t.end_date
from (
select status as period_state, 
       grp, 
       min(event_date) as start_date, 
       max(event_date) as end_date
from final 
group by 1 , 2 
order by 3) t 




