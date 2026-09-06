# IAM Architecture
## What is IAM Architecture?

IAM (Identity and Access Management) is the architecture used to manage identities, authentication, authorization, access lifecycle, and accountability across an organization's systems.

A mature IAM architecture separates several different responsibilities:
- Identity management
- Authentication
- Authorization
- Identity governance
- Privileged access management
- Directory services
- Federation and SSO
- Network authentication
- Auditing and accountability

One of the most important principles in IAM is to centralize identity and identity lifecycle management while allowing individual systems to enforce their own authorization policies.

The central identity infrastructure maintains the user's identity and relevant attributes, while individual systems decide what that user is allowed to do within their own environment. This keeps the IAM architecture manageable and avoids forcing one central system to understand every permission and business rule across the organization.

A useful way to think about this is that identity should be centralized, but authorization does not necessarily need to be.

Authentication and authorization should also remain separate concepts. Authentication establishes the identity of a user, while authorization determines what that identity is permitted to access or perform.

## Security Benefits

A well-designed IAM architecture can provide several important security benefits:
- Reduced attack surface: Centralized identity management reduces the need for independent accounts and credentials across many systems.
- Least privilege: Access can be controlled based on what a user actually needs to perform their role.
- Stronger authentication: Authentication policies such as MFA can be applied consistently.
- Reliable deprovisioning: Access can be removed when an identity is disabled or no longer requires access.
- Reduced credential exposure: SSO and federation can reduce the number of credentials users need to manage.
- Better visibility: Authentication, authorization, and access changes can be logged and monitored centrally.
- Privileged access protection: Administrative access can be separated, restricted, monitored, and made temporary where appropriate.
- Improved accountability: Access and administrative actions can be associated with specific identities.
- Better access governance: Access reviews and separation of duties can help prevent excessive or inappropriate access.

The security benefit comes primarily from having consistent control over the identity lifecycle and access, rather than simply having a centralized identity database.

## Security Implications

IAM is also a critical security boundary and therefore needs to be protected accordingly.

Because many systems may depend on the central identity infrastructure, compromising it can have a significant impact. An attacker who gains control of privileged IAM accounts may be able to access multiple applications and resources.

This makes IAM infrastructure itself a high-value target.

Important security considerations include:
- Protect privileged IAM administration with strong authentication and least privilege.
- Separate administrative identities from normal user identities where appropriate.
- Monitor authentication and privileged activity.
- Protect service and machine identities.
- Carefully control federation and trust relationships.
- Minimize the identity information shared with applications.
- Regularly review access and privileges.
- Ensure deprovisioning works reliably.
- Monitor provisioning and synchronization failures.
- Protect emergency and break-glass access.
- Design IAM for high availability and recovery.
- Regularly test identity revocation and privilege removal.

Centralization also creates an availability consideration. If many systems depend on the same authentication infrastructure, an IAM outage can affect access across the organization. High availability, redundancy, recovery procedures, and appropriate emergency access therefore become important parts of the architecture.

The central IAM system should also not automatically be treated as the authority for every authorization decision. Applications and resource owners still need to enforce their own security policies where appropriate.

A good IAM architecture therefore tries to balance centralized control, local enforcement, security, availability, and operational simplicity.

## Why use it?

Without a centralized IAM architecture, organizations can end up managing identities separately across applications, databases, infrastructure, networks, and other systems.

As the organization grows, this becomes increasingly difficult to manage securely. Different systems can end up with different accounts, different access rules, and different processes for removing access.

The identity lifecycle is particularly important. When someone joins the organization, they need the appropriate access. When their responsibilities change, their access needs to change as well. When they leave, their access needs to be removed.

Without proper lifecycle management, accounts can remain active after they are no longer required. These are commonly referred to as orphaned accounts and can become an unnecessary attack path.

A centralized IAM architecture provides a consistent way to manage this lifecycle while also making it easier to enforce security controls such as strong authentication, MFA, least privilege, access reviews, separation of duties, and privileged access management.

The goal is not to centralize every security decision. Instead, the goal is to centralize the parts of identity management where central control provides the most value.

## When to use it?

IAM architecture should be used whenever an organization has multiple users, systems, applications, networks, or resources that require controlled access.

It becomes increasingly important as the organization grows and the number of identities and systems increases.

IAM is particularly important when an organization has:
- Large numbers of users
- Multiple applications
- Multiple environments
- Cloud and on-premises systems
- External users
- Contractors
- Privileged administrators
- Sensitive information
- Regulatory requirements
- Complex authorization requirements
- Multiple organizations or security domains

It is especially important for systems containing:
- Financial information
- Customer information
- Intellectual property
- Administrative interfaces
- Production infrastructure
- Security infrastructure
- Sensitive business systems

IAM should be designed around principles such as least privilege, separation of duties, strong authentication, centralized lifecycle management, and continuous monitoring.

## Provisioning vs Just-In-Time

There are two common approaches to providing identities and access to systems: provisioning and Just-In-Time (JIT) provisioning.

### Provisioning / Synchronization

With provisioning, the IAM or IGA system creates, updates, or removes an account or access assignment in a target system.

This is useful when the target system requires a local account to exist before access can be provided, or when the organization needs explicit control over the complete account lifecycle.

Provisioning provides strong lifecycle control because changes can be automatically propagated to connected systems.

The main drawback is the additional synchronization dependency. Every connected system introduces another integration that can fail, become outdated, or require maintenance.

For security-critical access, provisioning and deprovisioning should therefore be monitored and regularly tested.

### Just-In-Time Provisioning

With Just-In-Time provisioning, a local account can be created when a user successfully authenticates to a target system.
This can reduce the number of accounts that need to exist before they are actually required and can simplify access to systems that support federation.
However, JIT provisioning should not be considered a replacement for identity lifecycle management.
There must still be a reliable mechanism for ensuring that an identity that is no longer valid cannot continue accessing the system.

It is also important to distinguish between JIT provisioning and JIT privileged access.
-- JIT provisioning concerns when an account is created.
-- JIT privileged access concerns when elevated privileges are granted and how long those privileges remain active.
These are separate security mechanisms that solve different problems.

## Central Identity vs Local Authorization

A key architectural decision is determining which responsibilities belong in the central IAM infrastructure and which should remain within individual systems.
The central IAM infrastructure should generally be responsible for:
- Identity
- Identity lifecycle
- Authentication
- Relevant identity attributes
- Organizational relationships
- Central access governance

Individual systems should generally remain responsible for:
- Resource-specific authorization
- Application roles
- Business rules
- Resource permissions
- Context-specific authorization decisions

This creates a useful separation between identity authority and resource authorization.

The central IAM system does not need to understand every permission and business rule within every application. Instead, it provides the identity and relevant context to the target system, while the target system evaluates whether the requested operation should be allowed.

This is particularly important because individual applications understand their own resources and business logic better than a central IAM system ever could.

A good general principle is to centralize identity and governance, while keeping resource-specific authorization close to the resource being protected.
This also reduces unnecessary coupling between applications and the central IAM infrastructure.

## Drawbacks

Centralizing IAM provides significant security and operational benefits, but it also introduces several risks.
- Central IAM becomes a high-value target
- The central identity infrastructure becomes a critical security boundary.
- If it is compromised, an attacker may potentially gain access to multiple applications and systems.

IAM infrastructure should therefore receive strong security controls, including:
- Strong administrative authentication
- Least privilege
- Privileged access management
- Network protection
- Continuous monitoring
- Security logging
- Configuration protection
- Regular security assessments

The administrative layer protecting IAM should itself be treated as highly sensitive.

## Availability dependency

Applications that depend on centralized authentication can be affected if the IAM infrastructure becomes unavailable.
This makes the availability and resilience of IAM particularly important.

The architecture should consider:
- High availability
- Redundancy
- Disaster recovery
- Backup and recovery
- Monitoring
- Dependency management
- Emergency access procedures

The organization should also understand which systems depend on centralized authentication and what the consequences would be if that authentication service became unavailable.

## Excessive centralization

Centralizing too much can also become a problem.
Trying to manage every authorization decision centrally can create a highly complex system with strong dependencies between the IAM infrastructure and individual applications. It is generally better to centralize identity, authentication, and governance while allowing applications and resource owners to manage their own resource-specific authorization policies. This creates a more modular architecture and reduces the impact of changes within individual applications.

## Synchronization failures

Provisioning and synchronization introduce additional failure modes.
If an identity or access change is not successfully propagated to a target system, that system may contain outdated access information.
This is particularly concerning during deprovisioning because an account may remain active after access should have been revoked.
Provisioning and deprovisioning should therefore be monitored, logged, and regularly tested.

## How to configure it according to security best practices?

The exact implementation depends on the organization's environment, but the architecture should generally follow these principles:

- Establish a clearly defined authoritative source for identities.
- Give every identity a unique and stable identifier.
- Separate authentication from authorization.
- Use strong authentication, especially for privileged access.
- Apply MFA where the risk justifies it.
- Use SSO and federation where appropriate.
- Minimize the identity attributes shared with applications.
- Follow the principle of least privilege.
- Use role-based or attribute-based authorization where appropriate.
- Keep application-specific authorization policies within the application or resource domain.
- Use automated provisioning and deprovisioning where possible.
- Make deprovisioning reliable and observable.
- Prefer temporary privileged access over permanent administrative privileges.
- Implement regular access reviews for sensitive access.
- Implement separation of duties for critical operations.
- Protect emergency and break-glass access separately.
- Log authentication, authorization, provisioning, deprovisioning, and privilege changes.
- Monitor IAM infrastructure as a critical security boundary.
- Protect service identities using least-privilege principles.
- Avoid unnecessary synchronization of identity data.
- Encrypt sensitive identity information in transit and at rest.
- Design the IAM infrastructure for high availability and recovery.
- Regularly test account revocation and privilege-removal processes.
- Regularly review integrations and remove unused or obsolete connections.
- Strongly protect administrative access to the IAM infrastructure.
- Monitor changes to IAM configuration and authorization policies.
- Ensure that access decisions can be traced back to an identity, policy, and authorization event.

The overall goal should be to minimize unnecessary trust. Applications should receive only the identity information they actually need, and authorization decisions should be based on the minimum information and privileges necessary to perform the requested operation.

## How to design the component?

The IAM architecture should be separated into logical security domains.

```{graphviz}
:caption: High-Level IAM Architecture
:align: center
digraph architecture {

    rankdir=TB

    fontname="Helvetica"

    node [
        shape=box
        style="rounded,filled"
        fontname="Helvetica"
    ]

    edge [
        fontname="Helvetica"
    ]

    identity [
        label="Central Identity\nIdentity + Attributes",
        fillcolor="#D5F5E3"
    ]

    authentication [
        label="Authentication\nMFA / SSO / Federation",
        fillcolor="#D7BDE2"
    ]

    iga [
        label="IGA\nIdentity Governance\n& Lifecycle",
        fillcolor="#F9E79F"
    ]

    provisioning [
        label="Provisioning\nCreate / Update / Revoke",
        fillcolor="#F9E79F"
    ]

    application [
        label="Application / Resource",
        fillcolor="#D7BDE2"
    ]

    authorization [
        label="Local Authorization\nRBAC / ABAC / Policy",
        fillcolor="#F9E79F"
    ]

    identity -> authentication [
        label="Identity"
    ]

    identity -> iga [
        label="Lifecycle"
    ]

    iga -> provisioning [
        label="Access lifecycle"
    ]

    provisioning -> application [
        label="Provision / revoke"
    ]

    authentication -> application [
        label="Authentication result"
    ]

    application -> authorization [
        label="Evaluate access"
    ]

    authorization -> application [
        label="Allow / deny"
    ]

}
```

# Centralized Authorization Architecture

In a centralized authorization architecture, authorization decisions are handled by a central policy decision component rather than being implemented independently inside every application.

The applications still enforce the final decision, but they rely on the central authorization service to determine whether access should be allowed.

This can be useful when an organization wants consistent authorization policies across many applications and resources.

## Why use it?

As an organization grows, having authorization logic implemented independently across many applications can lead to inconsistent policies and duplicated logic.
Centralized authorization provides a common place to manage and evaluate authorization policies.
This can make it easier to apply consistent security requirements across multiple applications and resources while reducing duplicated authorization logic.

## Security Benefits

A well-designed centralized authorization architecture can provide several security benefits:
- Consistent authorization policies
- Centralized control over access rules
- Easier auditing of authorization decisions
- Reduced duplicated authorization logic
- Easier enforcement of least privilege
- Better visibility into access decisions
- Easier policy changes across multiple systems
- Reduced risk of applications implementing different versions of the same access policy

Centralized authorization can also make authorization policies easier to review and govern because policies are not completely scattered across individual applications.

## Security Implications

Centralized authorization also introduces additional security considerations.
The authorization infrastructure becomes a high-value security component because multiple applications may depend on it.

Important considerations include:
- Protect the authorization service itself
- Apply strong administrative access controls
- Use least privilege for policy administration
- Monitor policy changes
- Log authorization decisions
- Protect communication between applications and the authorization service
- Design for high availability
- Consider what happens if the authorization service becomes unavailable
- Carefully validate identity attributes and authorization context
- Prevent applications from bypassing centralized authorization decisions

Authorization policies should also be carefully designed. A central policy engine should not automatically become responsible for every application-specific business rule.

```{graphviz}
:caption: Centralized Authorization Architecture
:align: center
digraph architecture {

    rankdir=TB

    fontname="Helvetica"

    node [
        shape=box
        style="rounded,filled"
        fontname="Helvetica"
    ]

    edge [
        fontname="Helvetica"
    ]

    identity [
        label="Central Identity",
        fillcolor="#D5F5E3"
    ]

    policy [
        label="Central Authorization\nPolicy Engine",
        fillcolor="#F9E79F"
    ]

    app1 [
        label="Application A",
        fillcolor="#D7BDE2"
    ]

    app2 [
        label="Application B",
        fillcolor="#D7BDE2"
    ]

    resource [
        label="Protected Resources",
        fillcolor="#D5F5E3"
    ]

    identity -> policy [
        label="Identity / Attributes"
    ]

    app1 -> policy [
        label="Authorization request"
    ]

    app2 -> policy [
        label="Authorization request"
    ]

    policy -> app1 [
        label="Allow / Deny"
    ]

    policy -> app2 [
        label="Allow / Deny"
    ]

    app1 -> resource [
        label="Access"
    ]

    app2 -> resource [
        label="Access"
    ]

}
```

The main advantage is consistency. Authorization policies can be managed centrally, making it easier to apply common rules across many systems.

The main drawback is that applications become more dependent on the central authorization infrastructure. Availability, performance, and policy-engine security therefore become important considerations.

This architecture is most useful when authorization rules need to be consistent across many systems or when the organization wants centralized control over sensitive access policies.

# Decentralized / Federated IAM Architecture

In a decentralized or federated architecture, multiple identity domains or organizations maintain their own identity infrastructure while establishing trust between them.

Instead of forcing every identity into one central system, each security domain remains responsible for its own users.

Federation allows users to authenticate in their own domain while accessing resources in another trusted domain.

## Why use it?

Federation is useful when users need to access resources outside their own organization or security domain.
It avoids the need to create and maintain separate identities for the same user in every organization or environment they need to access.
This can simplify access management across organizational boundaries while allowing each organization to maintain control over its own users.
Federation is particularly useful when organizations need to collaborate without merging their identity infrastructures.

## Security Benefits

A well-designed federated IAM architecture can provide several security benefits:

- Reduced credential duplication: Users do not need separate credentials for every trusted organization or service.
- Centralized identity control: Each organization maintains control over its own identities and lifecycle.
- Reduced password exposure: Applications do not need to directly manage credentials belonging to external users.
- Improved lifecycle management: Access can depend on the user's identity remaining valid in their home organization.
- Strong authentication: The identity provider can enforce authentication requirements before issuing a trusted authentication result.
- Clear trust boundaries: Organizations can explicitly define which identity domains they trust.
- Better scalability: New services or organizations can be integrated without creating completely separate identities for every user.
- Improved user experience: Users can access trusted resources using their existing organizational identity.

## Security Implications

Federation introduces a significant trust relationship between otherwise independent security domains.
If one identity domain is trusted by another, the receiving organization is relying on that identity domain to authenticate identities correctly and provide trustworthy information.

Important security considerations include:
- Carefully define trust relationships.
- Only trust required identity providers.
- Minimize the attributes and permissions accepted from external domains.
- Validate authentication and authorization information.
- Protect federation configuration.
- Strongly protect administrators managing federation.
- Monitor federation activity.
- Monitor changes to trust relationships.
- Regularly review established trust relationships.
- Ensure compromised or deactivated identities cannot continue accessing trusted resources.
- Clearly define responsibilities between the participating organizations.
- Consider the impact of a compromise of a trusted identity domain.

A particularly important point is that federation does not automatically mean authorization is shared.

```{graphviz}
:caption: Decentralized / Federated IAM Architecture
:align: center
digraph architecture {

    rankdir=LR

    fontname="Helvetica"

    node [
        shape=box
        style="rounded,filled"
        fontname="Helvetica"
    ]

    edge [
        fontname="Helvetica"
    ]

    domainA [
        label="Identity Domain A\nUsers + Identity",
        fillcolor="#D5F5E3"
    ]

    domainB [
        label="Identity Domain B\nUsers + Identity",
        fillcolor="#D5F5E3"
    ]

    trust [
        label="Federation / Trust",
        fillcolor="#F9E79F"
    ]

    resourceA [
        label="Resources\nDomain A",
        fillcolor="#D7BDE2"
    ]

    resourceB [
        label="Resources\nDomain B",
        fillcolor="#D7BDE2"
    ]

    domainA -> trust [
        label="Trusted identity"
    ]

    domainB -> trust [
        label="Trusted identity"
    ]

    trust -> resourceA [
        label="Access"
    ]

    trust -> resourceB [
        label="Access"
    ]

}
```

The advantage is that each organization or security domain can maintain control over its own identities without having to merge identity databases.

This is particularly useful in environments involving:
- Multiple organizations
- Business partners
- Mergers and acquisitions
- External users
- Multi-tenant environments
- Large organizations with independent security domains

The main challenge is trust management.

Once two identity domains establish a federation relationship, each side needs to carefully define what identities, attributes, and authentication claims it is willing to trust.

# Comparison of IAM Architectures

## 1. Centralized Identity + Local Authorization
### Pros
- Simple separation of responsibilities
- Flexible
- Applications control their own access rules

### Cons
- Authorization can become inconsistent
- Each application must implement authorization correctly

### When to use
- Most organizations
- Many applications with different access requirements

### When not to use
- When the same authorization policies must be enforced everywhere

## Best for
- Most organizations

## 2. Centralized Identity + Centralized Authorization
### Pros
- Consistent policies
- Centralized control
- Easier to manage common access rules

### Cons
- Central dependency
- More complex
- Central authorization becomes a high-value target

### When to use
- When consistent authorization is important
- Highly sensitive resources

### When not to use
When applications have very different authorization requirements

### Best for
- Consistent policies

## 3. Federated / Decentralized IAM
### Pros
- Works across organizations
- Each organization keeps control of its identities
- Good for external users and partners

### Cons
- More complex
- Requires careful trust management

### When to use
- Multiple organizations
- Partners
- Multiple independent identity domains

### When not to use
- Small environments with one identity domain

### Best for
- Multiple organizations