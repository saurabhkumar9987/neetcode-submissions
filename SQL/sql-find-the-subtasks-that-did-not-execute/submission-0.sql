-- Write your query below
with base as ( 
       select task_id, 
              subtasks_count,
              generate_series(1,subtasks_count) as subtask_id 
       from tasks 
), 
intermediate as ( 
select A.task_id, 
       A.subtask_id, 
       B.subtask_id as executed_task_id 
from base A
left join executed B ON A.task_id = B.task_id and A.subtask_id = B.subtask_id) 

select task_id, 
        subtask_id 
from intermediate 
where executed_task_id is null