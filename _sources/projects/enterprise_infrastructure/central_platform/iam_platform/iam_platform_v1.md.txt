
# IAM Platform — Version 1

## Overview

Version 1 is a small, self-built Identity and Access Management (IAM) platform designed to explore the fundamentals of identity, authentication, authorization, and secure application design.

The purpose of the project is not to reproduce a production IAM product, but to understand how the underlying security mechanisms work by designing and implementing them directly.

The implementation uses **Python, FastAPI, PostgreSQL, Docker Compose, and pytest**.

The V1 system provides a complete authentication and authorization flow:

```text
Request
   ↓
Authentication / Session Validation
   ↓
Identify User
   ↓
Authorization
   ↓
Protected Operation
   ↓
Audit Security-Relevant Result
   ↓
Response
```

The project therefore goes beyond implementing CRUD endpoints. Security controls are part of the application's control flow and are tested as security properties.

## Scope

V1 implements:

* Users
* Groups
* Roles
* Permissions
* User/group relationships
* User/role relationships
* Role/permission relationships
* Username/password authentication
* Secure password hashing
* Login failure protection and throttling
* Server-side sessions
* Session expiration and revocation
* Logout
* Role-Based Access Control (RBAC)
* Protected application resources
* Protected IAM administration
* Bootstrap administrator
* Security audit logging
* Security-focused automated tests
* Architecture and security documentation
* Threat modeling

The authorization model is deliberately kept simple:

```text
User
  ↓
Roles
  ↓
Role Permissions
  ↓
Effective Permissions
  ↓
ALLOW / DENY
```

Groups are implemented as an identity-management capability but do not directly grant permissions in V1. This leaves room for future group-to-role mappings without complicating the initial authorization model.

## Security Engineering

A major objective of V1 is to understand the difference between **implementing a security feature** and **demonstrating that the feature actually provides its intended security property**.

For example, implementing authorization is only part of the work. The project also tests whether an authenticated user can:

* access resources belonging to another user
* modify their own privileges
* assign themselves an administrator role
* grant themselves privileged permissions
* bypass authorization by manipulating object IDs
* access administrative endpoints without sufficient privileges
* perform protected operations without the required permission

Security tests therefore attempt to violate the intended security boundaries rather than only testing normal application behavior.

A key security invariant is:

```text
Authentication
      ↓
Authorization
      ↓
Prevent unauthorized operation
      ↓
Execute authorized operation
      ↓
Audit result
```

An authorization failure must prevent the protected operation from executing. The audit trail records the security-relevant result but does not act as the preventative control itself.

## Authentication and Sessions

Authentication uses username/password credentials with an established password-hashing library.

Successful authentication creates a cryptographically random, server-side session.

Sessions support:

* expiration
* revocation
* logout
* invalid-session rejection
* protection against session fixation
* rejection of predictable session identifiers

Authentication failures are deliberately generic so that the system does not reveal whether a particular username exists.

Login failure protection and throttling are also implemented as application-level security controls.

## Authorization

Authorization is implemented using RBAC.

Permissions represent specific actions on resources, for example:

```text
application:read
application:create
application:update
application:delete
application:deploy
iam:manage
```

Authorization decisions are centralized conceptually around:

```text
authorize(user_id, resource, action)
```

The application resolves the user's roles and their associated permissions before allowing a protected operation to execute.

The V1 design deliberately avoids introducing a complex policy framework. The goal is to make the authorization mechanism easy to understand, trace, test, and eventually extend.

## IAM Administration

IAM administration is itself protected by the IAM system.

An `Administrator` role is assigned the:

```text
iam:manage
```

permission.

Administrative operations such as creating users, assigning roles, modifying permissions, and managing group membership therefore require both:

```text
Authenticated session
        +
Appropriate authorization
```

This also provides a practical environment for testing privilege-escalation scenarios.

## Audit Logging

Security audit logging is treated separately from ordinary application/debug logging.

Security-relevant events include:

* successful and failed authentication
* logout and session revocation
* user changes
* group changes
* role changes
* permission changes
* role and permission assignments
* authorization failures
* security-sensitive operations

Audit records are generated by trusted server-side code. Clients cannot submit arbitrary audit events or modify the audit trail through the normal API.

The audit trail is designed to answer:

```text
Who?
What?
When?
Against what?
What was the result?
```

Sensitive information such as passwords, password hashes, session identifiers, authentication tokens, and secrets is never logged.

## Threat Modeling and Secure Development

The implementation follows a small secure-development lifecycle rather than treating security as a final testing step:

```text
Design
   ↓
Identify security risks
   ↓
Design security control
   ↓
Implement
   ↓
Functional tests
   ↓
Security tests
   ↓
Attempt to bypass
   ↓
Fix
   ↓
Regression test
```

The project uses principles from OWASP, ASVS, NIST SSDF, and CWE as guidance for the implementation and security review.

The threat model considers threats including:

* credential attacks
* authentication bypass
* session theft and fixation
* IDOR
* horizontal privilege escalation
* vertical privilege escalation
* SQL injection
* malicious input
* audit manipulation
* information disclosure
* login-based denial of service
* compromised administrator accounts

## Why Build IAM From Scratch?

The objective is primarily educational.

Using an existing IAM product would provide a much larger feature set, but it would hide many of the implementation details that this project is intended to explore.

By implementing a deliberately small IAM system first, I can understand:

* how authentication establishes identity
* how sessions maintain authenticated state
* how authorization decisions are made
* how RBAC is represented in a database
* where security controls belong in the request flow
* how privilege boundaries can fail
* how security events should be recorded
* how security controls can be tested
* how an IAM component could eventually integrate with a larger enterprise platform

This implementation is therefore intentionally limited.

Features such as MFA, OIDC, LDAP, Kerberos, WebAuthn/passkeys, SCIM, JIT/PIM, workload identity, Vault, and PKI are outside the scope of V1.

They are potential future extensions once the fundamentals have been understood and tested.

## V1 Outcome

The result is a small but complete IAM system that can be recreated from scratch and used as a foundation for further security engineering work.

More importantly, V1 establishes the security model that later versions can build upon:

```text
Identity
   ↓
Authentication
   ↓
Session
   ↓
Authorization
   ↓
Protected Resource
   ↓
Audit
```

The next step is not simply to add more IAM features, but to build upon this foundation with stronger security testing, automated security tooling, and eventually DevSecOps practices around the system.
