# **3.1 Flaws in the System**

---

## **Vulnerability Management**

---

### **Overview**

* A **vulnerability** is a weakness that can be exploited by a threat.
* Organizations use **vulnerability management** to:

  * Identify vulnerabilities
  * Assess risks
  * Apply fixes and defenses

* The goal is to reduce risk before attackers can exploit weaknesses.

---

### **Vulnerability vs Exploit**

#### **Vulnerability**

* A weakness in:

  * Systems
  * Applications
  * Processes
  * Assets

* Creates an opportunity for attackers.

---

#### **Exploit**

* A method used to take advantage of a vulnerability.

* Allows attackers to:

  * Gain access
  * Steal data
  * Damage systems

---

### **Vulnerability Management Cycle**

#### **1. Identify Vulnerabilities**

* Discover weaknesses in:

  * Systems
  * Applications
  * Networks
  * Processes

---

#### **2. Consider Potential Exploits**

* Determine how attackers could abuse vulnerabilities.

* Helps prioritize risks.

---

#### **3. Prepare Defenses**

* Implement:

  * Security controls
  * Patches
  * Monitoring systems

* Reduce likelihood of exploitation.

---

#### **4. Evaluate Defenses**

* Assess effectiveness of protections.

* Identify gaps and areas for improvement.

---

### **Continuous Process**

* Vulnerability management never ends.

* New vulnerabilities appear regularly.

* Security teams must continually:

  * Monitor
  * Patch
  * Reassess

---

### **Zero-Day Exploits**

#### **Definition**

* An exploit targeting a vulnerability that is:

  * Unknown to defenders
  * Not yet patched

---

#### **Why Dangerous**

* Organizations have:

  * No warning
  * No available fix

* Attackers gain an advantage before defenses exist.

---

## **Defense in Depth Strategy**

---

### **Overview**

* **Defense in Depth** is a layered security approach.

* Uses multiple security controls instead of relying on a single defense.

* If one layer fails, other layers continue protecting assets.

---

### **Castle Analogy**

* Similar to a castle protected by:

  * Moats
  * Walls
  * Watchtowers
  * Guards

* Multiple defenses increase security.

---

### **Five Layers of Defense**

#### **Perimeter Layer**

* First line of defense.

* Controls external access.

**Examples:**

* Usernames
* Passwords
* Authentication systems

---

#### **Network Layer**

* Protects network communications.

**Examples:**

* Firewalls
* Traffic filtering
* Network security devices

---

#### **Endpoint Layer**

* Protects devices connected to the network.

**Examples:**

* Antivirus software
* Endpoint protection platforms
* Device security tools

---

#### **Application Layer**

* Protects software and applications.

**Examples:**

* Secure authentication
* Multi-Factor Authentication (MFA)
* Application security controls

---

#### **Data Layer**

* Protects sensitive information.

**Examples:**

* Encryption
* Data classification
* Access restrictions

---

### **Benefits**

* Reduces risk
* Limits damage from successful attacks
* Provides multiple opportunities to stop threats

---

## **Common Vulnerabilities and Exposures (CVE)**

---

### **Overview**

* The **CVE List** is a public database of known:

  * Vulnerabilities
  * Exposures

* Provides a common language for discussing security flaws.

---

### **Purpose**

* Helps organizations:

  * Identify risks
  * Prioritize remediation
  * Share vulnerability information

---

### **MITRE Corporation**

* Created and manages the CVE program.

* Introduced the CVE system in:

  * 1999

---

### **CVE Numbering Authorities (CNAs)**

* Organizations authorized to:

  * Review vulnerability reports
  * Assign CVE identifiers

---

### **CVE Identifier**

* Every approved vulnerability receives a unique ID.

**Example:**

* CVE-2026-12345

---

### **National Vulnerability Database (NVD)**

* Managed by:

  * NIST

* Provides:

  * Detailed vulnerability analysis
  * Severity information
  * Technical references

---

### **Common Vulnerability Scoring System (CVSS)**

* Measures vulnerability severity.

* Scores range from:

  * 0.0 to 10.0

---

### **Severity Levels**

#### **Low Risk**

* Below 4.0

---

#### **Medium Risk**

* 4.0 – 6.9

---

#### **High Risk**

* 7.0 – 8.9

---

#### **Critical Risk**

* 9.0 – 10.0

---

### **Why CVE and CVSS Matter**

* Help security teams:

  * Prioritize patching
  * Evaluate threats
  * Reduce organizational risk

---

## **OWASP Top 10**

---

### **Overview**

* **OWASP (Open Worldwide Application Security Project)** is a nonprofit organization focused on improving software security.

* One of its most important resources is the:

  * **OWASP Top 10**

* Lists the most critical web application security risks.

---

### **Purpose of the OWASP Top 10**

* Helps organizations:

  * Build more secure applications
  * Avoid common security mistakes
  * Prioritize application security efforts

* Frequently referenced during software development and audits.

---

### **OWASP Top 10 Vulnerabilities**

#### **Broken Access Control**

* Users gain access to resources they should not have.

* Can result in:

  * Unauthorized viewing
  * Modification
  * Deletion of data

---

#### **Cryptographic Failures**

* Weak or missing encryption.

* Often exposes:

  * PII
  * Sensitive business information

* Example:

  * Using outdated hashing algorithms like MD5.

---

#### **Injection**

* Malicious code is inserted into an application.

* Common example:

  * SQL injection

* May allow attackers to:

  * Steal data
  * Bypass authentication
  * Execute commands

---

#### **Insecure Design**

* Security was not properly considered during development.

* Missing security controls create opportunities for attacks.

---

#### **Security Misconfiguration**

* Systems are deployed with insecure settings.

**Examples:**

* Default passwords
* Unnecessary services
* Improper permissions

---

#### **Vulnerable and Outdated Components**

* Applications use software libraries containing known vulnerabilities.

* Common in open-source dependencies.

---

#### **Identification and Authentication Failures**

* Weak authentication mechanisms.

* Allows attackers to:

  * Impersonate users
  * Bypass login protections

---

#### **Software and Data Integrity Failures**

* Updates or code are not properly validated.

* Can result in:

  * Supply chain attacks

---

##### **SolarWinds Attack (2020)**

* Attackers inserted malicious code into software updates.

* Compromised many organizations through trusted updates.

---

#### **Security Logging and Monitoring Failures**

* Insufficient logging or monitoring.

* Makes attacks harder to detect and investigate.

---

#### **Server-Side Request Forgery (SSRF)**

* Attackers manipulate a server into making unauthorized requests.

* May expose internal resources and sensitive information.

---

## **Open Source Intelligence (OSINT)**

---

### **Overview**

* **OSINT (Open Source Intelligence)** is information gathered from publicly available sources.

---

### **Common Sources**

* Websites
* Social media
* News reports
* Public records
* Government databases

---

### **Cybersecurity Uses**

* Threat intelligence
* Security investigations
* Vulnerability research
* Attack surface analysis

---

### **Benefits**

* Low cost
* Easily accessible
* Valuable for proactive defense

---

## **Key Takeaways**

* Vulnerability management identifies and fixes weaknesses before they are exploited.

* Zero-day exploits target vulnerabilities before defenses are available.

* Defense in Depth uses multiple security layers to reduce risk.

* CVE provides a standardized list of known vulnerabilities.

* CVSS scores help prioritize remediation efforts.

* OWASP Top 10 highlights the most critical web application vulnerabilities.

* OSINT uses publicly available information to support security operations.

* Staying informed about vulnerabilities is essential for effective cybersecurity defense.

---

## **Big Picture**

Modern cybersecurity depends on proactively identifying weaknesses before attackers exploit them. Vulnerability management, Defense in Depth, CVE databases, OWASP guidance, and OSINT all help organizations strengthen security, prioritize risks, and build resilient systems capable of defending against evolving threats.
