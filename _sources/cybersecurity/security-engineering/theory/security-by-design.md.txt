# Security By Design
Security should be considered from the start of system design, not added later.  
This reduces vulnerabilities and long-term costs.

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