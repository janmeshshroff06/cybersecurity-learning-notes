# **Module 1.1 The Incident Response Lifecycle**

---

## **Introduction to the Incident Response Lifecycle**

---

### **Overview**

- **Incident response** is the structured process of identifying, managing, and recovering from cybersecurity incidents.
- Organizations use **incident response frameworks** to:
  - Respond consistently
  - Minimize damage
  - Restore normal operations
  - Improve future security
- This course focuses on:
  - The **NIST Cybersecurity Framework (CSF)**
  - The **NIST Incident Response Lifecycle**

---

## **Key Concepts**

---

### **NIST Cybersecurity Framework (CSF)**

- The **NIST CSF** is a cybersecurity framework that helps organizations:

  - Manage cybersecurity risks
  - Improve security posture
  - Organize security activities

- It consists of five core functions:

  - **Identify**
  - **Protect**
  - **Detect**
  - **Respond**
  - **Recover**

---

### **Focus of the Course**

- This course emphasizes the last three CSF functions:

  - **Detect**
  - **Respond**
  - **Recover**

- These functions are central to:

  - Incident response
  - Security operations
  - Digital investigations

---

### **NIST Incident Response Lifecycle**

- The **NIST Incident Response Lifecycle** provides a structured process for handling cybersecurity incidents.

- It consists of four phases:

  - **Preparation**
  - **Detection and Analysis**
  - **Containment, Eradication, and Recovery**
  - **Post-Incident Activity**

---

### **Phase 1: Preparation**

- Organizations prepare **before** incidents occur.

- Includes:

  - Developing incident response plans
  - Creating playbooks
  - Defining team roles and responsibilities
  - Deploying security tools
  - Training employees
  - Establishing communication procedures
  - Performing backups

- Goal:

  - Respond quickly and effectively when an incident occurs.

---

### **Phase 2: Detection and Analysis**

- Security teams:

  - Monitor systems
  - Review alerts
  - Analyze logs
  - Investigate suspicious activity

- Determine:

  - Whether an incident has occurred
  - Scope of the incident
  - Severity
  - Affected systems
  - Potential impact

---

### **Phase 3: Containment, Eradication, and Recovery**

#### **Containment**

- Limit the spread of the attack.

- Examples:

  - Disconnect infected devices
  - Disable compromised accounts
  - Block malicious IP addresses

#### **Eradication**

- Remove the root cause.

- Examples:

  - Remove malware
  - Delete malicious files
  - Patch vulnerabilities
  - Reset compromised credentials

#### **Recovery**

- Restore affected systems safely.

- Includes:

  - Recovering from backups
  - Testing restored systems
  - Returning services to production
  - Monitoring for recurring attacks

---

### **Phase 4: Post-Incident Activity**

- Conduct a **lessons learned** review.

- Document:

  - Timeline of events
  - Root cause
  - Response actions
  - Effectiveness of controls

- Improve:

  - Policies
  - Procedures
  - Security controls
  - Future incident response plans

---

### **Incident Response Is a Cycle**

- Incident response is:

  - Continuous
  - Iterative

- Teams may revisit earlier phases as:

  - New evidence appears
  - Threats evolve
  - Additional systems are discovered to be affected

- The lifecycle supports continuous improvement.

---

### **Security Event**

- A **security event** is:

  - Any observable occurrence involving a system, network, application, or device.

- Events include:

  - Successful logins
  - Failed logins
  - File access
  - Password resets
  - Firewall alerts

- Most events are:

  - Normal system activity

- Events are recorded in:

  - System logs
  - Security logs

---

### **Security Incident**

- A **security incident** is:

  - A security event that threatens or violates:
    - Confidentiality
    - Integrity
    - Availability (CIA Triad)
    - Organizational security policies

- Examples:

  - Malware infection
  - Unauthorized account access
  - Data breach
  - Privilege escalation
  - Successful phishing attack

---

### **Events vs. Incidents**

- Every **security incident** is a:

  - Security event

- Not every **security event** is:

  - A security incident

- Analysts determine whether an event becomes an incident through investigation.

---

### **The Five W's of an Investigation**

- During investigations, analysts answer:

  - **Who** was involved?
  - **What** happened?
  - **When** did it occur?
  - **Where** did it occur?
  - **Why** did it happen?

- These questions help determine:

  - Root cause
  - Scope
  - Impact

---

### **Documentation**

- Documentation is critical throughout the incident response process.

- Analysts record:

  - Evidence
  - Observations
  - Timeline
  - Response actions
  - Decisions made

- Proper documentation helps:

  - Preserve evidence
  - Support investigations
  - Meet legal and compliance requirements
  - Improve future responses

---

### **Incident Handler's Journal**

- An **incident handler's journal** is a chronological record of an investigation.

- It typically includes:

  - Date and time
  - Description of events
  - Evidence collected
  - Actions taken
  - Investigation notes
  - Follow-up tasks

- Benefits:

  - Maintains an accurate investigation timeline
  - Improves communication among responders
  - Supports incident reports and audits

---

### **Why Incident Response Matters**

- Effective incident response helps organizations:
  - Reduce financial losses
  - Protect sensitive information
  - Restore business operations faster
  - Meet regulatory requirements
  - Improve overall cybersecurity resilience

---

## **Key Takeaways**

- The NIST Cybersecurity Framework consists of five core functions:

  - Identify
  - Protect
  - Detect
  - Respond
  - Recover

- The NIST Incident Response Lifecycle includes four phases:

  - Preparation
  - Detection and Analysis
  - Containment, Eradication, and Recovery
  - Post-Incident Activity

- Incident response is a continuous cycle that improves over time.

- Security events are observable activities, while security incidents threaten confidentiality, integrity, availability, or violate security policies.

- Every incident is an event, but not every event is an incident.

- Incident investigations focus on answering the **Five W's**:

  - Who
  - What
  - When
  - Where
  - Why

- Maintaining an **incident handler's journal** ensures accurate documentation, supports investigations, and helps improve future incident response efforts.

---

## **Big Picture**

Incident response is one of the most important responsibilities of a cybersecurity professional. Organizations cannot prevent every attack, but they can minimize damage by following a structured response process. The NIST Incident Response Lifecycle provides a repeatable framework that guides security teams from preparation through recovery while emphasizing continuous improvement. Thorough documentation, careful analysis, and lessons learned after every incident help organizations become more resilient against future cyber threats.
