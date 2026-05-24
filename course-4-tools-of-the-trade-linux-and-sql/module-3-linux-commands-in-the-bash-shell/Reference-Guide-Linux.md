# Linux Reference Guide

A quick reference guide for commonly used Linux commands related to navigation, file management, permissions, filtering, and getting help in Linux. 

---

# Table of Contents

* [Navigate the File System]
* [Read Files]
* [Manage the File System]
* [Filter Content]
* [Manage Users and Permissions]
* [Get Help in Linux]

---

# Navigate the File System

## `cd`

Navigate between directories.

### Examples

```bash
cd reports
```

Navigate from the current directory to the `reports` subdirectory.

```bash
cd /home/analyst/reports
```

Navigate directly to the `reports` directory using the full path.

```bash
cd ..
```

Move one directory up from the current working directory.

---

## `ls`

Display files and directories.

### Examples

```bash
ls
```

List files and directories in the current directory.

```bash
ls /home/analyst/reports
```

List contents of the `reports` directory.

```bash
ls -a
```

Show hidden files.

```bash
ls -l
```

Display detailed information including permissions, owner, size, and modification time.

```bash
ls -la
```

Display detailed information including hidden files.

---

## `pwd`

Print the current working directory.

### Example

```bash
pwd
```

Example output:

```bash
/home/analyst
```

---

## `whoami`

Display the current logged-in user.

### Example

```bash
whoami
```

Example output:

```bash
analyst
```

---

# Read Files

## `cat`

Display the full contents of a file.

### Example

```bash
cat updates.txt
```

---

## `head`

Display the beginning of a file.

### Examples

```bash
head updates.txt
```

Display the first 10 lines.

```bash
head -n 5 updates.txt
```

Display the first 5 lines.

---

## `less`

View file contents one page at a time.

### Example

```bash
less updates.txt
```

Useful for large files.

---

## `tail`

Display the end of a file.

### Examples

```bash
tail updates.txt
```

Display the last 10 lines.

```bash
tail -n 5 updates.txt
```

Display the last 5 lines.

---

# Manage the File System

## `cp`

Copy files or directories.

### Example

```bash
cp permissions.txt /home/analyst/logs
```

Copy `permissions.txt` to the `logs` directory.

---

## `mkdir`

Create directories.

### Examples

```bash
mkdir network
```

Create a directory named `network`.

```bash
mkdir /home/analyst/logs/network
```

Create a directory using a full path.

---

## `mv`

Move or rename files and directories.

### Examples

```bash
mv permissions.txt /home/analyst/logs
```

Move a file to another directory.

```bash
mv permissions.txt perm.txt
```

Rename `permissions.txt` to `perm.txt`.

---

## `nano`

Open or create files using the Nano text editor.

### Example

```bash
nano permissions.txt
```

---

## `rm`

Remove files.

### Examples

```bash
rm permissions.txt
```

Delete a file in the current directory.

```bash
rm /home/analyst/reports/permissions.txt
```

Delete a file using the full path.

---

## `rmdir`

Remove empty directories.

### Examples

```bash
rmdir network
```

Remove an empty directory.

```bash
rmdir /home/analyst/logs/network
```

Remove an empty directory using the full path.

---

## `touch`

Create empty files.

### Examples

```bash
touch permissions.txt
```

Create a file in the current directory.

```bash
touch /home/analyst/reports/permissions.txt
```

Create a file using the full path.

---

# Filter Content

## `find`

Search for files and directories.

### Examples

```bash
find /home/analyst/projects
```

Search all files starting from the `projects` directory.

```bash
find /home/analyst/projects -name "*log*"
```

Search for files containing `log` in the filename (case-sensitive).

```bash
find /home/analyst/projects -iname "*log*"
```

Search for files containing `log` in the filename (case-insensitive).

```bash
find /home/analyst/projects -mtime -3
```

Find files modified within the last 3 days.

```bash
find /home/analyst/projects -mmin -15
```

Find files modified within the last 15 minutes.

---

## `grep`

Search for specific text inside files.

### Example

```bash
grep OS updates.txt
```

Return all lines containing the string `OS`.

---

## `|` (Pipe)

Send output from one command into another command.

### Example

```bash
ls /home/analyst/reports | grep users
```

List files containing the word `users`.

---

# Manage Users and Permissions

## `chmod`

Change file or directory permissions.

### Examples

```bash
chmod u+rwx,g+rwx,o+rwx login_sessions.txt
```

Add read, write, and execute permissions for user, group, and others.

```bash
chmod g-rw bonuses.txt
```

Remove read and write permissions from the group.

```bash
chmod u=r,g=r,o=r login_sessions.txt
```

Set read-only permissions for everyone.

---

## `chown`

Change ownership of files and directories.

### Examples

```bash
sudo chown fgarcia access.txt
```

Change the file owner.

```bash
sudo chown :security access.txt
```

Change the group owner.

---

## `groupdel`

Delete groups from the system.

### Example

```bash
sudo groupdel accounting
```

---

## `sudo`

Run commands with elevated privileges.

### Example

```bash
sudo useradd fgarcia
```

---

## `useradd`

Add new users.

### Examples

```bash
sudo useradd fgarcia
```

Add a user.

```bash
sudo useradd -g security fgarcia
```

Set the primary group.

```bash
sudo useradd -G finance,admin fgarcia
```

Add supplemental groups.

---

## `userdel`

Delete users.

### Examples

```bash
sudo userdel fgarcia
```

Delete a user.

```bash
sudo userdel -r fgarcia
```

Delete a user and their home directory.

---

## `usermod`

Modify existing users.

### Examples

```bash
sudo usermod -g executive fgarcia
```

Change the primary group.

```bash
sudo usermod -G accounting fgarcia
```

Replace supplemental groups.

```bash
sudo usermod -a -G marketing fgarcia
```

Add a supplemental group without removing existing ones.

```bash
sudo usermod -d /home/garcia_f fgarcia
```

Change the home directory.

```bash
sudo usermod -L fgarcia
```

Lock a user account.

```bash
sudo usermod -l garcia_f fgarcia
```

Rename a user account.

---

# Get Help in Linux

## `apropos`

Search manual page descriptions.

### Examples

```bash
apropos password
```

Search for commands related to `password`.

```bash
apropos -a graph editor
```

Search for commands containing both `graph` and `editor`.

---

## `man`

Display detailed manual pages.

### Example

```bash
man chown
```

---

## `whatis`

Display a short one-line description of a command.

### Example

```bash
whatis nano
```
