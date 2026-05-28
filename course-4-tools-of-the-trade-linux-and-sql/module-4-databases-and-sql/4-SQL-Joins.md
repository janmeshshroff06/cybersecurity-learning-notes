## Module 4.4: SQL Joins

## Join Tables in SQL

## Overview

- SQL joins allow users to:
  - Combine information from multiple tables

- Joins are useful when data is stored across:
  - Different related tables

- Security analysts use joins to:
  - Investigate vulnerabilities
  - Match employees to devices
  - Analyze system information more efficiently

## Why Joins Are Important

### Multiple Related Tables

- Databases often separate information into:
  - Multiple related tables

Example:

- One table contains employee information
- Another table contains machine information

- Joins allow analysts to:
  - Combine these tables into one result

### Cybersecurity Example

- One table may contain:
  - Operating system vulnerabilities

- Another table may contain:
  - Company machines and operating systems

- Joining the tables helps identify:
  - Vulnerable machines within the organization

## Using Table Names with Columns

### Table.Column Format

- When working with multiple tables, SQL must know which table a column belongs to

Format:

```sql
table_name.column_name
```

Example:

```sql
employees.employee_id
```

### Why Table Names Matter

- Some columns may exist in multiple tables

Example:

- `employee_id` exists in both:
  - employees
  - machines

- Specifying the table prevents ambiguity

## Primary Keys and Foreign Keys

### Primary Key

- A primary key:
  - Uniquely identifies each row in a table

Requirements:

- Unique values
- No NULL values

Example:

```sql
employee_id
```

### Foreign Key

- A foreign key:
  - Connects one table to another

- Can contain:
  - Duplicate values
  - NULL values

Example:

```sql
employee_id
```

- In the machines table referencing the employees table

### NULL Values

- `NULL` represents:
  - Missing data
  - Empty values

Example:

- A machine not assigned to an employee

## INNER JOIN

### Overview

- `INNER JOIN` returns:
  - Only rows with matching values in both tables

- Nonmatching rows are excluded

### INNER JOIN Syntax

```sql
SELECT username, office, operating_system
FROM employees
INNER JOIN machines
ON employees.employee_id = machines.employee_id;
```

### Breaking Down the Query

#### SELECT

- Chooses the columns to display

#### FROM employees

- Sets the left table

#### INNER JOIN machines

- Adds the right table

#### ON

- Specifies the matching columns used for the join

### Left and Right Tables

- Table after `FROM`:
  - Left table

- Table after `INNER JOIN`:
  - Right table

### How INNER JOIN Works

- SQL compares matching values between tables

Example:

```text
employee_id = 1188
employee_id = 1189
```

- Only matching rows appear in the results

## Types of Joins

### Overview

- Different joins return different sets of records

Main join types:

- INNER JOIN
- LEFT JOIN
- RIGHT JOIN
- FULL OUTER JOIN

## LEFT JOIN

### Overview

- Returns:
  - All rows from the left table
  - Matching rows from the right table

- Rows without matches still appear

### LEFT JOIN Example

```sql
SELECT *
FROM employees
LEFT JOIN machines
ON employees.employee_id = machines.employee_id;
```

### How LEFT JOIN Works

- Matching rows are combined normally

- Unmatched rows from the left table:
  - Still appear in results

- Missing values become:

```sql
NULL
```

## RIGHT JOIN

### Overview

- Returns:
  - All rows from the right table
  - Matching rows from the left table

### RIGHT JOIN Example

```sql
SELECT *
FROM employees
RIGHT JOIN machines
ON employees.employee_id = machines.employee_id;
```

### How RIGHT JOIN Works

- Matching rows are combined normally

- Unmatched rows from the right table remain

- Missing values become:

```sql
NULL
```

## FULL OUTER JOIN

### Overview

- Returns:
  - All rows from both tables

- Includes:
  - Matching rows
  - Nonmatching rows from either table

### FULL OUTER JOIN Example

```sql
SELECT *
FROM employees
FULL OUTER JOIN machines
ON employees.employee_id = machines.employee_id;
```

### How FULL OUTER JOIN Works

- Every row from both tables is included

- Missing values are replaced with:

```sql
NULL
```

## Join Comparison

### INNER JOIN

- Only matching rows

### LEFT JOIN

- All rows from left table
- Matching rows from right table

### RIGHT JOIN

- All rows from right table
- Matching rows from left table

### FULL OUTER JOIN

- All rows from both tables

## Joins in Cybersecurity

### Common Uses

- Connect users to devices
- Match vulnerabilities to systems
- Investigate security incidents
- Analyze machine inventories
- Track employee-device assignments

## Key Takeaways

- SQL joins combine related data from multiple tables
- Primary keys and foreign keys are commonly used to connect tables
- `INNER JOIN` returns only matching records
- `LEFT JOIN`, `RIGHT JOIN`, and `FULL OUTER JOIN` can return nonmatching records
- `NULL` represents missing or unmatched data
- Joins are essential for cybersecurity investigations and database analysis

## Big Picture

- SQL joins allow analysts to connect information stored across multiple tables
- Makes it possible to investigate users, devices, vulnerabilities, and security events more efficiently
- Understanding when to use INNER, LEFT, RIGHT, and FULL OUTER joins is a fundamental database skill for cybersecurity professionals
