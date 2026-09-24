-- Write your query below
with base as ( 
    select A.customer_id, 
           A.name, 
           B.order_id, 
           B.order_date,
           RANK() OVER (PARTITION BY A.customer_id ORDER BY B.order_date DESC) as rk 
    from customers A 
    inner join orders B on A.customer_id = B.customer_id 
)

select name as customer_name, 
       customer_id, 
       order_id, 
       order_date
from base 
where rk < 4 
order by 1 