# Write your MySQL query statement below
SELECT e2.name as name
FROM (
    SELECT managerId
    FROM Employee
    WHERE managerId IS NOT  NULL
    GROUP BY managerId
    HAVING COUNT(id) >= 5
) as e1 INNER JOIN Employee as e2
ON e1.managerId = e2.id;