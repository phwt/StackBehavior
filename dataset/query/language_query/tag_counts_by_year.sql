SELECT
    tags, COUNT(*) AS total
FROM (
    SELECT
        tags, creation_date,
    CASE
        WHEN LOWER(tags) LIKE "%android%" THEN "android"
        WHEN LOWER(tags) LIKE "%angular%" THEN "angular"
        WHEN LOWER(tags) LIKE "%c#%" THEN "c#"
        WHEN LOWER(tags) LIKE "%c++%" THEN "c++"
        WHEN LOWER(tags) LIKE "%html%" THEN "html"
        WHEN LOWER(tags) LIKE "%ios%" THEN "ios"
        WHEN LOWER(tags) LIKE "%iphone%" THEN "iphone"
        WHEN LOWER(tags) LIKE "%java%" THEN "java"
        WHEN LOWER(tags) LIKE "%javascript%" THEN "javascript"
        WHEN LOWER(tags) LIKE "%jquery%" THEN "jquery"
        WHEN LOWER(tags) LIKE "%php%" THEN "php"
        WHEN LOWER(tags) LIKE "%python%" THEN "python"
        WHEN LOWER(tags) LIKE "%sql%" THEN "sql"
        WHEN LOWER(tags) LIKE "%swift%" THEN "swift"
        WHEN LOWER(tags) LIKE "%windows%" THEN "windows"
        WHEN LOWER(tags) LIKE "%wordpress%" THEN "wordpress"
        WHEN LOWER(tags) LIKE "%xcode%" THEN "xcode"
        ELSE tags
    END
    FROM
        `bigquery-public-data.stackoverflow.posts_questions`
    WHERE
        EXTRACT(YEAR FROM creation_date) = 2008 AND
        EXTRACT(QUARTER FROM creation_date) = 1
)
WHERE
  tags IN ('android', 'angular', 'c#', 'c++', 'html', 'ios', 'iphone', 'java', 'javascript', 'jquery', 'php', 'python', 'sql', 'swift', 'windows', 'wordpress', 'xcode')
GROUP BY tags