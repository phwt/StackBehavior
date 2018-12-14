SELECT
    year,
    SUM(CASE WHEN context = "Positive Context" THEN 1 ELSE 0 END) pos_count,
    SUM(CASE WHEN context = "Negative Context" THEN 1 ELSE 0 END) neg_count,
    COUNT(*) as total
FROM(
    SELECT
        CASE
            WHEN REGEXP_CONTAINS(LOWER(text), "thanks|you're welcome|no problem|good answer|good question|appreciate|good idea|i think this may it be helpful|try this repository|can be found at this link|that's working thanks|thanks for your reply|hope this helps|thanks for the detailed|answer here is good|nothing impossible|answer your question|your answer is pretty good|i have to agree|that's helpful thanks|seriously appreciate the help|this is different question|i like this answer|thanks for the reply|i was looking for that") 
            OR LOWER(text) LIKE "%+rep%" THEN "Positive Context"
            WHEN REGEXP_CONTAINS(LOWER(text), "possible duplicate of|google it|please google|asked before|is this homework|already has an answer|nothing much to share|troll|off-topic|downvote|talk to your client|stupid|stupid requirement|should be deleted|silly question|noob|unclear what you're asking|what you mean|what do you mean|can you clarify|still unclear|not helpful|i hate to|waste of my time|you won’t listen|self explanatory|i have already told") 
            OR LOWER(text) LIKE "%-rep%" THEN "Negative Context"
            ELSE ""
        END AS context,
        EXTRACT(YEAR FROM creation_date) as year
    FROM `bigquery-public-data.stackoverflow.comments`
)
GROUP BY year
ORDER BY year