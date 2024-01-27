# Write your MySQL query statement below


SELECT Signups.user_id as user_id, ROUND(IFNULL(conf.confirmation_rate, 0), 2) as confirmation_rate
FROM Signups LEFT JOIN (
    SELECT user_id, AVG(CASE 
        WHEN action = "confirmed" THEN 1
        WHEN action = "timeout" THEN 0
        END) as confirmation_rate
    FROM Confirmations
    GROUP BY user_id
) as conf ON Signups.user_id = conf.user_id
