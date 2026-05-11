-- https://leetcode.com/problems/consecutive-numbers/description/

-- - time window: 3
-- - id >= current_id and id < current_id + 3 => 모두 같은 숫자인 경우 select

SELECT DISTINCT num AS ConsecutiveNums
FROM (
  SELECT l1.num
  FROM Logs l1
  JOIN Logs l2 ON l1.num = l2.num
    AND l2.id >= l1.id
    AND l2.id < l1.id + 3
  GROUP BY l1.id, l1.num
  HAVING COUNT(l1.id) = 3
)

---------- LEAD (https://www.postgresql.org/docs/current/functions-window.html) ----------
WITH leads AS (
    SELECT
        num,
        LEAD(num, 1) OVER(ORDER BY id) as next_1,
        LEAD(num, 2) OVER(ORDER BY id) as next_2
    FROM Logs
)

SELECT DISTINCT
    num as ConsecutiveNums
FROM leads
WHERE num = next_1 and num = next_2;