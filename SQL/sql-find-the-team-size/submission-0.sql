-- Write your query below
select employee_id, 
       COUNT(*) OVER (partition by team_id) as team_size
from employee 
order by 1 