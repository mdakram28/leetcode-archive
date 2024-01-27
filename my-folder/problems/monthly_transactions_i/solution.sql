# Write your MySQL query statement below

SELECT DATE_FORMAT(trans_date, "%Y-%m") as month, 
    country, 
    COUNT(amount) as trans_count, 
    SUM(amount) as trans_total_amount,
    SUM(IF(state = "approved", 1, 0)) as approved_total_amount,
    SUM(IF(state = "approved", amount, 0)) as approved_count
FROM Transactions
GROUP BY YEAR(trans_date), MONTH(trans_date), country