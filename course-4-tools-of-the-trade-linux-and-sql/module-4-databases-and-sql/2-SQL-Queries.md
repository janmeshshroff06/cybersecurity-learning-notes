## Module 4.2: SQL Queries

## Basic Queries

## Overview

- SQL queries are used to retrieve information from:
  - Database tables

- Security analysts use queries to:
  - Investigate systems
  - Analyze logs
  - Retrieve employee or machine information

- Basic SQL queries commonly use:
  - `SELECT`
  - `FROM`

## What is a Query?

### Definition

- A query is a request for information from a database

- Queries allow users to:
  - Retrieve specific data quickly
  - Filter and analyze information

## SELECT and FROM

### SELECT Keyword

- `SELECT` specifies:
  - Which columns should be returned in the output

- Used to retrieve particular information from a table

### FROM Keyword

- `FROM` specifies:
  - Which table the information comes from

- Identifies the database table being queried

### Basic Query Structure

```sql
SELECT employee_id, device_id
FROM employees;
```

- This query:
  - Retrieves the `employee_id` column
  - Retrieves the `device_id` column
  - Pulls information from the `employees` table

### Commas in SQL Queries

- Multiple columns are separated using:
  - Commas

### Semicolons in SQL

- SQL statements commonly end with:
  - A semicolon (`;`)

- Indicates:
  - The end of the SQL statement

## SQL Syntax

### Overview

- Syntax refers to:
  - The rules that determine correct structure in a programming language

- SQL queries must follow proper syntax to run successfully

### Case Sensitivity

- SQL keywords are generally:
  - Not case-sensitive

Example:

```sql
SELECT
select
```

- Both are valid

- Capitalizing keywords improves:
  - Readability
  - Organization

## Selecting All Columns

### Asterisk (*)

- An asterisk (`*`) returns:
  - All columns from a table

### SELECT All Example

```sql
SELECT *
FROM employees;
```

- Returns:
  - Every column
  - Every row
  - From the `employees` table

## Basic Filters on SQL Queries

### Overview

- Filtering allows users to:
  - Select only specific pieces of data from a database

- Security analysts use filtering to:
  - Investigate logs
  - Analyze suspicious activity
  - Retrieve precise information quickly

## The WHERE Clause

### Overview

- `WHERE` specifies:
  - The condition for a filter

- Used after:
  - `SELECT`
  - `FROM`

### Basic WHERE Example

```sql
SELECT *
FROM log_in_attempts
WHERE country = 'USA';
```

- This query:
  - Selects all columns
  - From the `log_in_attempts` table
  - Returns only rows where `country` equals `USA`

## Operators in SQL

### Equal To Operator (=)

- Used to find records matching:
  - An exact value

### Example

```sql
country = 'USA'
```

- Returns records where:
  - The country value is exactly `USA`

## Pattern Matching

### Overview

- SQL can filter using:
  - Patterns instead of exact values

- Useful when:
  - Data is inconsistent
  - Similar values exist

### Wildcard (%)

- The percentage sign (`%`) acts as a:
  - Wildcard

- Represents:
  - Unspecified characters

### Wildcard Example

```sql
'East%'
```

- Returns values beginning with:
  - `East`

Example matches:

- `East-120`
- `East-290`
- `East-435`

## LIKE Operator

### Overview

- `LIKE` is used with:
  - `WHERE`

- Searches for patterns in a column

### LIKE Example

```sql
SELECT *
FROM log_in_attempts
WHERE country LIKE 'US%';
```

- Returns records where:
  - Country values begin with `US`

Example matches:

- `US`
- `USA`

## SQL Filtering vs Linux Filtering

### SQL Filtering

- Filters structured database information
- Used for:
  - Tables
  - Records
  - Relational data

### Linux Filtering

- Uses commands like:
  - `grep`
  - Pipes (`|`)

- Used for:
  - Text files
  - Logs
  - Command-line output

## Cybersecurity Importance

### Why SQL Queries Matter

- Security analysts use SQL queries to:
  - Search logs
  - Investigate incidents
  - Analyze suspicious activity
  - Retrieve security-related information quickly

### Benefits of SQL Filtering

- Helps analysts:
  - Reduce unnecessary data
  - Search large datasets efficiently
  - Investigate threats faster

## Key Takeaways

- SQL queries retrieve information from database tables
- `SELECT` specifies which columns to return
- `FROM` specifies which table to query
- `WHERE` filters records based on conditions
- `LIKE` and `%` help search for patterns
- SQL filtering is essential for cybersecurity investigations and data analysis
- Understanding SQL queries is an important skill for security analysts

## Big Picture

- SQL queries allow cybersecurity professionals to efficiently retrieve, filter, and analyze large amounts of database information
- Commands like `SELECT`, `FROM`, `WHERE`, and `LIKE` are foundational skills for working with security logs, investigations, and enterprise data systems
