import sqlite3

conn = sqlite3.connect("database/security.db")
cursor = conn.cursor()

print("\n=== Failed Login Attempts ===")
cursor.execute("SELECT username, ip_address FROM login_attempts WHERE success = 'No'")
for row in cursor.fetchall():
    print(row)

print("\n=== Suspicious IP Addresses ===")
cursor.execute("""
SELECT ip_address, COUNT(*) 
FROM login_attempts 
WHERE success = 'No'
GROUP BY ip_address
ORDER BY COUNT(*) DESC
""")
for row in cursor.fetchall():
    print(row)

print("\n=== Successful Logins ===")
cursor.execute("SELECT username, ip_address FROM login_attempts WHERE success = 'Yes'")
for row in cursor.fetchall():
    print(row)

conn.close()