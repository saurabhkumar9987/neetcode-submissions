-- Write your query below
with exam_highest_and_lowest as ( 
    select exam_id, 
           MAX(score) as highest_score, 
           MIN(score) as lowest_score
    from exam
    group by 1 
), 

quiet_students as ( 
    select A.student_id, 
           A.exam_id, 
           A.score,
           B.highest_score, 
           B.lowest_score, 
           (case when (A.score != B.highest_score and A.score != B.lowest_score) then 1 else 0 end) as quiet_category
    from exam A 
    inner join exam_highest_and_lowest B ON A.exam_id = B.exam_id 
), 
final as (
    select student_id, 
           count(exam_id) as total_exams, 
           sum(quiet_category) as quiet_category
    from quiet_students
    group by 1 
    ) 


select A.student_id, 
       B.student_name 
from final A
inner join student B ON A.student_id = B.student_id 
where A.quiet_category = A.total_exams
order by 1 

