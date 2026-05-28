# Linux & SQL Security Investigation Toolkit

## Overview

A beginner cybersecurity project that uses Linux log analysis and SQL queries to investigate authentication activity, failed login attempts, successful user logins, and suspicious IP addresses. The project demonstrates how security analysts can collect, store, and analyze authentication logs using Linux, Python, SQLite, and SQL.

## Features

* Analyze Linux authentication logs
* Detect failed SSH login attempts
* Track successful user logins
* Store log events in a SQLite database
* Run SQL queries for security investigations
* Generate a security investigation report

## Project Structure

```text
linux-sql-security-toolkit/
├── logs/
│   └── auth.log
├── database/
│   └── security.db
├── scripts/
│   ├── load_logs.py
│   └── analyze.py
├── queries/
│   ├── failed_logins.sql
│   ├── suspicious_users.sql
│   └── recent_logins.sql
├── README.md
└── report.md
```

## Technologies Used

* Linux
* Python
* SQLite
* SQL
* Regular Expressions
* Cybersecurity Log Analysis

## How to Run

```bash
python3 scripts/load_logs.py
python3 scripts/analyze.py
```

## Example Linux Commands

### View Authentication Logs

```bash
grep "Failed password" logs/auth.log
```

### Search for Successful Logins

```bash
grep "Accepted password" logs/auth.log
```

### Locate Log Files

```bash
find /var/log -name "*.log"
```

### Review File Permissions

```bash
ls -la logs/
```

## Example SQL Queries

### Failed Login Attempts

```sql
SELECT *
FROM login_attempts
WHERE success = 'No';
```

### Most Active Usernames

```sql
SELECT username, COUNT(*)
FROM login_attempts
GROUP BY username
ORDER BY COUNT(*) DESC;
```

### Successful Login Attempts

```sql
SELECT *
FROM login_attempts
WHERE success = 'Yes';
```

## Skills Demonstrated

### Linux

* Command-line investigation
* Authentication log analysis
* File and directory navigation
* Log searching and filtering
* Security-focused troubleshooting

### SQL

* Data retrieval with SELECT
* Filtering records with WHERE
* Aggregation using COUNT
* Grouping data with GROUP BY
* Sorting results with ORDER BY

### Cybersecurity

* Authentication monitoring
* Failed login detection
* Suspicious activity investigation
* Security reporting
* Log-based threat analysis

## Learning Outcomes

Through this project, I gained practical experience analyzing Linux authentication logs, identifying failed and successful login attempts, and using SQL queries to investigate security events. I also learned how to automate log processing with Python and store security data in a SQLite database for further analysis.

## Key Takeaway

Linux, SQL, and Python are valuable tools for cybersecurity investigations. By combining log analysis, database storage, and query-based reporting, security analysts can efficiently identify suspicious activity and gain insights into authentication events across a system.
