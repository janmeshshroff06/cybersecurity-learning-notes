## Module 2.2: System Identification

## Firewalls and Network Security Measures

## Overview

- A firewall monitors and controls incoming and outgoing network traffic
- Uses security rules to:
  - Allow traffic
  - Block traffic
- Protects networks from unauthorized access and threats

## How Firewalls Work

- Inspect data packets before allowing entry
- Use rules based on:
  - IP addresses
  - Port numbers

Example:

- Allow port 443 (HTTPS)  
- Block unknown ports  

## Types of Firewalls

### Hardware Firewall

- Physical device
- Filters traffic before entering network

### Software Firewall

- Installed on devices
- Protects individual systems

### Cloud-Based Firewall

- Hosted in cloud
- Protects both cloud and on-prem systems

## Stateful vs Stateless

### Stateful

- Tracks active connections
- More secure

### Stateless

- Uses fixed rules only
- Does not track past activity

## Next-Generation Firewalls (NGFW)

- Advanced firewalls with:
  - Deep packet inspection
  - Intrusion detection
  - Threat intelligence

## Key Takeaway

- Firewalls are a first line of defense in network security

## Virtual Private Networks (VPNs)

## Overview

- A VPN protects data and privacy on the internet
- Hides:
  - IP address
  - User location

## How VPNs Work

- Create an encrypted tunnel between:
  - User device
  - VPN server

## Encryption

- Converts data into unreadable form
- Protects sensitive information

## Encapsulation

- Wraps data inside another packet
- Allows secure transmission while maintaining routing

## Key Takeaway

- VPNs provide privacy, security, and confidentiality online

## Security Zones

## Overview

- Networks are divided into segments (zones)
- Each zone has different security levels

## Types of Zones

### Uncontrolled Zone

- External network (internet)

### Controlled Zone

- Internal network

### DMZ (Demilitarized Zone)

- Contains public-facing systems:
  - Web servers
  - Email servers
- Acts as a buffer between internet and internal network

### Internal Network

- Contains private systems
- Access restricted to authorized users

### Restricted Zone

- Highly secure area
- Stores sensitive data

## Key Takeaway

- Security zones improve protection through network segmentation

## Subnetting and CIDR

## Overview

- Subnetting divides a network into smaller networks
- Improves:
  - Performance
  - Security

## CIDR (Classless Inter-Domain Routing)

- Method for assigning IP addresses efficiently
- Uses notation like:
  - 192.168.1.0/24

## Key Takeaway

- Subnetting helps organize and secure networks

## Proxy Servers

## Overview

- A proxy server acts as an intermediary between users and the internet
- Adds:
  - Security
  - Privacy
  - Control

## How Proxy Servers Work

- Receives request → checks it → forwards it
- Uses a different IP address than the client

## Types of Proxies

### Forward Proxy

- Handles outgoing requests
- Hides user identity

### Reverse Proxy

- Handles incoming requests
- Protects servers

### Email Proxy

- Filters emails for spam and phishing

## Caching

- Stores frequently accessed data
- Improves speed and performance

## Key Takeaway

- Proxy servers enhance security and performance

## Virtual Networks and Privacy

## Overview

- Virtual networks simulate physical networks in software
- Used in cloud environments

## Benefits

- Flexibility
- Scalability
- Improved privacy

## VPN Protocols

### WireGuard

- Modern VPN protocol
- Fast and efficient
- Strong encryption

### IPSec

- Secures communication at network layer
- Widely used in enterprise environments

## Key Takeaway

- VPN protocols ensure secure and encrypted communication

## Key Takeaways

- Firewalls protect networks by controlling traffic
- VPNs secure data and hide identity
- Security zones segment networks for better protection
- Subnetting improves network efficiency and security
- Proxy servers add an extra security layer
- VPN protocols ensure encrypted communication

## Big Picture

- System identification tools and techniques help organizations
  control access, protect data, and secure network infrastructure
