## Module 1.3: Local and Wide Network Communication

## Overview

- Network communication can occur within local networks (LAN) or across wide networks (WAN)
- Devices use IP addresses and MAC addresses to communicate
- Data is routed through different components to reach its destination

## IP Addresses and Network Communication

### What is an IP Address

- An IP address is a unique identifier for a device on a network
- Allows devices to:
  - Send data
  - Receive data

Example:

- Like a home address for delivering mail

### Types of IP Addresses

#### IPv4

- Format: four numbers separated by dots
- Example: 192.168.1.1
- Limited number of addresses

#### IPv6

- Longer format
- Supports a much larger number of devices

### Public vs Private IP Addresses

#### Public IP Address

- Assigned by an ISP (Internet Service Provider)
- Used for communication over the internet

#### Private IP Address

- Used inside a local network (LAN)
- Not visible outside the network

## MAC Addresses

### Overview

- A MAC address is a unique identifier for a device’s network interface
- Used for communication within a local network

### Key Role

- Helps devices identify each other at the hardware level

## Components of Network Layer Communication

### Switches

- Connect devices within a local network
- Use MAC addresses to send data to the correct device

### MAC Address Table

- A table maintained by a switch
- Maps:
  - MAC addresses → switch ports

Purpose:

- Efficiently deliver data to the correct device

### Routing (WAN Communication)

- Routers send data between different networks
- Use IP addresses to determine where data should go

## Local vs Wide Network Communication

### Local Area Network (LAN)

- Small network (home, office)
- Uses:
  - Private IP addresses
  - MAC addresses

### Wide Area Network (WAN)

- Large network (internet)
- Uses:
  - Public IP addresses
  - Routers for communication

## Key Takeaways

- IP addresses identify devices on networks
- MAC addresses identify devices within local networks
- Switches use MAC addresses for local communication
- Routers use IP addresses for wide network communication
- LAN = local communication, WAN = global communication
