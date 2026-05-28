SELECT username, COUNT(*)
FROM login_attempts
GROUP BY username
ORDER BY COUNT(*) DESC;