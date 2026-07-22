# **Module 3.1 Incident Detection and Verification**

# **The Detection and Analysis Phase of the Lifecycle**

## **Overview**

- **Detection and Analysis** is the second phase of the:
  - NIST Incident Response Lifecycle
- During this phase, security teams:
  - Detect potential security incidents
  - Analyze security events
  - Verify whether an incident has occurred
- The primary goals are to:
  - Identify threats quickly
  - Minimize organizational impact
  - Gather enough evidence to begin containment and recovery

---

## **Key Concepts**

---

### **Detection and Analysis Phase**

- Focuses on:
  - Identifying suspicious activity
  - Investigating alerts
  - Confirming whether an event is actually a security incident
- Follows the:
  - Preparation phase
- Precedes:
  - Containment, Eradication, and Recovery

---

### **Detection**

- **Detection** is:
  - The prompt discovery of security events.
- Helps organizations:
  - Discover attacks early
  - Reduce response time
  - Prevent greater damage

---

### **Analysis**

- **Analysis** involves:
  - Investigating alerts
  - Validating evidence
  - Determining whether malicious activity occurred
- Analysts determine:
  - Scope
  - Severity
  - Business impact

---

### **Security Events**

- A **security event** is:
  - Any observable occurrence on a system or network.
- Examples:
  - Successful login
  - Password reset
  - File access
- Not every event:
  - Is a security incident

---

### **Security Incidents**

- A **security incident** is:
  - An event that threatens:
    - Confidentiality
    - Integrity
    - Availability (CIA Triad)
    - Organizational security policies
- Incidents require:
  - Investigation
  - Response

---

### **Detection Sources**

Security analysts collect information from:

- IDS
- IPS
- SIEM
- Endpoint Detection and Response (EDR)
- Antivirus software
- Firewalls
- Network and system logs
- User reports

---

### **Incident Verification**

- Analysts verify:
  - Alerts are legitimate
  - Activity is malicious
- Prevents:
  - False positives
  - Wasted incident response efforts

---

### **Incident Prioritization**

- Confirmed incidents are prioritized based on:
  - Severity
  - Scope
  - Business impact
- High-priority incidents:
  - Receive immediate attention

---

### **Incident Documentation**

- Throughout the investigation analysts document:
  - Evidence
  - Timeline
  - Observations
  - Findings
- Documentation supports:
  - Reporting
  - Future investigations
  - Legal and compliance requirements

---

### **Communication**

- Analysts communicate:
  - Incident status
  - Severity
  - Findings
- Ensures:
  - Response teams can begin containment quickly

---

### **Importance of Accuracy**

- Poor analysis may result in:
  - Missed attacks
  - Delayed responses
  - Wasted resources
- Analysts should:
  - Validate evidence
  - Confirm findings before escalating incidents

---

# **Cybersecurity Incident Detection Methods**

## **Overview**

- Organizations use multiple detection methods to:
  - Discover cyber threats
  - Verify suspicious activity
  - Improve detection accuracy
- No single tool detects every attack.
- Effective security combines:
  - Technology
  - Human expertise
  - Threat intelligence

---

## **Key Concepts**

---

### **Intrusion Detection System (IDS)**

- Detects:
  - Suspicious activity
  - Possible intrusions
- Generates:
  - Alerts for analysts

---

### **Security Information and Event Management (SIEM)**

- SIEM systems:
  - Collect logs
  - Correlate events
  - Analyze security data
- Help analysts:
  - Detect attacks faster

---

### **Limitations of Detection Tools**

- Detection tools only detect:
  - What they are configured to monitor
- Poor configuration may:
  - Miss attacks
  - Generate false positives
- Organizations should use:
  - Multiple detection methods

---

### **Threat Hunting**

- **Threat hunting** is:
  - The proactive search for hidden threats.
- Combines:
  - Human expertise
  - Security tools
- Helps discover:
  - Threats missed by automated detection

---

### **Threat Hunters**

- Threat hunters:
  - Research emerging threats
  - Analyze attacker behavior
  - Search networks for hidden compromises
- Use:
  - Threat intelligence
  - IoCs
  - IoAs
  - Machine learning

---

### **Fileless Malware**

- Fileless malware:
  - Operates in memory
  - Leaves little evidence on disk
- Difficult for:
  - Traditional signature-based detection
- Often discovered through:
  - Threat hunting

---

### **Threat Intelligence**

- **Threat intelligence** is:
  - Evidence-based information about existing or emerging threats.
- Helps organizations:
  - Understand attackers
  - Improve detection
  - Prepare defenses

---

### **Sources of Threat Intelligence**

- Industry reports
- Government advisories
- Threat data feeds
- Security vendors

---

### **Threat Data Feeds**

- Provide:
  - Known malicious IP addresses
  - Domains
  - File hashes
- Commonly used against:
  - Advanced Persistent Threats (APTs)

---

### **Advanced Persistent Threat (APT)**

- An **APT** is:
  - A long-term unauthorized presence inside a network.
- Attackers:
  - Maintain access for extended periods
  - Often steal sensitive information quietly

---

### **Threat Intelligence Platform (TIP)**

- A **TIP**:
  - Collects
  - Organizes
  - Analyzes threat intelligence
- Helps organizations:
  - Prioritize threats
  - Improve security posture

---

### **Cyber Deception**

- **Cyber deception** uses:
  - Fake systems
  - Fake resources
- Purpose:
  - Trick attackers
  - Improve detection

---

### **Honeypot**

- A **honeypot** is:
  - A decoy system intentionally designed to attract attackers.
- Helps analysts:
  - Observe attacker behavior
  - Gather intelligence
  - Detect intrusions early

---

# **Ongoing Monitoring of CI/CD**

## **Overview**

- CI/CD pipelines automate:
  - Software building
  - Testing
  - Deployment
- Continuous monitoring protects:
  - The software supply chain
- Automation helps detect:
  - Suspicious pipeline activity
  - Indicators of Compromise (IoCs)

---

## **Key Concepts**

---

### **Why Monitor CI/CD?**

- Prevent:
  - Unauthorized code changes
  - Malicious deployments
  - Supply chain attacks
- Detect:
  - Pipeline anomalies
  - Security incidents early

---

### **Common CI/CD Indicators of Compromise**

#### **Unauthorized Code Changes**

- Changes by:
  - Unauthorized developers
  - Unexpected locations
  - Unusual times

---

#### **Suspicious Deployments**

- Deployments:
  - Outside release windows
  - To unexpected environments
  - By unauthorized accounts

---

#### **Compromised Dependencies**

- Vulnerable libraries
- Unexpected dependencies
- Downloads from untrusted repositories

---

#### **Pipeline Execution Anomalies**

- Unexpected failures
- Long execution times
- Changed pipeline order

---

#### **Secrets Exposure Attempts**

- Attempts to:
  - Access secrets
  - Expose credentials
  - Hardcode secrets

---

### **Logging for CI/CD Monitoring**

Common logs include:

- Pipeline execution logs
- Code commit logs
- Access logs
- Deployment logs

---

### **SIEM Integration**

- SIEM platforms:
  - Aggregate CI/CD logs
  - Detect anomalies
  - Generate alerts
- Rules can detect:
  - Malicious file hashes
  - C2 connections
  - Secret exposure attempts

---

### **Continuous Vulnerability Scanning**

- Continuously scans:
  - CI/CD infrastructure
  - Plugins
  - Containers
- Detects:
  - Known CVEs
- Allows:
  - Rapid patching

---

# **Indicators of Compromise (IoCs)**

## **Overview**

- **Indicators of Compromise (IoCs)** are:
  - Observable evidence suggesting a security incident has occurred.
- IoCs help analysts:
  - Identify attacks
  - Investigate incidents
  - Understand attacker activity

---

## **Indicators of Attack (IoAs)**

- **Indicators of Attack (IoAs)** are:
  - Behavioral evidence of an attack in progress.
- Focus on:
  - Attacker behavior
  - Methods
  - Intentions

---

### **IoCs vs. IoAs**

| IoCs | IoAs |
| -------------------------- | ------------------------------------------------- |
| Evidence after an attack | Behavioral evidence during an attack |
| Focus on "what happened" | Focus on "how and why it is happening" |
| Examples: file hashes, IPs | Examples: suspicious processes, abnormal behavior |

---

## **Pyramid of Pain**

- Created by:
  - David J. Bianco
- Demonstrates:
  - Which IoCs are easiest or hardest for attackers to change.
- The higher the indicator:
  - The more difficult it is for attackers to adapt.

---

### **Levels of the Pyramid (Bottom → Top)**

#### **1. Hash Values**

- Malware file hashes
- Very easy for attackers to change

---

#### **2. IP Addresses**

- Malicious IP addresses
- Easily replaced

---

#### **3. Domain Names**

- Malicious domains
- Moderately easy to replace

---

#### **4. Network Artifacts**

Examples:

- User-Agent strings
- Network protocol characteristics

---

#### **5. Host Artifacts**

Examples:

- Malware filenames
- Registry keys
- System changes

---

#### **6. Tools**

Examples:

- Password crackers
- Malware frameworks
- Exploitation tools

---

#### **7. Tactics, Techniques, and Procedures (TTPs)**

- The attacker's:
  - Behavior
  - Methods
  - Strategy
- Hardest for attackers to change.
- Most valuable indicator for defenders.

---

## **Importance in Cybersecurity**

- Detection combines:
  - Technology
  - Human expertise
  - Threat intelligence
- Analysts continuously:
  - Monitor
  - Investigate
  - Validate alerts
- IoCs and IoAs help:
  - Detect attacks
  - Understand attacker behavior
  - Improve future defenses
- Threat hunting and cyber deception provide:
  - Additional layers of proactive security

---

## **Key Takeaways**

- Detection and Analysis is the second phase of the NIST Incident Response Lifecycle.
- Organizations detect threats using IDS, SIEM, logs, EDR, antivirus, firewalls, and user reports.
- Threat hunting proactively searches for hidden threats missed by automated tools.
- Threat intelligence provides evidence-based information about emerging threats.
- Honeypots use deception to detect attacker activity.
- Continuous CI/CD monitoring helps secure the software supply chain through automated anomaly detection.
- Indicators of Compromise (IoCs) are evidence of attacks, while Indicators of Attack (IoAs) describe attacker behavior.
- The Pyramid of Pain ranks IoCs by how difficult they are for attackers to change, with TTPs being the most valuable indicators.
- Combining automated detection, human analysis, and continuous monitoring enables faster and more effective incident response.

---

## **Big Picture**

This section focused on **detecting, verifying, and investigating cybersecurity incidents**. You learned how analysts use detection tools, threat hunting, threat intelligence, honeypots, and continuous CI/CD monitoring to identify threats before they cause significant damage. You also learned the difference between **Indicators of Compromise (IoCs)** and **Indicators of Attack (IoAs)** and how the **Pyramid of Pain** helps defenders prioritize indicators that are hardest for attackers to change. Together, these concepts form the foundation of modern incident detection, threat hunting, and proactive cyber defense.
