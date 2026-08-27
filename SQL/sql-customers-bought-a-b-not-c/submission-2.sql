-- Write your query below
with base as (
select customer_id, 
       sum(case when product_name='A' then 1 else 0 end) total_a, 
       sum(case when product_name='B' then 1 else 0 end) total_b,
       sum(case when product_name='C' then 1 else 0 end) total_c
from orders
group by 1 
)

select A.customer_id, 
       B.customer_name
from base A 
inner join customers B ON A.customer_id = B.customer_id 
where total_a > 0 and total_b > 0 and total_c = 0 
order by 2 