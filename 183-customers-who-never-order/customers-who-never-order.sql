# Write your MySQL query statement below
Select
c.Name as Customers
from
Customers c
    left join Orders o
    on c.ID=O.CustomerID
where o.ID is null;