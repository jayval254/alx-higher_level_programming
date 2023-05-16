-- groups by scores
SELECT score, COUNT(name) number
FROM second_table
GROUP BY score
ORDER BY score DESC;
