# **3.4 Review: Vulnerabilities in Systems**

---

## **Module Overview**

---

### **What You Learned**

* Vulnerabilities are weaknesses that attackers can exploit.

* Organizations use multiple strategies to:

  * Identify vulnerabilities
  * Assess risk
  * Reduce exposure
  * Strengthen defenses

* Security professionals must think proactively to:

  * Prevent attacks
  * Minimize damage
  * Improve security posture

---

## **Flaws in the System**

---

### **Vulnerability Management**

* Vulnerability management is the continuous process of:

  * Identifying vulnerabilities
  * Assessing risk
  * Prioritizing threats
  * Applying fixes

* Goal:

  * Reduce opportunities for attackers

---

### **CI/CD Vulnerabilities**

* CI/CD (Continuous Integration / Continuous Delivery) helps automate software development.

* Risks include:

  * Insecure code
  * Misconfigured pipelines
  * Weak access controls
  * Unverified software updates

* Secure development practices help reduce these risks.

---

### **Defense in Depth**

* Defense in depth uses:

  * Multiple layers of security controls

* If one security control fails:

  * Additional controls remain in place

* Examples:

  * Firewalls
  * MFA
  * Encryption
  * Monitoring tools
  * Access controls

---

### **Common Vulnerabilities and Exposures (CVE)**

* CVE is a public database of:

  * Known vulnerabilities
  * Security exposures

* Used by:

  * Security analysts
  * Organizations
  * Vendors

* Helps security teams:

  * Track threats
  * Prioritize remediation

---

### **OWASP Top 10**

* OWASP (Open Worldwide Application Security Project) publishes the:

  * Top 10 most critical web application vulnerabilities

* Frequently referenced during:

  * Application development
  * Security audits
  * Security testing

---

### **Major OWASP Top 10 Vulnerabilities**

#### **Broken Access Control**

* Users gain access to resources they should not access.

---

#### **Cryptographic Failures**

* Weak or missing encryption exposes sensitive data.

---

#### **Injection**

* Malicious code inserted into an application.

**Examples:**

* SQL Injection
* Command Injection

---

#### **Insecure Design**

* Security controls missing during application development.

---

#### **Security Misconfiguration**

* Incorrect security settings create vulnerabilities.

**Example:**

* Default passwords
* Default server settings

---

#### **Vulnerable and Outdated Components**

* Old software contains known security flaws.

---

#### **Identification and Authentication Failures**

* Weak authentication mechanisms allow unauthorized access.

---

#### **Software and Data Integrity Failures**

* Updates and code changes are not properly validated.

**Example:**

* Supply chain attacks

---

#### **Security Logging and Monitoring Failures**

* Lack of monitoring delays threat detection.

---

#### **Server-Side Request Forgery (SSRF)**

* Attackers force a server to access unauthorized resources.

---

## **Cyber Attacker Mindset**

---

### **Attack Surface**

* An attack surface includes:

  * All possible vulnerabilities
  * All potential entry points

* Two main types:

  * Physical attack surface
  * Digital attack surface

---

### **Security Hardening**

* Process of reducing vulnerabilities.

**Goals:**

* Reduce attack surface
* Strengthen defenses
* Prevent exploitation

---

### **Attack Vectors**

* Pathways attackers use to gain access.

**Examples:**

* Email
* USB drives
* Social media
* Cloud services

---

### **Thinking Like an Attacker**

Security teams ask:

* What is the target?
* How can it be accessed?
* Which vulnerabilities exist?
* What tools would an attacker use?

---

### **Threat Actors**

Common threat actors include:

* Cybercriminals
* Nation-state actors
* Insider threats
* Hacktivists
* Script kiddies

---

### **Brute Force Attacks**

* Repeatedly attempt passwords until successful.

**Defenses:**

* MFA
* Account lockouts
* Strong password policies

---

## **Identify System Vulnerabilities**

---

### **Vulnerability Assessments**

* Internal reviews of systems and security controls.

---

### **Four-Step Assessment Process**

#### **1. Identification**

* Discover vulnerabilities.

---

#### **2. Vulnerability Analysis**

* Investigate root causes.

---

#### **3. Risk Assessment**

* Evaluate:

  * Severity
  * Likelihood

---

#### **4. Remediation**

* Fix vulnerabilities through:

  * Patches
  * Updates
  * Security controls

---

### **Vulnerability Scanning**

* Automated process used to:

  * Detect vulnerabilities
  * Identify outdated software
  * Discover security weaknesses

---

### **Importance of Updates**

* Updates often contain:

  * Security patches
  * Bug fixes

* Delayed updates increase risk.

---

### **Penetration Testing**

* Authorized simulated attack against systems.

**Purpose:**

* Identify weaknesses before attackers do.

---

## **Key Takeaways**

* Vulnerabilities are weaknesses that can be exploited by attackers.

* Vulnerability management is a continuous process of identifying and fixing security issues.

* Defense in depth uses multiple layers of protection.

* The CVE database and OWASP Top 10 help security professionals stay informed about common threats.

* Security hardening reduces attack surfaces and limits attack vectors.

* Thinking like an attacker helps identify weaknesses before they are exploited.

* Vulnerability assessments follow four steps:

  * Identification
  * Analysis
  * Risk Assessment
  * Remediation

* Regular updates, vulnerability scanning, and penetration testing are critical security practices.

---

## **Big Picture**

Cybersecurity is not just about responding to attacks—it is about finding weaknesses before attackers do. By understanding vulnerabilities, reducing attack surfaces, applying defense-in-depth strategies, and continuously assessing risk, organizations can better protect their systems and assets from evolving threats.
