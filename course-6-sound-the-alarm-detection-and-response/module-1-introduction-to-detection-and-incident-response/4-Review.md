# **Module 1.4 Review: Introduction to Detection and Incident Response**

---

## **Overview**

- This module introduced the **incident response lifecycle** and the tools security analysts use to:

  - Detect security incidents
  - Investigate threats
  - Coordinate incident response
  - Recover affected systems

- It emphasized that successful incident response depends on:

  - Preparation
  - Communication
  - Documentation
  - Continuous improvement

- Analysts also learned how detection technologies and management platforms work together to improve organizational security.

---

## **Key Concepts**

---

### **NIST Cybersecurity Framework (CSF)**

- The NIST CSF consists of five core functions:

  - Identify
  - Protect
  - Detect
  - Respond
  - Recover

- This module focused primarily on:

  - Detect
  - Respond
  - Recover

---

### **NIST Incident Response Lifecycle**

- The lifecycle consists of four phases:

  - Preparation
  - Detection and Analysis
  - Containment, Eradication, and Recovery
  - Post-Incident Activity

- Incident response is:

  - Continuous
  - Cyclical
  - Not a one-time process

---

### **Security Events vs. Security Incidents**

#### **Security Event**

- Any observable occurrence on a system or network.

#### **Security Incident**

- An event that threatens:

  - Confidentiality
  - Integrity
  - Availability (CIA Triad)
  - Organizational security policies

- Remember:

  - Every incident is an event.
  - Not every event is an incident.

---

### **Incident Handler's Journal**

- Used to:

  - Document evidence
  - Record observations
  - Track investigation progress
  - Maintain a timeline

- Helps answer:

  - Who
  - What
  - When
  - Where
  - Why

---

### **Incident Response Teams (CSIRT)**

- A **Computer Security Incident Response Team (CSIRT)** is responsible for:

  - Detecting incidents
  - Coordinating response
  - Supporting recovery
  - Improving future security

- Effective incident response requires collaboration between:

  - Security analysts
  - Technical leads
  - Incident coordinators
  - IT teams
  - Legal teams
  - Public relations

---

### **Incident Response Plans**

- Provide standardized procedures for responding to:

  - Data breaches
  - Malware infections
  - Ransomware
  - DDoS attacks

- Typically include:

  - Policies
  - Standards
  - Procedures
  - Contact information
  - Network diagrams
  - Asset inventories
  - Response workflows

- Plans should be:

  - Tested regularly
  - Updated frequently
  - Customized to organizational needs

---

### **Documentation**

- Documentation is essential throughout incident response.

- Common documentation includes:

  - Incident handler's journals
  - Playbooks
  - Incident reports
  - Policies
  - Procedures
  - Security plans

- Effective documentation is:

  - Accurate
  - Clear
  - Consistent
  - Organized

---

### **Playbooks**

- Playbooks are:

  - Step-by-step response guides

- Help security teams:

  - Respond consistently
  - Reduce errors
  - Automate repetitive tasks

- Often integrated into:

  - SOAR platforms

---

### **Intrusion Detection System (IDS)**

- Monitors:

  - Networks
  - Systems
  - Devices

- Detects:

  - Suspicious activity

- Generates:

  - Security alerts

- Requires:

  - Human investigation

---

### **Intrusion Prevention System (IPS)**

- Performs IDS functions and additionally:

  - Automatically blocks malicious activity
  - Prevents attacks from continuing

- IPS focuses on:

  - Detection
  - Prevention

---

### **Detection Tools**

- Detection technologies help identify:

  - Malware
  - Unauthorized access
  - Network attacks
  - Suspicious behavior

- Examples include:

  - IDS
  - IPS
  - Endpoint Detection and Response (EDR)
  - Antivirus
  - Network monitoring tools

---

### **Security Information and Event Management (SIEM)**

- SIEM platforms:

  - Collect logs
  - Correlate events
  - Analyze security data
  - Generate alerts

- Improve:

  - Visibility
  - Threat detection
  - Investigations
  - Compliance

---

### **Security Events vs. Alerts**

#### **Event**

- Any recorded activity.

#### **Alert**

- Notification of suspicious activity requiring analyst attention.

- SIEM helps analysts prioritize:

  - Important alerts
  - High-risk events

---

### **Security Orchestration, Automation, and Response (SOAR)**

- SOAR platforms:

  - Automate investigations
  - Coordinate security tools
  - Execute response playbooks
  - Reduce manual work

- Benefits:

  - Faster incident response
  - Consistent workflows
  - Increased efficiency

---

### **SIEM vs. SOAR**

| **SIEM** | **SOAR** |
|-----------|-----------|
| Collects logs | Automates workflows |
| Correlates events | Executes playbooks |
| Detects threats | Coordinates response |
| Generates alerts | Performs automated actions |

---

### **SIEM + SOAR Together**

- SIEM:

  - Finds suspicious activity.

- SOAR:

  - Responds automatically.

- Together they:

  - Improve detection
  - Shorten response times
  - Reduce analyst workload
  - Strengthen security operations

---

## **Importance in Cybersecurity**

- Effective incident response depends on:

  - Planning
  - Teamwork
  - Communication
  - Documentation
  - Detection technologies
  - Automation

- Security analysts continuously:

  - Monitor systems
  - Investigate alerts
  - Document findings
  - Improve organizational defenses

- Modern Security Operations Centers (SOCs) rely heavily on:

  - IDS
  - IPS
  - SIEM
  - SOAR
  - Playbooks
  - Incident response plans

---

## **Key Takeaways**

- The NIST Incident Response Lifecycle consists of:

  - Preparation
  - Detection and Analysis
  - Containment, Eradication, and Recovery
  - Post-Incident Activity

- Incident response is a continuous improvement process.

- CSIRTs coordinate investigations and recovery efforts across multiple departments.

- Incident response plans provide standardized procedures for handling security incidents.

- Documentation, including incident handler's journals and playbooks, ensures consistent and effective investigations.

- IDS detects suspicious activity, while IPS detects and automatically blocks attacks.

- SIEM collects and analyzes logs to identify threats, while SOAR automates response actions.

- SIEM focuses on **visibility and detection**, whereas SOAR focuses on **automation and orchestration**.

- Combining skilled analysts, well-tested response plans, documentation, and modern security tools enables organizations to detect, investigate, and respond to cybersecurity incidents quickly and effectively.

---

## **Big Picture**

This module introduced the complete foundation of **incident detection and response**. You learned how organizations prepare for incidents using response plans, CSIRTs, and playbooks; how analysts distinguish between security events and true incidents; and how documentation preserves evidence throughout an investigation. You also explored the technologies that power modern Security Operations Centers—including IDS, IPS, SIEM, and SOAR—which work together to detect threats, automate repetitive tasks, and improve response speed. Together, these concepts form the core workflow that security analysts use every day to protect organizational assets and continuously strengthen cybersecurity defenses.
