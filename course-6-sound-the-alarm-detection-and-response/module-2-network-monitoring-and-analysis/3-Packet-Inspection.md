# Module **2.3 Packet Inspection**

---

# **Packet Captures with tcpdump**

## **Overview**

- **tcpdump** is a command-line network protocol analyzer used to:
  - Capture network traffic
  - Inspect packets
  - Analyze network communications
- It is widely used by:
  - Security analysts
  - Network administrators
  - Incident responders
- Captured traffic can be:
  - Viewed in real time
  - Saved for later forensic analysis
- tcpdump is lightweight and commonly pre-installed on:
  - Linux
  - macOS
  - Other Unix-based operating systems

---

## **Key Concepts**

---

### **tcpdump**

- **tcpdump** is:
  - An open-source command-line packet analyzer
- It captures:
  - Network packets
  - Packet headers
  - Packet information
- Used to:
  - Monitor traffic
  - Troubleshoot networks
  - Investigate security incidents

---

### **Network Protocol Analyzer**

- A **network protocol analyzer** (packet sniffer) is a tool used to:
  - Capture network traffic
  - Analyze packets
- Examples:
  - tcpdump
  - Wireshark

---

### **Packet Sniffing**

- **Packet sniffing** is:
  - Capturing and inspecting packets traveling across a network
- Helps analysts:
  - Detect malicious activity
  - Monitor communications
  - Investigate incidents

---

### **Network Interface**

- A **network interface** is:
  - The connection point between a device and a network
- Before capturing traffic:
  - Analysts choose which interface to monitor
- Examples:
  - Ethernet
  - Wi-Fi
  - Any interface (`any`)

---

### **Running tcpdump**

- Basic syntax:

```bash
sudo tcpdump [-i interface] [options] [expressions]
```

- **sudo**
  - Runs tcpdump with administrator privileges.
- Required because:
  - Capturing packets requires elevated permissions.

---

### **Listing Interfaces**

- Display available interfaces:

```bash
tcpdump -D
```

- Helps determine:
  - Which interface to monitor

---

### **Capturing Traffic**

- Capture packets on all interfaces:

```bash
sudo tcpdump -i any
```

- Capture packets on a specific interface:

```bash
sudo tcpdump -i eth0
```

---

### **Saving Packet Captures**

- Save captured packets to a PCAP file:

```bash
sudo tcpdump -i any -w packetcapture.pcap
```

- PCAP files can later be opened using:
  - tcpdump
  - Wireshark

---

### **Reading a PCAP File**

- Read a saved packet capture:

```bash
sudo tcpdump -r packetcapture.pcap
```

---

### **Verbose Output (-v)**

- By default:
  - tcpdump does not display every packet detail.
- The **-v** option increases detail.
- Three verbosity levels:
  - -v
  - -vv
  - -vvv
- Higher verbosity displays:
  - More packet header information

Example:

```bash
sudo tcpdump -r packetcapture.pcap -v
```

---

### **Count Option (-c)**

- Limits the number of packets captured.

Example:

```bash
sudo tcpdump -i any -c 3
```

- Captures:
  - Only the first three packets

---

### **Disable Name Resolution (-n)**

- Normally tcpdump converts:
  - IP addresses → Hostnames
  - Port numbers → Service names
- This may:
  - Produce misleading output
  - Alert attackers through reverse DNS lookups
- Best practice:

```bash
-n
```

- Prevents hostname resolution.

```bash
-nn
```

- Prevents both:
  - Hostname resolution
  - Port/service resolution

Example:

```bash
sudo tcpdump -r packetcapture.pcap -vn
```

---

### **Combining Options**

- Multiple options can be combined.

Example:

```bash
-vn
```

instead of

```bash
-v -n
```

---

### **Filtering Traffic**

- tcpdump supports expressions that filter captured traffic.

Examples:

```bash
ip6
```

Capture only IPv6 traffic.

```bash
port 80
```

Capture HTTP port traffic.

```bash
host 192.168.1.10
```

Capture traffic involving a specific host.

---

### **Boolean Operators**

- Expressions support:
  - and
  - or
  - not

Example:

```bash
sudo tcpdump -r packetcapture.pcap -n 'ip and port 80'
```

Example:

```bash
ip and (port 80 or port 443)
```

Captures:

- IPv4 traffic
- HTTP or HTTPS traffic

---

### **Packet Capture Files (PCAP)**

- PCAP files contain:
  - Captured packets
- Used for:
  - Incident response
  - Threat hunting
  - Digital forensics
  - Troubleshooting

---

### **Interpreting tcpdump Output**

Each captured packet displays:

- Timestamp
- Source IP address
- Source port
- Destination IP address
- Destination port
- Protocol information
- Additional packet details (depending on verbosity)

---

### **Timestamp**

Shows:

- When the packet was captured

Useful for:

- Building attack timelines

---

### **Source IP**

Identifies:

- Where the packet originated

---

### **Destination IP**

Identifies:

- Where the packet is going

---

### **Source Port**

Identifies:

- The sending application or service

---

### **Destination Port**

Identifies:

- The receiving application or service

---

### **Encrypted Traffic**

- Much network traffic is:
  - Encrypted
- Viewing packet contents may require:
  - Appropriate private keys
  - Decryption

---

### **Why tcpdump Matters**

- tcpdump allows analysts to:
  - Capture live traffic
  - Save forensic evidence
  - Filter suspicious packets
  - Troubleshoot connectivity
  - Investigate attacks

---

## **tcpdump vs. Wireshark**

| tcpdump                     | Wireshark                     |
| --------------------------- | ----------------------------- |
| Command-line tool           | Graphical interface           |
| Lightweight                 | Feature-rich                  |
| Excellent on remote servers | Easier for deep analysis      |
| Captures traffic            | Opens and analyzes PCAP files |
| Fast and scriptable         | Better visualization          |

---

## **Importance in Cybersecurity**

- tcpdump is one of the most widely used packet analysis tools.
- Security analysts use it to:
  - Capture network traffic
  - Investigate incidents
  - Detect malicious communications
  - Collect forensic evidence
- Understanding tcpdump is a foundational networking skill for SOC analysts and incident responders.

---

## **Key Takeaways**

- tcpdump is an open-source command-line packet analyzer.
- Packet sniffing is the process of capturing and inspecting network packets.
- Packet captures can be saved as PCAP files for later analysis.
- Common commands include:
  - `tcpdump`
  - `tcpdump -D`
  - `tcpdump -i <interface>`
  - `tcpdump -w <file>`
  - `tcpdump -r <file>`
- Useful options include:
  - `-v` (verbose)
  - `-c` (packet count)
  - `-n` (disable name resolution)
- Filter expressions allow analysts to capture only relevant traffic.
- tcpdump displays important packet information such as timestamps, IP addresses, ports, and protocols.
- tcpdump is essential for network monitoring, threat detection, troubleshooting, incident response, and digital forensics.

---

## **Big Picture**

This section introduced **tcpdump**, one of the most important command-line tools used by cybersecurity professionals to capture and inspect network traffic. You learned how to capture packets from specific network interfaces, save them as **PCAP files**, read existing captures, filter traffic using protocols, ports, hosts, and Boolean expressions, and interpret tcpdump output. You also learned best practices such as using `-n` to disable name resolution and using verbosity levels (`-v`, `-vv`, `-vvv`) for more packet details. Together with Wireshark, tcpdump is a core tool for network monitoring, incident response, threat hunting, and digital forensics.
