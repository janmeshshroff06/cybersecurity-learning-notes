# 2.2 Encryption Methods

## Fundamentals of Cryptography

### Overview

* Cryptography is a security control used to protect sensitive information.
* It helps ensure that only authorized users can access protected data.
* Commonly used to protect:

  * Personally Identifiable Information (PII)
  * Financial information
  * Medical records
  * Online communications

---

### Personally Identifiable Information (PII)

* Information that can identify an individual.

* Examples:

  * Names
  * Email addresses
  * Phone numbers
  * Financial information
  * Medical records
  * Fingerprints
  * Photographs

---

### Cryptography

* The process of transforming information into a form unauthorized users cannot understand.

* Used to:

  * Protect privacy
  * Secure communications
  * Safeguard sensitive information

---

### Encryption

* Converts readable information into an unreadable format.

* Protects data from unauthorized access.

* Encrypted data becomes:

  * Ciphertext

---

### Decryption

* Converts encrypted data back into readable information.

* Allows authorized users to access the original data.

---

### Plaintext and Ciphertext

#### Plaintext

* Original readable data before encryption.

#### Ciphertext

* Encrypted unreadable data after encryption.

---

### Encryption Process

* Plaintext → Encryption → Ciphertext

* Ciphertext → Decryption → Plaintext

---

### Algorithms

* A set of rules used to solve a problem.

* In cryptography:

  * Used to encrypt information
  * Used to decrypt information

---

### Ciphers

* A cryptographic algorithm used for encryption.

* Example:

  * Caesar Cipher

---

### Caesar Cipher

* One of the earliest encryption methods.

* Named after:

  * Julius Caesar

* Uses letter shifting to encrypt messages.

---

### Example

Using a shift of 3:

* A → D
* B → E
* C → F

Example:

* HELLO → KHOOR

---

### Cryptographic Keys

* A mechanism used to:

  * Encrypt data
  * Decrypt data

* Controls how encryption is performed.

---

### Brute Force Attacks

* Trial-and-error process used to discover:

  * Passwords
  * Encryption keys
  * Hidden information

---

### Key Management

* Keys should:

  * Be protected carefully
  * Never be stored publicly
  * Be shared securely

* Strong key management is critical for security.

---

### Modern Cryptography

* Uses stronger algorithms and larger key sizes.

* Designed to:

  * Resist brute force attacks
  * Protect online communications
  * Secure sensitive data

---

## Public Key Infrastructure (PKI)

### Overview

* Public Key Infrastructure (PKI) is a framework used to secure online communications.

* Combines:

  * Encryption
  * Identity verification
  * Digital certificates

* Establishes trust between communicating parties.

---

### What is PKI?

* A system that:

  * Secures online communication
  * Verifies identities
  * Protects encrypted data exchanges

---

### Two Major Functions

* Encryption
* Trust verification

---

## Asymmetric Encryption

### Overview

* Uses two separate keys:

  * Public key
  * Private key

---

### Public Key

* Can be shared openly.

* Used to:

  * Encrypt information

---

### Private Key

* Secret key owned by the recipient.

* Used to:

  * Decrypt information

---

### Advantages

* Strong security
* Secure communication between unknown parties

---

### Disadvantages

* Slower than symmetric encryption
* Requires more computing power

---

## Symmetric Encryption

### Overview

* Uses one shared secret key.

* Same key performs:

  * Encryption
  * Decryption

---

### Advantages

* Faster than asymmetric encryption
* Requires fewer resources
* Efficient for large amounts of data

---

### Disadvantages

* Shared key must be distributed securely.

* If the key is stolen:

  * Data may be compromised

---

## Combining Both Methods

### How PKI Uses Encryption

* Asymmetric encryption:

  * Establishes secure communication

* Symmetric encryption:

  * Handles ongoing communication

---

### Benefits

* Strong security
* Better performance
* Faster communications

---

## Digital Certificates

### Overview

* Digital certificates verify the identity of a public key owner.

* Function like a digital ID card.

---

### Purpose

* Establish trust between systems.

* Verify identities online.

---

## Certificate Authorities (CAs)

### Overview

* Trusted organizations that:

  * Verify identities
  * Issue digital certificates

---

### Responsibilities

* Confirm ownership of public keys.
* Create trusted digital certificates.
* Act as trusted third parties.

---

## Digital Signatures

### Overview

* Verify:

  * Authenticity
  * Integrity

---

### Purpose

* Prove information came from a trusted source.
* Ensure information has not been altered.

---

### PKI in Everyday Life

* HTTPS websites
* Online banking
* Secure email
* Mobile messaging applications

---

## Symmetric and Asymmetric Encryption

### Comparison

| Symmetric Encryption | Asymmetric Encryption |
| -------------------- | --------------------- |
| One shared key | Public and private key pair |
| Faster | Slower |
| Less resource intensive | More resource intensive |
| Good for large amounts of data | Good for secure key exchange |
| Lower computational cost | Higher computational cost |

---

### When Each is Used

#### Symmetric

* File encryption
* Data storage
* Large data transfers

#### Asymmetric

* Secure connections
* Identity verification
* Digital certificates
* Key exchange

---

## Non-Repudiation and Hashing

### Overview

* Encryption protects confidentiality.

* Hashing helps verify:

  * Integrity
  * Authenticity
  * Non-repudiation

---

### Hash Functions

* Algorithms that generate unique outputs from input data.

* One-way process:

  * Cannot be reversed

---

### Hash Values (Digests)

* Output generated by a hash function.

* Acts like a:

  * Digital fingerprint

---

### One-Way Process

* Original data cannot be reconstructed from the hash value.

---

### Data Integrity

* Ensures information remains:

  * Accurate
  * Consistent
  * Unmodified

---

### File Integrity Verification

* If a file changes:

  * Its hash value changes

* Even tiny changes create completely different hashes.

---

### Avalanche Effect

* Small changes in input create large changes in output.

* Helps detect unauthorized modifications.

---

## Non-Repudiation

### Definition

* Ensures authenticity cannot be denied.

* Provides evidence that:

  * Information is genuine
  * Information has not been altered

---

### Why It Matters

* Creates trust in digital systems.

* Supports accountability.

---

## Hashing Algorithms

### MD5

* Older hashing algorithm.

* No longer considered secure for many applications.

---

### SHA-256

* Common modern hashing algorithm.

* Frequently used for:

  * Integrity verification
  * Security monitoring
  * Malware analysis

---

## Hashing in Linux

### Generate a Hash

```bash
sha256sum filename.txt
```

---

### Purpose

* Verify file integrity.

* Compare files against trusted versions.

---

## VirusTotal

### Overview

* Security tool used to analyze:

  * Files
  * URLs
  * Domains
  * IP addresses

---

### How Analysts Use It

* Compare file hashes against known malware databases.

* Investigate suspicious files.

---

## Cybersecurity Importance

* Cryptography protects confidentiality.
* PKI establishes trust online.
* Symmetric and asymmetric encryption secure communications.
* Hashing protects integrity.
* Digital signatures support non-repudiation.
* Security analysts use hashes to:

  * Detect malware
  * Verify files
  * Investigate incidents

---

## Key Takeaways

* Cryptography protects sensitive information through encryption.
* Encryption converts plaintext into ciphertext.
* PKI combines encryption and identity verification.
* Asymmetric encryption uses public/private key pairs.
* Symmetric encryption uses a shared secret key.
* Digital certificates establish trust online.
* Hashing verifies data integrity and authenticity.
* Non-repudiation prevents users from denying actions.
* SHA-256 is a commonly used hashing algorithm.
* Encryption and hashing are foundational cybersecurity controls.

---

## Big Picture

Cryptography is one of the most important security controls in cybersecurity. Encryption protects confidentiality, PKI establishes trust, digital certificates verify identities, and hashing ensures integrity. Together, these technologies secure online communications, protect sensitive data, and help organizations defend against cyber threats.
