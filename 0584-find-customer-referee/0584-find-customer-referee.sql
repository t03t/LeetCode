# Write your MySQL query statement below
SELECT name from Customer where (referee_id IS NULL or referee_id != 2)