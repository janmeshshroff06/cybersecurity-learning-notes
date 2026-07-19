# **Module 2.4 Review: Network Monitoring and Analysis**

## **Overview**

* Module 2 focused on:

  * Understanding network traffic
  * Capturing and analyzing packets
  * Monitoring networks for suspicious activity
  * Using packet analysis tools to investigate security incidents
* Security analysts use network traffic analysis to:

  * Detect cyber threats
  * Investigate attacks
  * Protect organizational assets

---

## **Key Concepts**

---

### **Network Traffic**

* Network traffic is:

  * The movement of data between devices on a network.
* Data is transmitted using:

  * Packets

---

### **Network Traffic Flows**

* A network traffic flow describes:

  * How packets move between communicating devices.
* Monitoring traffic flows helps analysts:

  * Detect abnormal behavior
  * Identify malicious communications

---

### **Network Monitoring**

* Network monitoring is the continuous observation of:

  * Incoming traffic
  * Outgoing traffic
  * Internal communications
* Helps organizations:

  * Detect attacks early
  * Respond quickly
  * Maintain network visibility

---

### **Traffic Baseline**

* A **traffic baseline** is:

  * A record of normal network behavior.
* Analysts compare current traffic to the baseline to:

  * Detect anomalies
  * Identify potential security incidents

---

### **Data Exfiltration**

* Data exfiltration is:

  * The unauthorized transfer of sensitive data outside an organization.
* Common indicators include:

  * Large outbound transfers
  * Unusual network activity
  * Unexpected external connections

---

### **Data Loss Prevention (DLP)**

* DLP solutions help:

  * Monitor sensitive information
  * Detect unauthorized transfers
  * Prevent confidential data from leaving the organization

---

### **Packets**

* A packet is:

  * The basic unit of network communication.
* Every packet contains:

  * Header
  * Payload

---

### **Packet Header**

* Stores routing and communication information such as:

  * Source IP address
  * Destination IP address
  * Source port
  * Destination port
  * Protocol
  * TTL
  * Sequence number
  * Checksum

---

### **Packet Payload**

* Contains:

  * The actual data being transmitted
* Examples:

  * Web pages
  * Emails
  * Files
  * Images

---

### **Packet Capture (PCAP)**

* A **PCAP** file is:

  * A recorded capture of network packets.
* Used to:

  * Review historical traffic
  * Investigate incidents
  * Perform digital forensics

---

### **Packet Analysis**

* Analysts inspect packets to determine:

  * Where traffic originated
  * Where it was sent
  * Which protocols were used
  * Whether communication is legitimate

---

### **Packet Analysis Tools**

* Common tools include:

  * Wireshark
  * tcpdump

---

### **tcpdump**

* **tcpdump** is:

  * A command-line packet analyzer.
* Used to:

  * Capture live traffic
  * Save PCAP files
  * Filter packets
  * Troubleshoot networks
  * Investigate incidents

---

### **Common tcpdump Commands**

* Capture packets:

```bash
tcpdump
```

* List interfaces:

```bash
tcpdump -D
```

* Capture from a specific interface:

```bash
tcpdump -i eth0
```

* Save to a PCAP file:

```bash
tcpdump -w capture.pcap
```

* Read a PCAP file:

```bash
tcpdump -r capture.pcap
```

---

### **Useful tcpdump Options**

* `-v`

  * Verbose output
* `-vv`

  * More detailed output
* `-vvv`

  * Maximum detail
* `-c`

  * Limit number of captured packets
* `-n`

  * Disable hostname resolution
* `-nn`

  * Disable hostname and port resolution

---

### **Packet Filters**

* Filters allow analysts to capture only relevant traffic.

Examples:

* Specific host

```bash
host 192.168.1.10
```

* Specific port

```bash
port 80
```

* IPv6 traffic

```bash
ip6
```

* Boolean expressions

```bash
ip and port 443
```

---

### **Why Packet Analysis Matters**

* Helps analysts:

  * Detect malware communications
  * Investigate security incidents
  * Trace attacker activity
  * Troubleshoot connectivity issues
  * Collect forensic evidence

---

## **Module Summary**

During this module you learned how security analysts:

* Monitor network traffic
* Establish traffic baselines
* Detect abnormal network behavior
* Investigate data exfiltration
* Capture packets using PCAP files
* Analyze packet headers and payloads
* Interpret network communications
* Use tcpdump to capture, filter, and inspect packets
* Use packet analysis during incident response and digital forensics

---

## **Key Takeaways**

* Network traffic monitoring helps detect attacks before they become major incidents.
* A traffic baseline makes abnormal behavior easier to identify.
* Data exfiltration is a major indicator of a security breach.
* Every packet contains:

  * A header
  * A payload
* Packet captures (PCAPs) provide valuable evidence during investigations.
* Packet analysis helps analysts understand network communications and identify malicious activity.
* tcpdump is an essential command-line tool for capturing, filtering, and analyzing packets.
* Network monitoring and packet analysis are foundational skills for SOC analysts, incident responders, threat hunters, and digital forensic investigators.

---

## **Big Picture**

Module 2 introduced the core networking skills every cybersecurity analyst needs. You learned how data moves through networks as packets, how to monitor normal and abnormal traffic, detect data exfiltration, capture and inspect packet data using PCAP files, and use **tcpdump** to analyze live network communications. These skills form the foundation for threat detection, incident response, digital forensics, and Security Operations Center (SOC) work, where understanding network behavior is essential for identifying and investigating cyber threats.
