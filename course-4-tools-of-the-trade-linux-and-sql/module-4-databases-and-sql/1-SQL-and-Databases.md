## Module 4.1: SQL and Databases

## Introduction to Databases

## Overview

- A database is an organized collection of:
  - Information
  - Data

- Databases help store large amounts of data so it is:
  - Organized
  - Easy to access
  - Fast to process

- Security analysts regularly work with databases to investigate and manage security-related information

## Databases vs Spreadsheets

### Spreadsheets

Examples:

- Google Sheets
- Microsoft Excel

- Best for:
  - Single users
  - Small teams
  - Smaller amounts of data

### Databases

- Better for:
  - Large organizations
  - Enterprise systems
  - Security operations

- Can:
  - Store massive amounts of data
  - Support multiple users at once
  - Perform complex operations efficiently

## Relational Databases

## Overview

- A relational database stores data in:
  - Related tables

- Data is organized into:
  - Rows
  - Columns

- Relationships between tables improve:
  - Organization
  - Efficiency
  - Data retrieval

### Tables

- A table stores related information

Example:

- Employee information table

### Columns (Fields)

- Columns are also called:
  - Fields

- Represent categories of information

Example fields:

- `employee_id`
- `device_id`
- `username`

### Rows (Records)

- Rows are also called:
  - Records

- Each row contains a specific set of related data

## Keys in Relational Databases

### Primary Key

- A primary key:
  - Uniquely identifies each row
  - Cannot contain duplicates
  - Cannot contain empty values

Example:

- `employee_id`

### Foreign Key

- A foreign key:
  - Connects one table to another
  - References a primary key from another table

- Foreign keys:
  - Can contain duplicates
  - Can contain empty values

### Connecting Tables

- Tables can share fields to create relationships

Example:

- Employees table connected to Machines table through:
  - `employee_id`

## SQL (Structured Query Language)

## Overview

- SQL is a programming language used to:
  - Create databases
  - Interact with databases
  - Retrieve information

- Used heavily in:
  - Cybersecurity
  - Data analytics
  - System administration

### What is a Query?

- A query is a request for information from:
  - One table
  - Multiple tables

- Queries help retrieve specific information quickly

## SQL in Cybersecurity

### Logs

- A log is a record of events occurring within:
  - Systems
  - Applications
  - Networks

- Security analysts analyze logs to:
  - Detect suspicious activity
  - Investigate incidents
  - Monitor systems

### Using SQL for Security Analysis

- SQL helps analysts:
  - Search through large datasets
  - Analyze login attempts
  - Investigate unusual activity
  - Detect malicious behavior

### Handling Large Data Sets

- Security logs may contain:
  - Millions of records

- SQL allows analysts to:
  - Filter data quickly
  - Return relevant results efficiently

## SQL Filtering vs Linux Filtering

### Linux Filtering

- Uses commands like:
  - `grep`
  - Pipes (`|`)

- Commonly used for:
  - File searching
  - Log filtering in Linux systems

### SQL Filtering

- Uses SQL queries to filter information inside databases
- Better for:
  - Structured relational data
  - Large enterprise datasets

### Common SQL Filtering Uses

- Finding devices missing patches
- Identifying suspicious login activity
- Searching user records
- Investigating incidents

## Cybersecurity Importance

### Why SQL Matters

- SQL helps security analysts:
  - Investigate threats faster
  - Analyze system activity
  - Process large amounts of data efficiently

- SQL is an essential cybersecurity skill

## Key Takeaways

- Databases organize and store large amounts of data efficiently
- Relational databases use tables connected through keys
- Primary keys uniquely identify records, while foreign keys connect tables
- SQL is used to interact with relational databases and retrieve information
- Security analysts use SQL to analyze logs and investigate incidents
- SQL filtering is essential for working with large cybersecurity datasets

## Big Picture

- Databases and SQL allow cybersecurity professionals to efficiently store, search, filter, and analyze massive amounts of security data
- Understanding relational databases and SQL queries is essential for investigations, monitoring, and incident response
