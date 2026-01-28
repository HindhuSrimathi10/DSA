# Write your MySQL query statement below
SELECT DISTINCT d.Num ConsecutiveNums FROM Logs d
JOIN Logs b ON d.Id  = b.Id + 1 AND d.Num=b.Num
JOIN Logs c ON d.Id =c.Id + 2 AND d.Num=c.Num