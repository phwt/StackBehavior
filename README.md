[**EN**/[TH](https://github.com/phwt/StackBehavior/blob/master/README_th.md)]

# StackBehavior
Data Analysis project for analyzing questions, answers, comments and overall user's behavior on the Stack Overflow site.

*This project is a part of Problem Solving in Information Technology (06016314) - King Mongkut's Institute of Technology Ladkrabang*

## Topics
### Programming Topics' popularity over the years
Analyze topics popularity by tag(s) defined in asked questions.

### Comments' Positive and Negative context
Analyze user behavior based on the positive and negative context of the comments.

### Average user activity in a year
Analyze how time in a year affect user's activity on the site.

## Results
* [View on our site](https://phwt.github.io/StackBehavior/)
* [View on YouTube](https://www.youtube.com/watch?v=0eT0Aw0En2s)

## Data Sources
#### [StackExchange Public DataSet - StackOverflow](https://archive.org/download/stackexchange)
* `badges` - Acquired badges  - 1.19 GB
* `comments` - Posted Comments - 12.01 GB
* `post_questions` - Submitted Question - 25.10 GB
* `post_answers` - Submitted Answer - 20.17 GB
* `tags` - Used tags in questions - 2.08 MB
* `users` - User's info - 1.4 GB

**Data Range** - 2008 - 2018

**Total Size** - 59.87 GB (Estimated)

## Built-With
* Python `3.7.0`
    * pygal `2.4.0`
* Google Cloud Platform
    * BigQuery
    
## Development Setup
Install the required library

    pip install pygal
    
### Directory Structure
* `dataset`
  * `data` - Raw and converted data
  * `query` - BigQuery query method
* `convert` - Python files for converting raw data into visualization ready format
* `visualize` - Python files for data visualization
* `docs` - Project's site

**Notes** - All the path is set to relative to the project's root directory. (`./StackBehavior/...`)

## Authors
* นายภูวทิตต์ สัมมาวิวัฒน์ - 61070173 - [phwt](https://github.com/phwt)
* นายวีรพงศ์ ทันจันทึก - 61070213 - [veerapong76](https://github.com/veerapong76)
* นายณภัทร พรบุญเรือง - 61070044 - [61070044](https://github.com/61070044)
* นายสหัสวรรษ หิรัญเพชร - 61070239 - [maizerocom](https://github.com/maizerocom)

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com) 
