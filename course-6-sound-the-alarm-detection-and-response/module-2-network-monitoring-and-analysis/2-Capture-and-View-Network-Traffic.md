# Module **2.2 Capture and View Network Traffic**

---

# **Packets and Packet Captures**

## **Overview**

* Network communication occurs through:

  * Packets
* Every time data is sent across a network:

  * It is broken into smaller packets
* Security analysts examine packets to:

  * Monitor network activity
  * Detect suspicious behavior
  * Investigate cybersecurity incidents
* A **packet capture (PCAP)** records network traffic so it can be analyzed later.
* Packet analysis provides one of the most detailed views of network communications.

---

## **Key Concepts**

---

### **Packet**

* A **packet** is:

  * The basic unit of data transmitted across a network.
* Packets contain:

  * Header
  * Payload
* Large files are divided into:

  * Multiple packets before being transmitted.

---

### **Purpose of Packets**

* Packets allow data to:

  * Travel efficiently across networks
  * Be routed independently
  * Be reassembled at the destination
* Breaking data into packets:

  * Improves speed
  * Improves reliability
  * Makes network communication scalable

---

### **Packet Header**

* Every packet contains a:

  * Header
* The header stores information required to deliver the packet correctly.

---

### **Packet Payload**

* The payload contains:

  * The actual information being transmitted.
* Examples include:

  * Emails
  * Web pages
  * Images
  * Files
  * Messages

---

### **Packet Capture (PCAP)**

* A **Packet Capture (PCAP)** is:

  * A recording of network packets.
* PCAP files contain:

  * Packet headers
  * Packet payloads
* Security analysts use PCAP files to:

  * Analyze communications
  * Investigate incidents
  * Troubleshoot networks

---

### **Packet Capture Tools**

* Common packet capture tools include:

  * Wireshark
  * tcpdump
* These tools allow analysts to:

  * Capture packets
  * Filter traffic
  * Inspect packet contents

---

### **Analyzing Packet Captures**

* Analysts examine PCAPs to determine:

  * Who sent the data
  * Where it was sent
  * Which protocol was used
  * Whether the communication is legitimate
* Packet captures provide valuable evidence during:

  * Security investigations

---

### **Network Visibility**

* Packet captures improve:

  * Network visibility
* Analysts can observe:

  * Device communications
  * Protocol usage
  * Suspicious traffic
  * Network behavior over time

---

### **Benefits of Packet Analysis**

* Helps organizations:

  * Detect cyberattacks
  * Investigate incidents
  * Troubleshoot network problems
  * Understand attacker behavior
  * Verify security alerts

---

## **Importance in Cybersecurity**

* Packet captures are one of the most valuable sources of:

  * Network evidence
* Analysts rely on packet captures to:

  * Investigate attacks
  * Understand how attackers communicate
  * Detect malicious activity
  * Support forensic investigations

---

## **Key Takeaways**

* A packet is the basic unit of data transmitted across a network.
* Every packet contains:

  * A header
  * A payload
* Packet captures (PCAPs) record network communications for later analysis.
* Common packet analysis tools include Wireshark and tcpdump.
* Packet analysis provides detailed visibility into network communications and supports cybersecurity investigations.

---

# **Interpret Network Communications with Packets**

## **Overview**

* Every packet contains information that allows devices to:

  * Send data
  * Receive data
  * Route communications correctly
* By interpreting packet information, analysts can:

  * Understand network behavior
  * Detect suspicious activity
  * Investigate cybersecurity incidents
* Packet interpretation is one of the most important skills for:

  * Network monitoring
  * Incident response
  * Threat hunting

---

## **Key Concepts**

---

### **Interpreting Packets**

* Analysts examine packets to determine:

  * Source
  * Destination
  * Protocol
  * Legitimacy of communication

---

### **Source IP Address**

* Identifies:

  * The device that sent the packet
* Helps analysts determine:

  * Where network traffic originated

---

### **Destination IP Address**

* Identifies:

  * The receiving device
* Helps determine:

  * The intended destination

---

### **Port Numbers**

* Port numbers identify:

  * The application or service using the connection
* Analysts use ports to identify:

  * Which services are communicating

---

### **Protocols**

* Packets specify the protocol being used.
* Common protocols include:

  * TCP
  * UDP
  * HTTP
  * HTTPS
  * DNS
  * ICMP

---

### **Packet Payload**

* Contains:

  * The transmitted information
* Examples:

  * Email messages
  * Web content
  * Files
  * Images

---

### **Packet Analysis**

* Packet analysis allows analysts to:

  * Trace communications
  * Verify legitimate traffic
  * Detect malicious behavior
  * Investigate incidents

---

## **Importance in Cybersecurity**

* Packet interpretation enables analysts to:

  * Monitor networks
  * Detect anomalies
  * Investigate attacks
  * Understand attacker communications

---

## **Key Takeaways**

* Every packet contains a header and payload.
* Source and destination IP addresses identify communicating devices.
* Port numbers identify applications and services.
* Protocols determine how devices communicate.
* Packet analysis is essential for network monitoring and incident response.

---

# **Reexamine the Fields of a Packet Header**

## **Overview**

* Packet headers contain the routing and communication information required to transmit data.
* Understanding header fields allows analysts to:

  * Trace network traffic
  * Detect malicious communications
  * Troubleshoot network issues
  * Investigate incidents

---

## **Key Concepts**

---

### **Source IP Address**

* Identifies:

  * The sending device
* Used to:

  * Trace where traffic originated

---

### **Destination IP Address**

* Identifies:

  * The receiving device
* Helps analysts determine:

  * Where traffic is headed

---

### **Source Port**

* Identifies:

  * The application or process sending the packet

---

### **Destination Port**

* Identifies:

  * The receiving application or service
* Common ports:

  * HTTP → 80
  * HTTPS → 443
  * DNS → 53
  * SSH → 22

---

### **Protocol**

* Specifies the communication protocol.
* Common values:

  * TCP
  * UDP
  * ICMP

---

### **Packet Length**

* Indicates:

  * Total packet size
* Helps:

  * Detect incomplete transmissions
  * Process packets correctly

---

### **Time to Live (TTL)**

* **TTL** is:

  * The maximum number of routers (hops) a packet can pass through.
* Each router:

  * Decreases the TTL value by one.
* When TTL reaches zero:

  * The packet is discarded.
* Prevents:

  * Packets from endlessly looping around the network.

---

### **Flags**

* Flags contain:

  * Control information
* Used to manage:

  * Connection establishment
  * Connection termination
  * Data transmission

---

### **Sequence Number**

* Identifies:

  * The packet's position within a communication stream.
* Allows:

  * Correct reassembly of packets at the destination.

---

### **Checksum**

* A checksum verifies:

  * Packet integrity.
* Detects:

  * Corrupted packets
  * Transmission errors
* Invalid checksums usually result in:

  * Packet rejection

---

### **Payload**

* Contains:

  * The actual transmitted data.

---

### **Why Packet Headers Matter**

* Packet headers allow analysts to:

  * Trace communications
  * Identify devices
  * Detect abnormal traffic
  * Investigate attacks

---

## **Importance in Cybersecurity**

* Understanding packet header fields is essential for:

  * Threat detection
  * Network monitoring
  * Packet analysis
  * Digital forensics
  * Incident response

---

## **Key Takeaways**

* Packet headers contain routing and communication information.
* Important fields include:

  * Source IP
  * Destination IP
  * Source Port
  * Destination Port
  * Protocol
  * Length
  * TTL
  * Flags
  * Sequence Number
  * Checksum
* The payload contains the transmitted information.
* Header analysis helps analysts investigate network communications and identify malicious activity.

---

# **Big Picture**

This section introduced **packet analysis**, one of the most important skills for cybersecurity analysts. You learned that all network communication is broken into **packets**, each containing a **header** (routing and control information) and a **payload** (actual data). By capturing traffic with **PCAP files** and analyzing fields such as IP addresses, ports, protocols, TTL, flags, and sequence numbers, analysts can reconstruct network conversations, trace attacker activity, troubleshoot network problems, and investigate security incidents. Packet analysis forms the foundation for network forensics, intrusion detection, threat hunting, and incident response, making it an essential skill for anyone working in a Security Operations Center (SOC).
