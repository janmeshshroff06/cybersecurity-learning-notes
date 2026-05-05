## Module 3.3: Network Attack Tactics and Defense

## Malicious Packet Sniffing

## Overview

- Packet sniffing captures and analyzes data packets on a network
- Used by:
  - Security professionals → monitoring
  - Attackers → stealing sensitive data

## How Packet Sniffing Works

- Data travels in packets containing:
  - Header (IP, routing info)
  - Body (actual data)

- Attackers use tools to:
  - Capture packets
  - Inspect transmitted data

## Types of Packet Sniffing

### Passive Sniffing

- Observes packets without changing them
- Common in less secure networks

### Active Sniffing

- Modifies or redirects packets
- More dangerous and harder to detect

## Risks

- Exposure of:
  - Personal data
  - Financial information
  - Credentials

## Prevention Methods

- Use VPNs
- Use HTTPS (encryption)
- Avoid unsecured public Wi-Fi

## Key Takeaway

- Packet sniffing allows attackers to intercept sensitive data, but encryption reduces risk

## IP Spoofing

## Overview

- Attack where attacker fakes source IP address
- Makes traffic appear from a trusted system

## How It Works

- Modifies packet headers
- Bypasses security controls

## Common Attacks Using Spoofing

### On-Path (Man-in-the-Middle)

- Intercepts communication
- Can modify data

### Replay Attack

- Captures and resends valid packets

### Smurf Attack

- Combines spoofing + DDoS
- Floods victim with traffic

## Prevention Methods

- Encryption
- Strong firewall rules
- Network monitoring

## Key Takeaway

- IP spoofing allows attackers to impersonate trusted systems and bypass defenses

## Overview of Interception Tactics

## Overview

- Interception attacks involve unauthorized access to data in transit
- Often used to:
  - Steal data
  - Monitor communication

## Common Interception Techniques

- Packet sniffing
- Man-in-the-middle attacks
- Session hijacking

## Goals of Attackers

- Capture sensitive data
- Gain unauthorized access
- Disrupt communication

## Defense Strategies

- Use encryption (HTTPS, VPNs)
- Secure network configurations
- Monitor traffic patterns

## Analyze Network Attacks

## Purpose

- Identify suspicious behavior in network traffic

## Indicators of Attack

- Unusual traffic spikes
- Unknown IP addresses
- Repeated connection attempts

## Tools Used

- SIEM tools
- Packet analyzers

## Key Takeaways

- Network attacks often involve intercepting or manipulating data
- Packet sniffing and spoofing are common attack methods
- Encryption and monitoring are key defenses
- Identifying attack patterns helps prevent future incidents

## Big Picture

- Network attack tactics focus on intercepting, impersonating, or disrupting communication
- Defenses rely on encryption, monitoring, and secure configurations to protect systems
