with base as (
    select user_id, 
           visit_date, 
           LEAD(visit_date) OVER (PARTITION BY user_id ORDER BY visit_date) as next_visit_date
    from user_visits
), 

intermediate as ( 
    select user_id, 
           visit_date, 
           COALESCE(next_visit_date,'2021-1-1') as next_visit_date
    from base 
)


select user_id, 
       MAX(next_visit_date::date - visit_date::date) AS biggest_window
from intermediate 
group by 1 