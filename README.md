# StackBehavior
Data Analysis project for analyzing questions, answers, comments and overall user's behavior on the StackOverflow site.

## Objectives
### Programming Topics' popularity over time
Analyze topics popularity by tag(s) defined in asked questions.

### Average user activity in a year
Analyze how time in a year affect user's activity on the site.

### Comments' Positive and Negative context
Analyze user behavior based on the positive and negative context of the comments.

## To-do
1. [ ] Query and download all required data.
   - [X] Topics
   - [ ] Users' Activity - *Working in Progress*
   - [ ] Comments' context - *Working in Progress*
2. [ ] Convert data into visualiztion-ready format.
   - [X] Topics
   - [ ] Users' Activity
   - [ ] Comments' context
3. [ ] Data Visualization
   - [ ] Topics - *Working in Progress*
   - [ ] Users' Activity
   - [ ] Comments' context
4. [ ] Presentation
   - [ ] Website - *Working in Progress*
   - [ ] Video

## Data Sources
#### [StackExchange Public DataSet - StackOverflow](https://archive.org/download/stackexchange)
* **`badges`** - Acquired badges  - 1.19 GB
* **`comments`** - Posted Comments - 12.01 GB
* **`post_questions`** - Submitted Question - 25.10 GB
* **`post_answers`** - Submitted Answer - 20.17 GB
* **`tags`** - Used tags in questions - 2.08 MB
* **`users`** - User's info - 1.4 GB
##### Data Range - 2008 Q3 - 2018 Q3* (10 Years)
##### Total Size - 59.87 GB
\* 2018 Q4 Data is excluded because of incomplete data.

## Built-With
* Python `3.7.0`
    * pygal `2.0.0`
* Google Cloud Platform
    * BigQuery
    * Storage

## Authors
* นายภูวทิตต์ สัมมาวิวัฒน์ - 61070173 - [phwt](https://github.com/phwt)
* นายวีรพงศ์ ทันจันทึก - 61070213 - [veerapong76](https://github.com/veerapong76)
* นายณภัทร พรบุญเรือง - 61070044 - [61070044](https://github.com/61070044)
* นายสหัสวรรษ หิรัญเพชร - 61070239 - [maizerocom](https://github.com/maizerocom)

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com) 
