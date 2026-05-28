## Module 4.3: More SQL Filters

## Filter Dates and Numbers

## Overview

- SQL filters can also be applied to:
  - Numeric data
  - Date and time data

- Security analysts commonly filter:
  - Login attempts
  - Patch dates
  - Activity times

- SQL operators help retrieve specific records involving:
  - Numbers
  - Dates
  - Times

## Common SQL Data Types

### String Data

- String data consists of:
  - Ordered sequences of characters

- Can include:
  - Letters
  - Numbers
  - Symbols

Example:

```sql id="xtx1yi"
'analyst10'
```

### Numeric Data

- Numeric data consists of:
  - Numbers

- Mathematical operations can be performed on numeric data

Example:

- Number of login attempts

### Date and Time Data

- Represents:
  - Dates
  - Times
  - Or both together

- Commonly used in cybersecurity to:
  - Track activity
  - Analyze system events
  - Monitor patch installation dates

## Filtering Numeric and Date Data

### Overview

- Analysts may filter:
  - Machines needing updates
  - Login attempts during suspicious times
  - Events within a time range

## Common SQL Operators

### Comparison Operators

| Operator | Meaning |
|---|---|
| `=` | Equal to |
| `>` | Greater than |
| `<` | Less than |
| `!=` | Not equal to |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

### Greater Than Operator Example

```sql id="ycdbqr"
SELECT *
FROM log_in_attempts
WHERE time > '18:00';
```

- Returns login attempts made after:
  - 6:00 PM

- Useful for identifying:
  - Suspicious after-hours activity

## BETWEEN Operator

### Overview

- `BETWEEN` filters for:
  - Numbers or dates within a range

- Commonly used when:
  - Searching between two dates
  - Finding records within a time frame

### BETWEEN Example

```sql id="t14j2r"
SELECT *
FROM machines
WHERE OS_patch_date
BETWEEN '2021-03-01' AND '2021-09-01';
```

- Returns machines patched between:
  - March 1, 2021
  - September 1, 2021

### Structure of BETWEEN

- Components include:
  - Column name
  - `BETWEEN`
  - Starting value
  - `AND`
  - Ending value

## Quotation Marks in SQL

### Used With

- Strings
- Dates
- Times

### Examples

```sql id="zh1a9o"
'18:00'
'2021-03-01'
```

### Numeric Values

- Numbers do NOT use quotation marks

Example:

```sql id="5a4h13"
WHERE attempts > 5
```

## Filters with AND, OR, and NOT

## Overview

- SQL allows users to filter queries using:
  - Multiple conditions

- Common operators include:
  - `AND`
  - `OR`
  - `NOT`

- These operators help analysts:
  - Investigate vulnerabilities
  - Search for affected systems
  - Filter security-related data efficiently

## AND Operator

### Overview

- `AND` specifies that:
  - Both conditions must be true simultaneously

- Returns only records matching:
  - Every condition

### AND Example

```sql id="p6j2v0"
SELECT *
FROM machines
WHERE operating_system = 'OS 1'
AND email_client = 'Email Client 1';
```

- Returns machines running:
  - `OS 1`
  - AND `Email Client 1`

### How AND Works

- Similar to selecting:
  - Large AND fresh apples

- Both conditions must be satisfied

## OR Operator

### Overview

- `OR` specifies that:
  - Either condition can be true

- Records may satisfy:
  - One condition
  - Or both conditions

### OR Example

```sql id="5z3mf4"
SELECT *
FROM machines
WHERE operating_system = 'OS 1'
OR operating_system = 'OS 3';
```

- Returns machines running:
  - `OS 1`
  - OR `OS 3`

### How OR Works

- Returns a broader set of results

- Useful when:
  - Multiple values need the same action

## NOT Operator

### Overview

- `NOT` negates a condition

- Returns records that:
  - Do NOT match the specified condition

### NOT Example

```sql id="kcl25k"
SELECT *
FROM machines
WHERE NOT operating_system = 'OS 3';
```

- Returns all machines NOT running:
  - `OS 3`

### How NOT Works

- Useful for:
  - Excluding specific values

## Combining Filters in Cybersecurity

### Common Uses

- Security analysts use these operators to:
  - Find vulnerable machines
  - Identify affected systems
  - Filter login activity
  - Investigate incidents efficiently

### Venn Diagram Concept

- `AND`
  - Intersection of conditions

- `OR`
  - All matching conditions combined

- `NOT`
  - Everything outside the specified condition

## Key Takeaways

- SQL can filter numeric, date, and time data using operators
- Operators like `>`, `<`, and `BETWEEN` help retrieve precise results
- `BETWEEN` is useful for filtering ranges
- `AND`, `OR`, and `NOT` combine multiple conditions
- `AND` requires all conditions to be true
- `OR` allows either condition to be true
- `NOT` excludes records matching a condition
- These filters are essential for cybersecurity investigations and log analysis

## Big Picture

- Advanced SQL filtering allows cybersecurity professionals to efficiently search large databases for suspicious activity, vulnerable systems, login events, and security patterns
- Using operators like `BETWEEN`, `AND`, `OR`, and `NOT` helps analysts retrieve precise information quickly during investigations and monitoring
