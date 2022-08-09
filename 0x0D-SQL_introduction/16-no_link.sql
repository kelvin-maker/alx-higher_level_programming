-- sort records in second_table where name is non-null
SELECT `score`, `name`
FROM `second_table`
WHERE `name` IS NOT NULL
ORDER BY `score` DESC;
