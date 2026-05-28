# Security Investigation Report

## Project

Linux & SQL Security Investigation Toolkit

## Objective

The objective of this project was to investigate Linux authentication logs, identify failed and successful login attempts, store log data in a SQL database, and generate useful security findings.

## Data Source

The project uses a sample Linux authentication log located at:

```text
logs/auth.log
```

## Investigation Steps

* Reviewed Linux authentication log entries.
* Parsed failed and successful SSH login attempts using Python.
* Extracted usernames and IP addresses from log data.
* Stored login activity in a SQLite database.
* Queried the database to identify suspicious activity.

## Linux Investigation Activities

Linux commands were used to examine authentication logs and identify login activity.

### Example Commands

```bash
grep "Failed password" logs/auth.log
```

```bash
grep "Accepted password" logs/auth.log
```

```bash
cat logs/auth.log
```

```bash
sqlite3 login_activity.db
```

## SQL Investigation Activities

SQL queries were used to analyze login activity stored in a SQLite database.

### Investigations Performed

#### Failed Login Attempts

```sql
SELECT *
FROM login_attempts
WHERE success = 'No';
```

Purpose:

* Identify unsuccessful authentication attempts.

#### Suspicious Users

```sql
SELECT username, COUNT(*)
FROM login_attempts
GROUP BY username
ORDER BY COUNT(*) DESC;
```

Purpose:

* Identify accounts with the highest number of login attempts.

#### Successful Logins

```sql
SELECT *
FROM login_attempts
WHERE success = 'Yes';
```

Purpose:

* Review successful authentication events.

## Findings

### Failed Login Attempts

The log showed multiple failed SSH login attempts.

| Username | IP Address   |
| -------- | ------------ |
| root     | 192.168.1.10 |
| admin    | 192.168.1.10 |
| root     | 192.168.1.11 |
| root     | 192.168.1.10 |

### Successful Login

| Username | IP Address   |
| -------- | ------------ |
| janmesh  | 192.168.1.20 |

### Suspicious IP Activity

The IP address **192.168.1.10** appeared multiple times in failed login attempts. This behavior may indicate brute-force activity or unauthorized access attempts.

## Conclusion

This investigation identified repeated failed login attempts originating from **192.168.1.10**, making it the most suspicious IP address in the sample logs. The project demonstrates how Linux log analysis, Python automation, and SQL queries can be combined to perform basic cybersecurity investigations and identify potentially malicious activity.
