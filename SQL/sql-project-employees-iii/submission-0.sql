-- Write your query below
with base as 
(select A.project_id, 
       B.employee_id, 
       B.experience_years as exp_yrs, 
       RANK() OVER (partition by A.project_id order by B.experience_years desc) as rk 
from project A
inner join employee B ON A.employee_id = B.employee_id 
) 

select project_id, 
       employee_id
from base
where rk = 1  