SELECT
    EXTRACT(YEAR FROM creation_date) AS year,
    EXTRACT(QUARTER FROM creation_date) AS quarter,
    COUNT(*) AS total
FROM
    `bigquery-public-data.stackoverflow.posts_questions`
GROUP BY year, quarter
ORDER BY year, quarter
