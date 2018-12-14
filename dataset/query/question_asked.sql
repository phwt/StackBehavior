SELECT
    EXTRACT(MONTH FROM creation_date) as month, COUNT(*) AS total
FROM `bigquery-public-data.stackoverflow.posts_questions`
GROUP BY month
ORDER BY month