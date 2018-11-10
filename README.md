# StackBehavior
Data Analysis project for analyzing questions, answers, comments and overall user's behavior on the StackOverflow site.

## Objectives
### Comments' Positive and Negative context
Analyze user behavior based on the positive and negative context of the comments. Such as `+1`, `Thanks!` are considered to be positive, `-1`, `Possible duplicate of` (State the low quality of question) are considered to be negative.

**Example** - What is the ratio of positive, negative and neutral comments?

### Languages popularity
Analyze languages popularity by tag(s) defined in questions. Such as `angular`, `c#` and other programming related tags.

**Example** - What is the most used language out of all question asked?

### User Participations
Analyze user participation using user's acquired badges.

**Example** - Out of all users, How many percentages of users have asked good questions? (From `Nice Question` badge)


## Data Sources
#### [StackExchange Public DataSet - StackOverflow](https://archive.org/download/stackexchange)
* **`badges`** - Acquired badges  - 1.19 GB
* **`comments`** - Posted Comments - 12.01 GB
* **`post_questions`** - Submitted Question - 25.10 GB
* **`post_answers`** - Submitted Answer - 20.17 GB
* **`tags`** - Used tags in questions - 2.08 MB
* **`users`** - User's info - 1.4 GB
##### Total Size - 59.87 GB

## Built-With
* Python `3.7.0`
    * pygal `2.0.0`
* Google BigQuery

## Authors
* นายภูวทิตต์ สัมมาวิวัฒน์ - 61070173 - [phwt](https://github.com/phwt)
* นายวีรพงศ์ ทันจันทึก - 61070213 - [veerapong76](https://github.com/veerapong76)
* นายณภัทร พรบุญเรือง - 61070044 - [61070044](https://github.com/61070044)
* นายสหัสวรรษ หิรัญเพชร - 61070239 - [maizerocom](https://github.com/maizerocom)

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com) 
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
