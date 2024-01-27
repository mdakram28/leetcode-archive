# Write your MySQL query statement below
-- SELECT del.order_date as order_date, del.customer_pref_delivery_date as customer_pref_delivery_date
-- from (
--     SELECT customer_id, MIN(order_date) as order_date
--     FROM Delivery
--     GROUP BY customer_id
-- ) as min_order_date LEFT JOIN Delivery as del
-- ON min_order_date.order_date = del.order_date and min_order_date.customer_id = del.customer_id;

SELECT ROUND(
    AVG(IF(order_date = customer_pref_delivery_date, 100.0, 0)),
    2) as immediate_percentage
FROM (
    
    SELECT del.order_date as order_date, del.customer_pref_delivery_date as customer_pref_delivery_date
    from (
        SELECT customer_id, MIN(order_date) as order_date
        FROM Delivery
        GROUP BY customer_id
    ) as min_order_date LEFT JOIN Delivery as del
    ON min_order_date.order_date = del.order_date and min_order_date.customer_id = del.customer_id

) as first_orders;