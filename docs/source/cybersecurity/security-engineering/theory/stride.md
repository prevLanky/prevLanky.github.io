
    Spoofing 
        Sending an email as another user.
        Creating a phishing website mimicking a legitimate one to harvest user credentials.
    Tampering
        Updating the password of another user.
        Installing system-wide backdoors using an elevated access.
    Repudiation
        Denying unauthorised money-transfer transactions, wherein the system lacks auditing.
        Denying sending an offensive message to another person, wherein the person lacks proof of receiving one.
    Information Disclosure 
        Unauthenticated access to a misconfigured database that contains sensitive customer information.
        Accessing public cloud storage that handles sensitive documents.
    Denial of Service
        Flooding a web server with many requests, overwhelming its resources, and making it unavailable to legitimate users.
        Deploying a ransomware that encrypts all system data that prevents other systems from accessing the resources the compromised server needs.
    Elevation of Privilege
        Creating a regular user but being able to access the administrator console.
        Gaining local administrator privileges on a machine by abusing unpatched systems.


To implement the STRIDE framework in threat modelling, it is essential to integrate the six threat categories into a systematic process that effectively identifies, assesses, and mitigates security risks. Here is a high-level approach to incorporating STRIDE in the threat modelling methodologies we discussed.

    System Decomposition

    Break down all accounted systems into components, such as applications, networks, and data flows. Understand the architecture, trust boundaries, and potential attack surfaces.
    Apply STRIDE Categories

    For each component, analyse its exposure to the six STRIDE threat categories. Identify potential threats and vulnerabilities related to each category.
    Threat Assessment

    Evaluate the impact and likelihood of each identified threat. Consider the potential consequences and the ease of exploitation and prioritise threats based on their overall risk level.
    Develop Countermeasures 

    Design and implement security controls to address the identified threats tailored to each STRIDE category. For example, to enhance email security and mitigate spoofing threats, implement DMARC, DKIM, and SPF, which are email authentication and validation mechanisms that help prevent email spoofing, phishing, and spamming.
    Validation and Verification

    Test the effectiveness of the implemented countermeasures to ensure they effectively mitigate the identified threats. If possible, conduct penetration testing, code reviews, or security audits.
    Continuous Improvement

    Regularly review and update the threat model as the system evolves and new threats emerge. Monitor the effective countermeasures and update them as needed.

