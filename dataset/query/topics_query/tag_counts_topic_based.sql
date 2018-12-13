SELECT
    year, COUNT(*) AS total
FROM(
    WITH vars AS (SELECT 'java' AS topic)
    SELECT
        EXTRACT(YEAR FROM creation_date) AS year,
        CASE WHEN LOWER(tags) LIKE CONCAT("%", (SELECT topic FROM vars), "%") THEN (SELECT topic FROM vars) ELSE "" END
    FROM
        `bigquery-public-data.stackoverflow.posts_questions`
    WHERE
         tags LIKE CONCAT("%", (SELECT topic FROM vars), "%")
--          AND tags NOT LIKE "%javascript%"
)
GROUP BY year
ORDER BY year
