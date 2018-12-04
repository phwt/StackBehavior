SELECT
    tags, COUNT(*) AS total
FROM (
    SELECT
        tags, creation_date,
    CASE
        WHEN LOWER(tags) LIKE "%python%" THEN "python"
        WHEN LOWER(tags) LIKE "%javascript%" THEN "javascript"
        WHEN LOWER(tags) LIKE "%java%" THEN "java"
        WHEN LOWER(tags) LIKE "%c#%" THEN "c#"
        WHEN LOWER(tags) LIKE "%php%" THEN "php"
        WHEN LOWER(tags) LIKE "%html%" THEN "html"
        WHEN LOWER(tags) LIKE "%c++%" THEN "c++"
        ELSE tags
    END
    FROM
        `bigquery-public-data.stackoverflow.posts_questions`
    WHERE
        EXTRACT(YEAR FROM creation_date) = 2008 AND
        EXTRACT(QUARTER FROM creation_date) = 1
)
WHERE
  tags IN ('python', 'javascript', 'java', 'c#', 'php', 'html', 'c++')
GROUP BY tags