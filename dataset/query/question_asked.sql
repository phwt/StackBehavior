SELECT
    total
FROM(
    SELECT
        EXTRACT(YEAR FROM creation_date) as year,
        EXTRACT(MONTH FROM creation_date) as month,
        COUNT(*) AS total
    FROM
        `bigquery-public-data.stackoverflow.posts_questions`
    WHERE EXTRACT(YEAR FROM creation_date) = 2017
    GROUP BY year, month
    ORDER BY year, month
)
GROUP BY total