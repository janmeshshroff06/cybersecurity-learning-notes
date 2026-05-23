## Module 3.2: Manage File Content in Bash

## Find What You Need with Linux

## Overview

- Security analysts often need to quickly locate important information in Linux
- Linux filtering tools help analysts:
  - Search logs
  - Find files
  - Investigate incidents
  - Analyze suspicious activity

- Common filtering tools include:
  - `grep`
  - Piping (`|`)

## Filtering in Linux

## Overview

- Filtering means searching for:
  - Specific text
  - Patterns
  - Information within files

- Useful when working with:
  - Large logs
  - Reports
  - System files

## grep Command

- `grep` searches files for a specific string of characters
- Returns all matching lines

Basic syntax:

```bash id="z84xq1"
grep [string] [file]
```

## grep Example

Example:

```bash id="n72mvp"
grep OS updates.txt
```

- Searches `updates.txt` for lines containing:
  - `OS`

## Why grep is Important

- Helps analysts avoid manually searching large files

Common cybersecurity uses:

- Searching logs
- Finding suspicious activity
- Investigating malware

## Piping Commands

## Overview

- Piping connects commands together

- Uses the pipe symbol:

```bash id="b91lka"
|
```

- Sends output from one command into another command

## Pipe Example

Example:

```bash id="u28wfd"
ls reports | grep users
```

Process:

- `ls reports`
  - Lists files/directories

- `grep users`
  - Filters results containing `users`

## Benefits of Piping

- Makes filtering more efficient
- Allows advanced searches
- Helps automate command workflows

## Create and Modify Directories and Files

## Overview

- Linux provides commands for:
  - Creating files
  - Managing directories
  - Moving data
  - Editing content

- File organization is important for:
  - Log management
  - Investigations
  - Security reporting

## Directory Management Commands

### mkdir Command

- `mkdir` stands for:
  - Make Directory

- Creates new directories

Example:

```bash id="j93fpl"
mkdir drafts
```

### rmdir Command

- `rmdir` stands for:
  - Remove Directory

- Deletes empty directories

Example:

```bash id="x41tke"
rmdir drafts
```

## File Management Commands

### touch Command

- Creates a new empty file

Example:

```bash id="v66ohr"
touch OS_patches.txt
```

### rm Command

- Removes files

Example:

```bash id="f52kzm"
rm email_patches.txt
```

### mv Command

- Moves or renames files/directories

Example:

```bash id="q13ldb"
mv report.txt drafts
```

### cp Command

- Copies files/directories

Example:

```bash id="m77sja"
cp vulnerabilities.txt projects
```

## Navigation and Verification Commands

### pwd Command

- Displays the current working directory

Example:

```bash id="g85rnp"
pwd
```

### ls Command

- Lists files and directories

Example:

```bash id="h63wlt"
ls
```

## Editing Files with nano

### nano Text Editor

- Beginner-friendly Linux text editor
- Used to create and edit text files

Example:

```bash id="d49vcu"
nano OS_patches.txt
```

### Saving and Exiting nano

- Save file:
  - `Ctrl + O`

- Confirm save:
  - Press `Enter`

- Exit nano:
  - `Ctrl + X`

## Cybersecurity Importance

### Why File Management Matters

- Security analysts manage:
  - Logs
  - Reports
  - Configuration files
  - Investigation records

- Linux file commands help analysts:
  - Stay organized
  - Investigate incidents efficiently
  - Manage system data securely

## Key Takeaways

- Linux filtering tools help locate important information quickly
- `grep` searches files for matching text
- Piping (`|`) connects commands together for advanced filtering
- Important file management commands include:
  - `mkdir`
  - `rmdir`
  - `touch`
  - `rm`
  - `mv`
  - `cp`

- `nano` is commonly used for editing text files
- File management skills are essential in cybersecurity and Linux administration

## Big Picture

- Linux filtering and file management commands allow security professionals to efficiently organize data
- Helps investigate incidents, search logs, and manage system files directly from the Bash shell
