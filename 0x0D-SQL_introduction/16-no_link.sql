-- Skips NULL values

SELECT score, name FROM second_table
where score IS NOT NULL AND
name IS NOT NULL
ORDER BY score DESC;
