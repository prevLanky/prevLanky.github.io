# ISO/IEC 19249:2017  
Information technology – Security techniques – Catalogue of architectural and design principles for secure products, systems and applications

ISO/IEC 19249 defines a set of architectural and design principles that help build secure systems from the ground up.


## ISO/IEC 19249 architectural principles

### Domain Separation
Domain separation means grouping related components into isolated domains, each with its own security rules. This limits how much damage can occur if one domain is compromised.

Example:  
In operating systems, the kernel runs with higher privileges than user applications. If a user application is compromised, it should not be able to directly affect the kernel.

### Layering
Layering structures a system into distinct levels, where each layer has a specific responsibility. Security controls can then be applied at multiple layers.

Example:  
The OSI networking model separates communication into layers. Firewalls, encryption, and authentication can be applied at different layers.  
This principle closely supports Defence-in-Depth.

### Encapsulation
Encapsulation hides internal implementation details and only exposes controlled interfaces. This prevents direct access to sensitive data or logic.

Example:  
Applications interact with a database through an API instead of direct database access, reducing the risk of misuse or injection attacks.

### Redundancy
Redundancy improves availability and integrity by removing single points of failure.

Example:  
Using multiple power supplies in a server or RAID storage so systems continue to function even if one component fails.

### Virtualization
Virtualization allows multiple isolated systems to run on the same physical hardware. It strengthens security boundaries and limits the spread of attacks.

Example:  
Running applications in separate virtual machines or containers so a compromised application cannot easily access others.


## ISO/IEC 19249 design principles

### Least Privilege
Least privilege means giving users, systems, or processes only the permissions they need to perform their tasks.

Example:  
A user who only needs to read reports should not have permission to modify or delete them.

### Attack Surface Minimisation
Reducing the attack surface means removing unnecessary features, services, and entry points that could be exploited.

Example:  
Disabling unused network services on a server to reduce potential vulnerabilities.

### Centralized Parameter Validation
All input validation should be handled in a consistent and centralized way to reduce errors and security gaps.

Example:  
Using a shared validation library for all user input to prevent SQL injection, buffer overflows, or malformed requests.

### Centralized General Security Services
Security services such as authentication, authorization, and logging should be centralized to ensure consistency and easier management.

Example:  
Using a centralized identity provider instead of each application managing its own user accounts.

### Preparing for Error and Exception Handling
Systems should be designed to fail safely and handle errors without exposing sensitive information.

Example:  
If a firewall crashes, it should block traffic by default. Error messages should not reveal internal system details.