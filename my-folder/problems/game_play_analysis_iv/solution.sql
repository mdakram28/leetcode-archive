# Write your MySQL query statement below
SELECT ROUND(AVG(IF(a2.event_date IS NULL, 0, 1)),2) as fraction
-- SELECT *
FROM (
    SELECT player_id, MIN(event_date) as event_date
    FROM Activity
    GROUP BY player_id
) as first
LEFT JOIN Activity as a2
ON first.player_id = a2.player_id and a2.event_date = DATE_ADD(first.event_date, INTERVAL +1 DAY)