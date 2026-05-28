## Module 4.5: Review – Databases and SQL

## Databases and SQL Review

## Overview

- This module introduced the fundamentals of:
  - Databases
  - SQL (Structured Query Language)

- SQL allows analysts to:
  - Retrieve data
  - Filter information
  - Join tables
  - Analyze large datasets

- These skills are widely used in cybersecurity investigations and reporting

## Databases

### What is a Database?

- A database is an organized collection of data

- Databases help organizations:
  - Store information
  - Access information efficiently
  - Manage large amounts of data

### Relational Databases

- Relational databases organize data into:
  - Tables
  - Rows
  - Columns

- Tables can be connected using:
  - Primary keys
  - Foreign keys

### Benefits of Databases

- Store large amounts of information
- Support multiple users
- Allow efficient searching and analysis
- Improve data organization

## SQL Fundamentals

### What is SQL?

- SQL stands for:
  - Structured Query Language

- SQL is used to:
  - Query databases
  - Retrieve information
  - Update records
  - Analyze stored data

### Basic Query Structure

```sql
SELECT column_name
FROM table_name;
```

- `SELECT`
  - Chooses the data to display

- `FROM`
  - Specifies the table containing the data

## Filtering Data

### WHERE Clause

- The `WHERE` clause filters records

Example:

```sql
SELECT *
FROM employees
WHERE department = 'Finance';
```

### Comparison Operators

- Common operators:
  - `=`
  - `>`
  - `<`
  - `>=`
  - `<=`
  - `!=`

- Used to compare:
  - Numbers
  - Dates
  - Text values

### Logical Operators

- Combine multiple conditions using:
  - `AND`
  - `OR`
  - `NOT`

#### AND

- All conditions must be true

Example:

```sql
SELECT *
FROM employees
WHERE department = 'Finance'
AND office = 'East-170';
```

#### OR

- At least one condition must be true

Example:

```sql
SELECT *
FROM employees
WHERE department = 'Finance'
OR department = 'Sales';
```

#### NOT

- Excludes matching records

Example:

```sql
SELECT *
FROM employees
WHERE NOT department = 'Information Technology';
```

## SQL Joins

### Purpose of Joins

- Joins combine data from multiple tables

- Useful when information is stored across:
  - Related tables

### Primary and Foreign Keys

- Primary key:
  - Uniquely identifies a row

- Foreign key:
  - Connects one table to another

### INNER JOIN

- Returns only matching records from both tables

Example:

```sql
SELECT *
FROM employees
INNER JOIN machines
ON employees.employee_id = machines.employee_id;
```

### LEFT JOIN

- Returns:
  - All rows from the left table
  - Matching rows from the right table

### RIGHT JOIN

- Returns:
  - All rows from the right table
  - Matching rows from the left table

### FULL OUTER JOIN

- Returns:
  - All rows from both tables

- Missing values appear as:

```sql
NULL
```

## SQL in Cybersecurity

### Common Uses

- Investigating login attempts
- Reviewing employee records
- Tracking devices
- Finding vulnerable systems
- Connecting users to machines
- Analyzing security events

### Benefits for Security Analysts

- Quickly search large datasets
- Identify suspicious activity
- Generate reports
- Support incident investigations

## Key Takeaways

- Databases organize and store large amounts of information
- SQL is used to retrieve, filter, and analyze data
- The `WHERE` clause filters records using conditions
- `AND`, `OR`, and `NOT` help build complex filters
- Joins combine related information from multiple tables
- SQL is an essential skill for cybersecurity analysts

## Big Picture

- Databases contain valuable organizational and security data, while SQL provides the tools needed to access and analyze that information
- By learning queries, filters, and joins, cybersecurity professionals can efficiently investigate incidents, identify vulnerabilities, and make data-driven security decisions
