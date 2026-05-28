import sqlite3
import re

conn = sqlite3.connect("database/security.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS login_attempts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    ip_address TEXT,
    success TEXT,
    log_entry TEXT
)
""")

with open("logs/auth.log", "r") as file:
    for line in file:
        username_match = re.search(r"for (\w+)", line)
        ip_match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)

        username = username_match.group(1) if username_match else "unknown"
        ip_address = ip_match.group(1) if ip_match else "unknown"
        success = "No" if "Failed password" in line else "Yes"

        cursor.execute("""
        INSERT INTO login_attempts (username, ip_address, success, log_entry)
        VALUES (?, ?, ?, ?)
        """, (username, ip_address, success, line.strip()))

conn.commit()
conn.close()

print("Logs loaded into database/security.db")