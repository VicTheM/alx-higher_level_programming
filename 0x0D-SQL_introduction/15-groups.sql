-- counts duplicates

SELECT score, COUNT(name) AS number
FROM second_table
GROUP BY score;
