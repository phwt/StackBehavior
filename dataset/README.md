* **Data** - Contains exported data in .csv format.
* **Query** - Contains keyword use to query data or a method used to query data.

## Dataset Schema

Notes - Some column are excluded and self-explained column will left blanks.

* **`badges`**
    * `name`
    * `date`
    * `user_id` - Recipients' ID
* **`comments`**
    * `text`
    * `creation_date`
    * `post_id` - Comment's origin post's ID
    * `user_id`
    * `score` - Comment's score (Min = 0; Comment cannot be down-voted)
* **`post_questions`**
    * `title`
    * `body`
    * `accepted_answer_id` - Accepted answer's post ID
    * `answer_count`
    * `comment_count`
    * `creation_date`
    * `favorite_count` - Amount of user marked this question as favorite
    * `last_activity_date`
    * `last_edit_date`
    * `last_editor_user_id`
    * `owner_user_id`
    * `score`
    * `tags` - Questions's tags (Separated by "|" for multiple tags)
    * `view_count`
* **`post_answers`**
    * `body`
    * `comment_count`
    * `creation_date`
    * `last_activity_date`
    * `last_edit_date`
    * `last_editor_user_id`
    * `owner_user_id`
    * `parent_id` - Question ID
    * `score`
* **`tags`**
    * `tag_name`
    * `count`
* **`users`**
    * `display_name`
    * `about_me`
    * `creation_date`
    * `last_access_date`
    * `location`
    * `reputation`
    * `up_votes`
    * `down_votes`
    * `views`
