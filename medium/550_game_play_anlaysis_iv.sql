-- https://leetcode.com/problems/game-play-analysis-iv/

WITH total_player_count AS (
    SELECT COUNT(DISTINCT player_id) as denom
    FROM Activity
),
initial_logged_in_info AS (
    SELECT player_id, MIN(event_date) AS initial_log_in_date
    FROM Activity
    GROUP BY player_id
),
re_logged_in_player_count AS (
    SELECT COUNT(DISTINCT a.player_id) as numer
    FROM Activity a
    WHERE a.event_date = (
        SELECT initial_log_in_date
        FROM initial_logged_in_info ii
        WHERE ii.player_id = a.player_id
    ) + 1
)
SELECT 
    ROUND(
        (
            (SELECT numer::FLOAT FROM re_logged_in_player_count) 
            / (SELECT denom::FLOAT FROM total_player_count)
        )::NUMERIC
        , 2
    ) 
    AS fraction

-- Better Solution
SELECT 
    ROUND(
        COUNT(*) * 1.0 / (SELECT COUNT(DISTINCT player_id) FROM Activity),
        2
    ) AS fraction
FROM (
    SELECT player_id, MIN(event_date) AS first_date
    FROM Activity
    GROUP BY player_id
) f
WHERE EXISTS (
    SELECT 1
    FROM Activity a
    WHERE a.player_id = f.player_id
    AND a.event_date = f.first_date + INTERVAL '1 day'
);