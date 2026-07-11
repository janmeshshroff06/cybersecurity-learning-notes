# **2.1 Understand Network Traffic**

---

## **Overview**

* This lesson introduces how data moves across computer networks and why monitoring network traffic is essential for cybersecurity.
* You'll learn about:

  * Network traffic
  * Network traffic flows
  * Network baselines
  * Traffic analysis
  * Data exfiltration
  * Data Loss Prevention (DLP)
* Security analysts monitor network communications to detect suspicious activity, investigate incidents, and protect organizational assets.

---

## **Key Concepts**

### **The Importance of Network Traffic Flows**

#### **Network Traffic**

* **Network traffic** is:

  * The movement of data across a network.
* Data is exchanged between:

  * Computers
  * Servers
  * Mobile devices
  * Routers
  * Switches
  * Other network-connected devices
* Communication occurs through:

  * Packets
  * Network protocols

---

#### **Network Traffic Flow**

* A **network traffic flow** is:

  * The sequence of packets exchanged between communicating devices.
* A traffic flow identifies:

  * Source device
  * Destination device
  * Direction of communication
  * Amount of data transferred
* Flows allow analysts to understand:

  * Who is communicating
  * What services are being used
  * Whether communication is expected

---

#### **Why Network Traffic Matters**

* Monitoring network traffic helps organizations:

  * Detect cyberattacks
  * Identify unauthorized communications
  * Troubleshoot network issues
  * Protect sensitive information
  * Verify that systems operate normally

---

#### **Network Baseline**

* A **network baseline** is:

  * A record of normal network activity.
* Baselines include:

  * Typical users
  * Common applications
  * Expected traffic volume
  * Normal communication patterns
* Analysts compare current traffic against the baseline to identify:

  * Anomalies
  * Suspicious behavior

---

#### **Normal Network Activity**

* Every organization has:

  * Predictable communication patterns.
* Examples:

  * Employees accessing internal applications
  * Email communication
  * Web browsing
  * File sharing
  * Scheduled backups

---

#### **Abnormal Network Activity**

* Traffic that differs from the baseline may indicate:

  * Malware infections
  * Unauthorized access
  * Data exfiltration
  * Denial-of-service attacks
  * Compromised devices
  * Insider threats

---

#### **Network Monitoring**

* Security analysts continuously monitor:

  * Incoming traffic
  * Outgoing traffic
  * Internal communications
* Monitoring helps:

  * Detect attacks early
  * Investigate incidents
  * Reduce response time

---

#### **Network Visibility**

* Network visibility provides insight into:

  * Device communications
  * Application usage
  * User activity
* Better visibility enables:

  * Faster investigations
  * Better threat detection
  * Improved incident response

---

#### **Traffic Analysis**

* **Traffic analysis** involves examining network communications to identify:

  * Communication patterns
  * Suspicious connections
  * Unexpected behavior
* Analysts examine:

  * Source IP addresses
  * Destination IP addresses
  * Ports
  * Protocols
  * Packet sizes
  * Timing of communications

---

#### **Packets**

* Data travels across networks as:

  * Packets
* Each packet contains:

  * Payload (actual data)
  * Source address
  * Destination address
  * Protocol information
  * Control information
* Packets allow large amounts of data to be transmitted efficiently.

---

#### **Protocols**

* Traffic flows depend on network protocols such as:

  * TCP
  * UDP
  * HTTP
  * HTTPS
  * DNS
* Analysts often examine protocol usage when investigating suspicious activity.

---

#### **Security Monitoring**

* Continuous monitoring helps detect:

  * Unexpected connections
  * Malware communication
  * Unauthorized devices
  * Command-and-control (C2) traffic
* Early detection reduces:

  * Incident impact
  * Recovery time

---

### **Data Exfiltration Attacks**

#### **Data Exfiltration**

* **Data exfiltration** is:

  * The unauthorized movement of sensitive information outside an organization's control.
* Also known as:

  * Data theft
  * Data leakage
  * Data export
  * Data extrusion

---

#### **How Data Exfiltration Happens**

* Attackers typically:

  1. Gain unauthorized access.
  2. Locate valuable information.
  3. Collect the data.
  4. Transfer it to an external location.
* Exfiltration may occur:

  * Immediately
  * Slowly over days or weeks to avoid detection

---

#### **Information Commonly Targeted**

* Personally Identifiable Information (PII)
* Financial records
* Customer databases
* Healthcare records
* Login credentials
* Intellectual property
* Trade secrets
* Business documents

---

#### **Common Attack Methods**

* Phishing attacks
* Malware infections
* Ransomware
* Compromised user accounts
* Insider threats
* Exploited software vulnerabilities
* Misconfigured cloud storage

---

#### **Signs of Data Exfiltration**

* Large outbound data transfers
* Unusual file downloads
* Unexpected uploads
* Connections to unfamiliar external servers
* Activity outside normal business hours
* Sudden spikes in network traffic
* Unusual user behavior

---

#### **Traffic Baselines**

* Baselines help determine:

  * What normal outbound traffic looks like.
* Analysts compare:

  * Current activity
  * Historical activity
* Significant deviations may indicate:

  * Data exfiltration

---

#### **Data Loss Prevention (DLP)**

* **Data Loss Prevention (DLP)** tools:

  * Monitor sensitive information
  * Detect unauthorized transfers
  * Block prohibited data movement
* DLP solutions help protect:

  * Confidential business information
  * Customer records
  * Regulated data

---

#### **Encryption**

* Encrypting sensitive data:

  * Protects information during transmission
  * Makes stolen data difficult to read without encryption keys
* Supports:

  * Confidentiality
  * Compliance requirements

---

#### **Access Controls**

* Strong access controls reduce risk by:

  * Limiting who can view sensitive information
  * Restricting who can export data
* Organizations commonly apply:

  * Principle of Least Privilege (PoLP)
  * Multi-Factor Authentication (MFA)
  * Role-Based Access Control (RBAC)

---

#### **Analyst Responsibilities**

* Security analysts:

  * Monitor outbound traffic
  * Investigate anomalies
  * Review alerts
  * Analyze logs
  * Respond to suspected exfiltration attempts
* Documentation is essential throughout the investigation.

---

## **Importance**

* Understanding network traffic flows allows analysts to:

  * Detect threats quickly
  * Identify compromised systems
  * Investigate incidents
  * Protect organizational assets
* Network monitoring is a core responsibility within:

  * Security Operations Centers (SOCs)
  * Network security teams
* Preventing data exfiltration protects:

  * Confidentiality
  * Organizational reputation
  * Customer trust
  * Regulatory compliance
* Detecting unauthorized data movement is a major responsibility of:

  * Security analysts
  * Security Operations Centers (SOCs)

---

## **Key Takeaways**

* **Network traffic** is the movement of data between devices on a network.
* A **network traffic flow** describes how packets move between communicating systems.
* Analysts establish a **network baseline** to recognize abnormal behavior.
* Monitoring network traffic helps identify malware, unauthorized access, and other cyber threats.
* Packets carry both user data and addressing information across networks.
* Traffic analysis provides valuable evidence during security investigations.
* **Data exfiltration** is the unauthorized transfer of sensitive information outside an organization.
* Attackers commonly target PII, financial information, intellectual property, credentials, and business records.
* Signs of data exfiltration include abnormal outbound traffic, unusual file transfers, and unexpected external connections.
* **Data Loss Prevention (DLP)**, encryption, access controls, and continuous monitoring are key defenses against data theft.
* Continuous network monitoring is essential for effective threat detection and incident response.

---

## **Big Picture**

This lesson introduced how security analysts monitor **network traffic** to detect threats before they become serious incidents. By understanding normal traffic flows and establishing network baselines, analysts can quickly recognize abnormal communications that may indicate malware, unauthorized access, or **data exfiltration**. Continuous monitoring, combined with tools like **Data Loss Prevention (DLP)**, encryption, and strong access controls, helps organizations protect sensitive information and respond effectively to cyber threats.
