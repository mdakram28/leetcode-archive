# Write your MySQL query statement below
SELECT Product.product_name as product_name, Sales.year as year, Sales.price as price
FROM Sales LEFT JOIN Product
ON Sales.product_id = Product.product_id;