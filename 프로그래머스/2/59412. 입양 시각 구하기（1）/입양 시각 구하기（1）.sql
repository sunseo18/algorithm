-- 코드를 입력하세요
SELECT HOUR(DATETIME) as HOUR, count(*) as COUNT
from ANIMAL_OUTS
WHERE TIME(DATETIME) between '09:00' and '19:59'
group by HOUR
order by hour;