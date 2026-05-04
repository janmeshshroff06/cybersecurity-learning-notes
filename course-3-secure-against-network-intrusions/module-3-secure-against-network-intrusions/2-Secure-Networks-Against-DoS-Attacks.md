## Module 3.2: Secure Networks Against Denial of Service (DoS) Attacks

## Denial of Service (DoS) Attacks

## Overview

- A Denial of Service (DoS) attack floods a system with excessive traffic
- Goal is to make the system:
  - Slow
  - Unresponsive
  - Unavailable
- Prevents legitimate users from accessing services

## Distributed Denial of Service (DDoS)

- Uses multiple devices (botnets) to attack a target
- More powerful and harder to stop than DoS
- Traffic comes from many locations simultaneously

## Common Types of DoS Attacks

### SYN Flood Attack

- Exploits the TCP handshake process
- Attacker sends many SYN requests
- Server responds but never receives final ACK

Result:

- Server resources get exhausted
- System becomes unresponsive

### ICMP Flood Attack

- Uses ICMP (ping requests)
- Attacker sends large number of requests

Result:

- Bandwidth gets consumed
- System slows down or crashes

### Ping of Death

- Sends oversized ICMP packets
- Exploits system limitations

Result:

- System crashes or becomes unstable

## Reading tcpdump Logs

## Overview

- tcpdump is a tool used to capture and analyze network traffic
- Helps detect:
  - Suspicious activity
  - Attack patterns

## Key Use

- Identify abnormal traffic spikes
- Detect repeated requests from same source
- Analyze packet details

## Real-Life DDoS Attack

## Insight

- Real-world attacks show:
  - Massive traffic overload
  - Service outages
  - Large-scale disruption

- Often involve:
  - Botnets
  - Compromised devices

## Analyze Network Layer Communication

## Purpose

- Examine traffic patterns at network layer
- Identify:
  - Unusual spikes
  - Malicious activity

## Key Indicators of Attack

- High volume of traffic
- Repeated requests
- Unknown or suspicious IP addresses

## Defending Against DoS Attacks

### Common Mitigation Techniques

- Use firewalls and filtering rules
- Implement rate limiting
- Monitor traffic using tools (like tcpdump, SIEM)
- Use load balancing
- Deploy intrusion detection systems (IDS)

## Key Takeaway

- DoS attacks target availability
- Early detection and monitoring are critical

## Key Takeaways

- DoS attacks overwhelm systems with traffic
- DDoS attacks use multiple sources and are harder to stop
- Common attacks include SYN flood, ICMP flood, and ping of death
- Tools like tcpdump help detect attacks
- Monitoring and filtering are key defenses

## Big Picture

- Protecting against DoS attacks ensures systems remain available, reliable, and secure
- Essential for maintaining business operations
