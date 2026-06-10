# 2.3 Authentication, Authorization, and Accounting (AAA)

## Access Controls and Authentication Systems

### Overview

* Access controls manage:

  * Access
  * Authorization
  * Accountability

* Help maintain:

  * Confidentiality
  * Integrity
  * Availability (CIA Triad)

* Organized using the:

  * Authentication
  * Authorization
  * Accounting (AAA) framework

---

### Access Controls

* Regulate:

  * Who can access information
  * What resources can be accessed
  * How user actions are tracked

* Help organizations:

  * Protect sensitive information
  * Enforce security policies
  * Reduce risk

---

### Authentication

* Authentication verifies a user's identity.

* Answers the question:

  * "Who are you?"

* Access is granted only after successful identity verification.

---

### Authentication Factors

#### Knowledge Factor

* Something the user knows.

* Examples:

  * Passwords
  * PINs
  * Security question answers

#### Ownership Factor

* Something the user possesses.

* Examples:

  * Security tokens
  * Mobile devices
  * One-Time Passcodes (OTPs)

#### Characteristic Factor

* Something the user is.

* Also called:

  * Biometrics

* Examples:

  * Fingerprints
  * Facial recognition
  * Retina scans

---

### One-Time Passcodes (OTPs)

* Temporary codes used once during authentication.

* Common delivery methods:

  * Text message
  * Email
  * Authentication apps

---

### Single Sign-On (SSO)

* Allows users to:

  * Authenticate once
  * Access multiple systems

* Reduces:

  * Login fatigue
  * Repeated authentication

---

### Benefits of SSO

* Improved convenience
* Better productivity
* Fewer passwords to manage

---

### Risks of SSO

* One compromised account may provide access to:

  * Multiple systems
  * Multiple applications

---

### Multi-Factor Authentication (MFA)

* Requires two or more authentication factors.

* Examples:

  * Password + OTP
  * Password + fingerprint
  * Security token + facial recognition

---

### Benefits of MFA

* Reduces risk from:

  * Stolen passwords
  * Credential theft
  * Unauthorized access

* Provides stronger identity verification.

---

### SSO + MFA

* Many organizations combine:

  * SSO
  * MFA

* Provides:

  * Convenience
  * Stronger security

---

## The Mechanisms of Authorization

### Overview

* Authorization determines:

  * What resources a user can access
  * What actions a user can perform

* Occurs after authentication succeeds.

* Answers the question:

  * "What are you allowed to do?"

---

### Principle of Least Privilege (PoLP)

* Users should only receive:

  * The minimum access necessary

* Access should be:

  * Limited
  * Role-based
  * Temporary when appropriate

---

### Benefits of PoLP

* Reduces:

  * Security risks
  * Insider threats
  * Accidental misuse
  * Unauthorized access

---

### Separation of Duties

* Prevents one person from having excessive control.

* Responsibilities are divided among multiple individuals.

---

### Benefits of Separation of Duties

* Reduces:

  * Fraud
  * Abuse
  * Human error
  * System failures

---

### Role-Based Authorization

* Permissions are assigned according to:

  * Job responsibilities
  * Organizational roles

* Different users receive different levels of access.

---

## Authorization Technologies

### HTTP

* Hypertext Transfer Protocol.

* Used to establish communication across networks.

* Enables:

  * Web browsing
  * Data exchange

---

### HTTP Basic Authentication (Basic Auth)

* Sends user credentials to a server.

* Credentials are transmitted during communication.

---

### Weaknesses of Basic Auth

* Credentials may be exposed.
* Vulnerable to interception.
* Considered outdated for modern security needs.

---

### HTTPS

* Hypertext Transfer Protocol Secure.

* Secure version of HTTP.

---

### Benefits of HTTPS

* Encrypts communications.

* Protects:

  * Credentials
  * Sensitive information
  * Network traffic

* Helps prevent:

  * Eavesdropping
  * Credential theft

---

### OAuth

* Open-standard authorization protocol.

* Allows secure authorization without sharing passwords.

---

### OAuth Example

* Login using:

  * Google
  * Microsoft
  * GitHub

* Third-party application verifies identity without receiving the password.

---

### API Tokens

* Small encrypted blocks of code.

* Contain information about:

  * User identity
  * Permissions
  * Access rights

---

### Benefits of API Tokens

* Reduce exposure of passwords.
* Improve authorization security.
* Support secure communication.

---

## Why We Audit User Activity

### Overview

* Accounting is the third component of AAA.

* Focuses on:

  * Monitoring activity
  * Recording access
  * Tracking system usage

---

### Accounting

* Records:

  * User actions
  * Login activity
  * Resource access

* Helps answer:

  * Who accessed a system?
  * When was it accessed?
  * What was accessed?

---

### Access Logs

* Records of user activity and system events.

* Used by analysts to:

  * Detect threats
  * Investigate incidents
  * Identify suspicious behavior

---

### Why Logs Matter

* Often the first source examined during an investigation.

* Help identify:

  * Unauthorized access
  * Failed login attempts
  * Security incidents

---

## Sessions and Session Tracking

### Session

* A sequence of requests and responses associated with one user.

* Begins when:

  * A user accesses a system

* Ends when:

  * The user logs out
  * The session expires

---

### Session ID

* Unique identifier assigned to a user session.

* Used to:

  * Track activity
  * Maintain active sessions

---

### Session Cookies

* Tokens exchanged between:

  * Browser
  * Server

* Used to:

  * Validate active sessions
  * Maintain authentication

---

### Benefits of Session Cookies

* Reduce repeated credential entry.
* Improve efficiency.
* Help maintain user sessions securely.

---

## Session Hijacking

### Overview

* Occurs when an attacker obtains a valid session ID.

* Allows the attacker to impersonate a legitimate user.

---

### Risks

* Unauthorized access
* Data theft
* Account compromise
* Access to protected systems

---

### SSO Risk

* If an SSO session is hijacked:

  * Multiple connected systems may be compromised

---

### Detecting Session Hijacking

* Analysts monitor access logs for:

  * Unusual activity
  * Unexpected locations
  * Suspicious session behavior

---

## Identity and Access Management (IAM)

### Overview

* Identity and Access Management (IAM) is a collection of processes and technologies used to manage user identities and access rights.

---

### Goals of IAM

* Verify identities
* Control access
* Enforce least privilege
* Support accountability

---

### IAM Components

* Authentication
* Authorization
* Accounting
* Access controls
* Identity management

---

### Benefits of IAM

* Improves security
* Simplifies access management
* Supports compliance requirements
* Reduces unauthorized access risks

---

## Cybersecurity Importance

* Authentication verifies identities.
* Authorization controls access.
* Accounting tracks activity.
* Together they create the AAA framework.
* IAM strengthens organizational security by managing identities and permissions.
* Logs and session tracking help analysts investigate incidents and detect threats.

---

## Key Takeaways

* AAA stands for:

  * Authentication
  * Authorization
  * Accounting

* Authentication verifies identity.

* Authorization determines permissions.

* Accounting tracks user activity.

* SSO simplifies authentication while MFA strengthens security.

* PoLP and Separation of Duties reduce risk.

* HTTPS and OAuth provide secure authorization methods.

* Access logs help investigate incidents and detect suspicious behavior.

* Session IDs and cookies maintain authenticated sessions.

* IAM helps organizations manage identities and access securely.

---

## Big Picture

The AAA framework forms the foundation of modern access control. Authentication confirms who users are, authorization determines what they can do, and accounting records their actions. Together with IAM, SSO, MFA, and secure authorization technologies like OAuth, organizations can protect sensitive assets while maintaining accountability and reducing security risks.
