-- script for listing avg temp per city
-- DML query for listing
SELECT city,avg_temp FROM (SELECT city,
 AVG(value) AS avg_temp
 FROM temperatures
 GROUP BY city
 ORDER BY AVG(value) DESC) results LIMIT 3;
