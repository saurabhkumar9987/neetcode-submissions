-- Write your query below
with base as (
select student_id, 
       exam_id,
       score,  
       RANK() OVER (PARTITION BY student_id  ORDER BY score DESC) as rk 
from exam_results 
) 

select student_id, 
       MIN(exam_id) as exam_id, 
       score 
from base 
where rk = 1 
group by 1,3