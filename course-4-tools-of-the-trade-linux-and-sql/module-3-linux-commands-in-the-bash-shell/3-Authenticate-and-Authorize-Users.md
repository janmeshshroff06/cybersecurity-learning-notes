## Module 3.3: Authenticate and Authorize Users

## File Permissions and Ownership

## Overview

- Linux uses permissions and ownership to control access to files and directories
- Permissions determine:
  - Who can read files
  - Modify files
  - Execute files

- Permissions are an important part of:
  - Authorization
  - System security

## Authorization

## Overview

- Authorization determines what resources a user is allowed to access
- Helps protect:
  - Files
  - Directories
  - System resources

- Follows the:
  - Need-to-know principle

## Purpose of Authorization

- Prevents unauthorized users from:
  - Viewing files
  - Modifying content
  - Running programs

## Types of Permissions

### Read Permission (r)

- On files:
  - Allows viewing file contents

- On directories:
  - Allows viewing files inside the directory

### Write Permission (w)

- On files:
  - Allows modifying file contents

- On directories:
  - Allows creating or deleting files

### Execute Permission (x)

- On files:
  - Allows running executable files

- On directories:
  - Allows entering/accessing the directory

## Ownership Categories

### User

- Owner of the file
- Usually the creator of the file

### Group

- Collection of users sharing permissions
- Common in team environments

### Other

- All remaining users on the system
- Anyone outside the owner or assigned group

## Permission String Format

### Permission Example

Example:

```bash id="5p7mec"
-rw-r--r--
```

### First Character

- Indicates file type

Examples:

- `-` → Regular file
- `d` → Directory

### Permission Sections

- Characters 2–4:
  - User permissions

- Characters 5–7:
  - Group permissions

- Characters 8–10:
  - Other permissions

### Hyphen (-)

- Indicates a permission is NOT granted

Example:

```bash id="p0n20j"
r--
```

- Read only
- No write or execute access

## Viewing Permissions

### ls -l Command

- Displays detailed file permissions and ownership

Example:

```bash id="g87o1h"
ls -l
```

### ls -a Command

- Displays hidden files

Example:

```bash id="m2wl8u"
ls -a
```

### ls -la Command

- Displays all files with detailed permissions

Example:

```bash id="alw5e1"
ls -la
```

### Hidden Files

- Hidden files begin with:

```bash id="56zc7y"
.
```

Example:

```bash id="lq1waj"
.hidden1.txt
```

## World-Writable Files

## Overview

- World-writable files allow:
  - User
  - Group
  - Other

to all modify the file

## Security Risk

- Can create major vulnerabilities because:
  - Anyone can alter the file
  - Attackers may abuse permissions

## Change Permissions

## Overview

- Linux permissions can be changed using:
  - `chmod`

- Useful when:
  - Users change roles
  - Projects change
  - Access requirements are updated

## chmod Command

## Overview

- `chmod` stands for:
  - Change mode

- Used to modify file and directory permissions

## Symbolic Mode

- Uses symbols to represent permission groups and changes

## Owner Symbols

- `u` → User
- `g` → Group
- `o` → Other

## Operators

- `+` → Add permission
- `-` → Remove permission

## Permission Symbols

- `r` → Read
- `w` → Write
- `x` → Execute

## chmod Example

Example:

```bash id="y3b8o7"
chmod g+w,o-r access.txt
```

## Example Breakdown

- `g+w`
  - Adds write permission to the group

- `o-r`
  - Removes read permission from others

## Add and Delete Users

## Overview

- Linux systems use authentication to verify user identities
- Organizations manage:
  - User accounts
  - Permissions
  - Group access

## Authentication

## Overview

- Authentication verifies a user's identity
- Helps prevent unauthorized access

## Root User (Superuser)

## Overview

- The root user has elevated privileges

- Can:
  - Modify the system
  - Create/delete files
  - Manage users

## Security Risks

- Direct root access is risky because:
  - Mistakes can damage the system
  - Attackers often target root accounts

## sudo Command

## Overview

- `sudo` stands for:
  - Super-user-do

- Temporarily grants elevated privileges

Example:

```bash id="2i5ggm"
sudo useradd salesrep7
```

## Benefits of sudo

- Improves:
  - Security
  - Accountability

- Users authenticate with their own password

## User Management Commands

### useradd Command

- Adds a new user to the system

Example:

```bash id="cnby8n"
sudo useradd salesrep7
```

### userdel Command

- Removes a user from the system

Example:

```bash id="v24n86"
sudo userdel salesrep7
```

## Responsible Use of sudo

### Least Privilege Principle

- Users should only receive permissions necessary for their job
- Excessive privileges increase security risks

### Why Responsible sudo Usage Matters

- Improper sudo use can:
  - Damage systems
  - Delete important files
  - Create vulnerabilities

## Cybersecurity Importance

### Why Permissions Matter

- Security analysts manage permissions to:
  - Protect sensitive files
  - Prevent unauthorized access
  - Maintain secure systems

### Common Security Tasks

- Reviewing permissions
- Managing users/groups
- Restricting file access
- Applying least privilege

## Key Takeaways

- Linux permissions control access to files and directories

- Main permissions are:
  - Read
  - Write
  - Execute

- Permissions apply to:
  - User
  - Group
  - Other

- `chmod` changes permissions
- `sudo` provides temporary elevated privileges safely
- `useradd` creates users and `userdel` removes users
- Proper authorization and permission management are essential in cybersecurity

## Big Picture

- Authentication and authorization help secure Linux systems
- Control who can access resources and what actions users are allowed to perform
