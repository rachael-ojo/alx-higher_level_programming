-- List namba yema records with same_score in 'second_table'

SELECT score, COUNT (1) AS number FROM second_table
GROUP BY Score
ORDER BY number DESC;