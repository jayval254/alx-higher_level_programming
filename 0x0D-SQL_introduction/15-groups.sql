-- groups by scores
SELECT score, COUNT(score) AS number FROM second_table
    GROUP BY score DESC;
