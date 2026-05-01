## Module 1.2: Network Communication

## Overview

- Network communication allows devices to send and receive data across networks
- Data is transferred in small units called data packets
- Enables:
  - Internet access
  - File sharing
  - Communication between systems
- Also introduces security risks (attackers can intercept or exploit data)

## Data Packets

- A data packet is the basic unit of data sent across a network
- Data is broken into smaller pieces before transmission

Each packet contains:

- Source address
- Destination address
- Actual data/message

## Packet Structure

- Similar to sending a letter

### Header

- Contains IP address and MAC address
- Includes protocol information

### Body

- Contains the actual data

### Footer

- Marks the end of the packet

## Network Performance

### Bandwidth

- Amount of data transmitted per second

### Speed

- How fast data is received

- Unusual changes may indicate:
  - Network issues
  - Possible attacks

## Packet Sniffing

- Capturing and analyzing network packets

Used by:

- Security professionals → monitoring
- Attackers → stealing data

## The TCP/IP Model

## Overview

- Standard framework for network communication
- Defines how data is sent and received

### TCP (Transmission Control Protocol)

- Ensures:
  - Reliable delivery
  - Organized data
- Establishes connection between devices

### IP (Internet Protocol)

- Handles:
  - Addressing
  - Routing
- Uses IP addresses to identify devices

### Ports

- Software-based communication endpoints

Purpose:

- Organize different types of traffic

Example:

- IP = building address
- Port = apartment number

### Common Ports

- Port 25 → Email
- Port 443 → HTTPS
- Port 20 → FTP

## The Four Layers of the TCP/IP Model

### Network Access Layer

- Handles physical transmission
- Includes hardware (cables, switches)

### Internet Layer

- Handles IP addressing and routing

### Transport Layer

- Ensures reliable data delivery
- Controls data flow and errors

### Application Layer

- Interface between user and network
- Supports:
  - Email
  - File transfer

## The OSI Model

## Overview

- Conceptual model with 7 layers
- Used to understand network communication

### Layers

#### Application

- User-facing services

#### Presentation

- Data formatting and encryption

#### Session

- Manages connections

#### Transport

- Reliable delivery

#### Network

- Routing (IP addresses)

#### Data Link

- MAC address communication

#### Physical

- Hardware and signals

## TCP/IP vs OSI

- TCP/IP → 4 layers (used in real world)
- OSI → 7 layers (used for learning and troubleshooting)

## Key Takeaways

- Network communication uses data packets
- TCP/IP model defines how data is transmitted
- OSI model helps understand network layers
- Packet sniffing can be useful but also a security risk
- Understanding these concepts is essential for network security and troubleshooting
