# SQL Reference Guide

A quick reference guide for commonly used SQL commands, filters, joins, and aggregate functions.

---

# Table of Contents

- Query a Database
- Apply Filters to SQL Queries
- Join Tables
- Perform Calculations

---

# Query a Database

The `SELECT`, `FROM`, and `ORDER BY` keywords are used when retrieving information from a database.

## `FROM`

Specifies which table to query.

### Examples

```sql
FROM employees;
```

Query the `employees` table.

---

## `ORDER BY`

Sorts records returned by a query.

### Examples

```sql
ORDER BY department;
```

Sort records in ascending order by department.

```sql
ORDER BY department ASC;
```

Sort records in ascending order by department.

```sql
ORDER BY city DESC;
```

Sort records in descending order by city.

```sql
ORDER BY country, city;
```

Sort first by country, then by city.

---

## `SELECT`

Specifies which columns to return.

### Examples

```sql
SELECT employee_id
FROM employees;
```

Return only the `employee_id` column.

```sql
SELECT *
FROM employees;
```

Return all columns.

---

# Apply Filters to SQL Queries

The `WHERE` clause and related operators are used to filter records.

## `WHERE`

Specifies a condition for filtering.

### Example

```sql
SELECT *
FROM employees
WHERE title = 'IT Staff';
```

Return employees whose title is `IT Staff`.

---

## `AND`

Requires both conditions to be true.

### Example

```sql
SELECT *
FROM employees
WHERE region = 5 AND country = 'USA';
```

Return records where both conditions are met.

---

## `OR`

Requires at least one condition to be true.

### Example

```sql
SELECT *
FROM employees
WHERE country = 'Canada' OR country = 'USA';
```

Return records from Canada or the USA.

---

## `BETWEEN`

Filters values within a range.

### Example

```sql
SELECT *
FROM employees
WHERE hiredate BETWEEN '2002-01-01' AND '2003-01-01';
```

Return records with hire dates in the specified range.

---

## `=` (Equal To)

### Example

```sql
SELECT *
FROM employees
WHERE birthdate = '1980-05-15';
```

Return records with an exact match.

---

## `>` (Greater Than)

### Example

```sql
SELECT *
FROM employees
WHERE birthdate > '1970-01-01';
```

Return records greater than the specified value.

---

## `>=` (Greater Than or Equal To)

### Example

```sql
SELECT *
FROM employees
WHERE birthdate >= '1965-06-30';
```

Return records greater than or equal to the specified value.

---

## `<` (Less Than)

### Example

```sql
SELECT *
FROM employees
WHERE date < '2023-01-31';
```

Return records less than the specified value.

---

## `<=` (Less Than or Equal To)

### Example

```sql
SELECT *
FROM employees
WHERE date <= '2020-12-31';
```

Return records less than or equal to the specified value.

---

## `NOT`

Negates a condition.

### Example

```sql
SELECT *
FROM employees
WHERE NOT country = 'Mexico';
```

Return records that are not from Mexico.

---

## `<>` (Not Equal To)

### Example

```sql
SELECT *
FROM employees
WHERE date <> '2023-02-28';
```

Return records not equal to the specified value.

---

## `!=` (Not Equal To)

### Example

```sql
SELECT *
FROM employees
WHERE date != '2023-05-14';
```

Alternative syntax for "not equal to."

---

## `LIKE`

Searches for a pattern.

### Examples

```sql
SELECT *
FROM employees
WHERE title LIKE 'IT%';
```

Return titles starting with `IT`.

```sql
SELECT *
FROM employees
WHERE state LIKE 'N_';
```

Return values matching `N` plus one character.

---

## `%` Wildcard

Represents zero or more characters.

### Examples

```sql
'a%'
```

Starts with `a`.

```sql
'%a'
```

Ends with `a`.

```sql
'%a%'
```

Contains `a`.

---

## `_` Wildcard

Represents exactly one character.

### Examples

```sql
'a_'
```

`a` followed by one character.

```sql
'a__'
```

`a` followed by two characters.

```sql
'_a'
```

One character followed by `a`.

```sql
'_a_'
```

One character before and after `a`.

---

# Join Tables

Joins combine data from multiple tables.

## `INNER JOIN`

Returns only matching rows from both tables.

### Example

```sql
SELECT *
FROM employees
INNER JOIN machines
ON employees.device_id = machines.device_id;
```

Return records with matching `device_id` values.

---

## `LEFT JOIN`

Returns all rows from the left table and matching rows from the right table.

### Example

```sql
SELECT *
FROM employees
LEFT JOIN machines
ON employees.device_id = machines.device_id;
```

Return all employees and matching machine records.

---

## `RIGHT JOIN`

Returns all rows from the right table and matching rows from the left table.

### Example

```sql
SELECT *
FROM employees
RIGHT JOIN machines
ON employees.device_id = machines.device_id;
```

Return all machines and matching employee records.

---

## `FULL OUTER JOIN`

Returns all rows from both tables.

### Example

```sql
SELECT *
FROM employees
FULL OUTER JOIN machines
ON employees.device_id = machines.device_id;
```

Return all records from both tables, matching where possible.

---

# Perform Calculations

Aggregate functions perform calculations on groups of records.

## `AVG()`

Returns the average value.

### Example

```sql
SELECT AVG(height)
FROM employees;
```

Return the average height.

---

## `COUNT()`

Returns the number of records.

### Example

```sql
SELECT COUNT(firstname)
FROM employees;
```

Return the number of non-null first names.

---

## `SUM()`

Returns the total sum.

### Example

```sql
SELECT SUM(cost)
FROM expenses;
```

Return the total cost.

---
