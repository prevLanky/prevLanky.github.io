Security engineering
==================

# CIA / DAD

## Confidentiality
Confidentiality is about making sure information is only accessible to people or systems that are authorized to see it.  
This is usually achieved through access controls, encryption, and proper authentication.  
Example: Encrypting a database so only authorized applications can read customer data.

## Integrity
Integrity ensures that data is accurate, complete, and has not been modified without authorization.  
Mechanisms like hashing, checksums, and digital signatures are commonly used.  
Example: Using file hashes to detect whether a configuration file has been tampered with.

## Availability
Availability means that systems and data are accessible when needed by authorized users.  
This often involves redundancy, backups, and protection against denial-of-service attacks.  
Example: Using load balancers and failover systems to keep a website online.

## Authenticity
Authenticity is about confirming that users, devices, or systems are who they claim to be.  
This is typically enforced through authentication mechanisms.  
Example: Using certificates to verify the identity of a server.

## Nonrepudiation
Nonrepudiation ensures that a user cannot deny having performed an action.  
This is commonly achieved through logging and digital signatures.  
Example: Digitally signing a transaction so the sender cannot later deny sending it.

## Disclosure
Disclosure refers to the unauthorized exposure of information.  
This is a violation of confidentiality.  
Example: Sensitive files being leaked due to misconfigured cloud storage.

## Alteration
Alteration occurs when data is changed without authorization.  
This is a violation of integrity.  
Example: An attacker modifying transaction amounts in a database.

## Destruction / Denial
Destruction or denial refers to data or services being made unavailable.  
This is a violation of availability.  
Example: Ransomware encrypting files or a DDoS attack taking down a service.


# Asset management
An organization can only protect assets that it knows about. Asset management focuses on identifying, classifying, and tracking all assets.

A CMDB (Configuration Management Database) is used to document systems, configurations, and dependencies.

An SBOM (Software Bill of Materials) lists all software components and libraries used in an application, helping manage supply chain risks.  
Example: Knowing which applications are affected by a vulnerable open-source library.


# Security Assessment
Security assessments evaluate how well security controls are working.  
They may include vulnerability scanning, penetration testing, architecture reviews, and configuration audits.  
Example: Running a penetration test before releasing a new application.


# Security Models

## Bell-LaPadula Model
This model focuses on confidentiality and access control based on security levels (e.g., classified vs unclassified).

### Pros & Cons
**Pros**
- Strong focus on confidentiality  
- Clear access rules  

**Cons**
- Ignores integrity  
- Not practical for many modern systems  

## The Biba Integrity Model
The Biba model focuses on protecting data integrity by preventing unauthorized modification.

### Pros & Cons
**Pros**
- Strong integrity guarantees  
- Useful for systems where data accuracy is critical  

**Cons**
- Can be too restrictive  
- Does not address confidentiality  

## The Clark-Wilson Model
This model enforces integrity using controlled processes, separation of duties, and well-defined transactions.

### Pros & Cons
**Pros**
- Practical for commercial systems  
- Supports auditing and accountability  

**Cons**
- More complex to implement  
- Requires well-defined processes  


# Security Principles

## Security By Design
Security should be considered from the start of system design, not added later.  
This reduces vulnerabilities and long-term costs.

### Pros & Cons
**Pros**
- Fewer security gaps  
- Cheaper than fixing issues later  

**Cons**
- Requires more planning  
- May slow early development  

## Defence-In-Depth
Defence-in-Depth uses multiple layers of security controls. If one layer fails, others still provide protection.

### Pros & Cons
**Pros**
- Reduces impact of single failures  
- Improves overall resilience  

**Cons**
- Increased complexity  
- Higher cost and maintenance  

## Zero Trust vs Trust but Verify

### Zero Trust
Zero Trust assumes no implicit trust. Every access request must be verified, regardless of network location or device ownership.  
Authentication, authorization, and continuous monitoring are required.

Example: Requiring MFA and device checks before accessing internal systems.

### Trust but Verify
Trust but Verify allows initial trust but relies on monitoring and logging to detect misuse.  
Automation is required since manual review is not feasible.

Example: Allowing employee access but monitoring logs for suspicious activity.

### Pros & Cons
**Zero Trust Pros**
- Limits breach impact  
- Strong against insider threats  

**Zero Trust Cons**
- Complex to implement  
- Can affect user experience  

**Trust but Verify Pros**
- Easier to adopt  
- Less disruptive  

**Trust but Verify Cons**
- Relies heavily on detection  
- Attacks may succeed before being noticed  


# GRC

## Governance
Governance defines how security decisions are made and enforced.  
Sometimes business needs require exceptions to policies. These exceptions must be formally approved and mitigations applied to reduce risk.

### COBIT, what else?
Other common frameworks include ITIL, ISO 27001, and internal governance models.

## Risk
Risk management identifies threats, vulnerabilities, and potential impacts, then decides how to treat the risk.

### NIST SP 800 – Risk analysis and patch management
NIST SP 800 provides guidance on identifying risks and managing vulnerabilities through regular patching and updates.

## Compliance
Compliance ensures adherence to laws, regulations, and standards such as GDPR, PCI DSS, or ISO 27001.

## Assurance
Assurance provides confidence that security controls are effective.  
It is achieved through audits, testing, monitoring, and reporting.

The required level of assurance depends on exposure and potential impact.  
Example: A public-facing payment system requires higher assurance than an internal test environment.


# Change Management
Change management ensures security is maintained as systems evolve. Any change should be assessed for security impact.

For example, upgrading an e-commerce system requires risk assessment, vulnerability scanning, and penetration testing before deployment. The goal is to ensure the change does not introduce new vulnerabilities and remains compliant with security policies.
