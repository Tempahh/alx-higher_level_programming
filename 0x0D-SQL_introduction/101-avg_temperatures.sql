--AUTHOR: Orjiogo Chinedu

SELECT city, AVG(value) as avg_temp FROM temperatures GROUP BY city ORDER BY value DESC 