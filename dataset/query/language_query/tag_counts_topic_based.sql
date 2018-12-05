SELECT
    year, quarter, COUNT(*) AS total
FROM(
    SELECT
        EXTRACT(YEAR FROM creation_date) AS year,
        EXTRACT(QUARTER FROM creation_date) AS quarter,
        CASE WHEN LOWER(tags) LIKE "%python%" THEN "python" ELSE "" END
    FROM
        `bigquery-public-data.stackoverflow.posts_questions`
    WHERE
         tags LIKE "%python%"
)
GROUP BY year, quarter
ORDER BY year, quarter
