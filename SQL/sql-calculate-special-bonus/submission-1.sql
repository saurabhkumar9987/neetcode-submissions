-- Write your query below
select employee_id, 
       (case when (employee_id%2)=0 or name LIKE 'M%' then 0 else salary end) as bonus
from employees
order by 1 