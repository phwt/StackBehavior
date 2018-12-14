SELECT
    year, month, total
FROM(
    SELECT
        EXTRACT(YEAR FROM creation_date) as year,
        EXTRACT(MONTH FROM creation_date) as month,
        COUNT(*) AS total
    FROM
        `bigquery-public-data.stackoverflow.users`
    GROUP BY year, month
    ORDER BY year, month
)
GROUP BY year, month, total
ORDER BY year, month