-- list all records of the table second_table
SELECT `score`, COUNT(*) AS number
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
