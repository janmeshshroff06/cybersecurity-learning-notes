## Module 1.2: The Operating System at Work

## Inside the Operating System

## Overview

- The operating system (OS) manages communication between:
  - Users
  - Applications
  - Hardware

- Allows programs to run efficiently without users managing hardware directly

## Booting the Computer

- When a computer powers on, the boot process begins

## BIOS and UEFI

### BIOS (Basic Input/Output System)

- Older startup firmware

### UEFI (Unified Extensible Firmware Interface)

- Modern replacement for BIOS

## Bootloader

- Loaded by BIOS/UEFI
- Responsible for starting the operating system

## Boot Process Security

- Boot process vulnerabilities may allow:
  - Malware infections
  - Unauthorized modifications

- BIOS/UEFI are often not scanned by antivirus tools

## Applications and the OS

- Applications send requests to the OS
- OS communicates with hardware to complete tasks

## Hardware Interaction Example

### Calculator Process

- User opens calculator app
- App sends request to OS
- OS sends request to CPU
- CPU performs calculation
- Result returns:
  - CPU → OS → Application → User

## Requests to the Operating System

## Overview

- Applications rely on the OS to access:
  - Files
  - Memory
  - Hardware resources

## System Calls

- Requests from applications to the OS are called system calls

## Purpose

- Allows applications to safely use system resources without direct hardware access

## Resource Allocation via the OS

## Overview

- The OS manages computer resources so multiple programs can run efficiently

## Resources Managed

- CPU usage
- Memory
- Storage
- Bandwidth

## Multitasking

- Multiple applications run simultaneously
- OS allocates resources where needed most

## Task Manager

- Displays:
  - Running processes
  - CPU usage
  - Memory usage

- Useful for:
  - Monitoring performance
  - Troubleshooting issues

## Cybersecurity Importance

- Malware often uses excessive resources
- Security analysts monitor abnormal resource usage

## Virtualization Technology

## Overview

- Virtualization allows one physical computer to run multiple virtual systems

## Virtual Machine (VM)

- Software-based computer running inside another system

## Benefits

- Isolation between systems
- Efficient resource use
- Safe testing environments

## Hypervisor

- Software managing virtual machines

## Types of Hypervisors

### Type 1

- Runs directly on hardware

### Type 2

- Runs on top of an operating system

## Cybersecurity Uses

- Malware analysis
- Secure testing
- Sandboxing suspicious files

## Key Takeaways

- The OS manages communication between users, applications, and hardware
- BIOS/UEFI and bootloaders start the operating system
- Applications use system calls to request resources
- OS handles multitasking and resource allocation
- Virtualization allows multiple systems to run securely on one machine
- Monitoring OS behavior is important in cybersecurity

## Big Picture

- The operating system controls how systems function, allocate resources, and communicate with hardware
- Critical part of both computing and cybersecurity operations
