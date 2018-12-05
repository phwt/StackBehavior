SELECT
    year, quarter, COUNT(*) AS total
FROM(
    WITH vars AS (SELECT 'python' AS topic)
    SELECT
        EXTRACT(YEAR FROM creation_date) AS year,
        EXTRACT(QUARTER FROM creation_date) AS quarter,
        CASE WHEN LOWER(tags) LIKE CONCAT("%", (SELECT topic FROM vars), "%") THEN (SELECT topic FROM vars) ELSE "" END
    FROM
        `bigquery-public-data.stackoverflow.posts_questions`
    WHERE
         tags LIKE CONCAT("%", (SELECT topic FROM vars), "%")
)
GROUP BY year, quarter
ORDER BY year, quarter
