# Azure Kubernetes Service (AKS) Confidential Containers

What is Azure Kubernetes Service (AKS) Confidential Containers? 
When to use it? 
Why use it?
How to configure it according to security best practices?
How to design the component?
How to design the supporting infrastructure?

```{graphviz}
:caption: AKS Confidential Containers – Secure Workload Architecture
:align: center

digraph architecture {
    rankdir=LR
    fontname="Helvetica"

    node [shape=box style="rounded,filled" fontname="Helvetica"]
    edge [fontname="Helvetica"]

    /* =======================
       TRUST ZONES
       ======================= */

    subgraph cluster_edge {
        label="Internet / Edge"
        style="filled"
        color="#FFE6E6"

        user [label="User / Client\n• HTTPS\n• JWT / Entra ID", fillcolor="#FFFFFF"]
        waf [label="Azure Front Door / WAF\n• TLS termination\n• WAF rules\n• DDoS protection", fillcolor="#FFCCCC"]
    }

    subgraph cluster_network {
        label="Azure Network (Private)"
        style="filled"
        color="#E6F2FF"

        firewall [label="Azure Firewall\n• Egress filtering\n• FQDN rules\n• Threat intelligence", fillcolor="#CCE5FF"]

        private_dns [label="Private DNS\n• AKS\n• Key Vault\n• ACR\n• Database", fillcolor="#CCE5FF"]
    }

    subgraph cluster_aks {
        label="AKS Private Cluster"
        style="filled"
        color="#E6F2FF"

        ingress [label="Ingress / Application Gateway\n• Internal ingress\n• TLS\n• Routing", fillcolor="#CCE5FF"]

        subgraph cluster_confidential {
            label="Confidential Node Pool / Workload"
            style="filled"
            color="#E8DAEF"

            pod [label="Confidential Pod\n• Application\n• Non-root\n• Read-only filesystem\n• Minimal capabilities", fillcolor="#D7BDE2"]

            kata [label="Kata Confidential Containers\n• Isolation boundary\n• Confidential workload runtime", fillcolor="#D7BDE2"]

            tee [label="Hardware TEE\nAMD SEV-SNP\n• Encrypted memory\n• Hardware-backed isolation", fillcolor="#BB8FCE"]
        }

        identity [label="AKS Workload Identity\n• Entra ID\n• OIDC\n• Managed Identity", fillcolor="#CCE5FF"]

        policy [label="Azure Policy / Kubernetes Policy\n• Pod security\n• Allowed images\n• Privilege restrictions", fillcolor="#CCE5FF"]

        networkpolicy [label="NetworkPolicy\n• Pod-to-pod restrictions\n• Least privilege", fillcolor="#CCE5FF"]
    }

    subgraph cluster_data {
        label="Protected Azure Services"
        style="filled"
        color="#E8F8F5"

        acr [label="Azure Container Registry\n• Trusted images\n• Image scanning\n• Signed images", fillcolor="#D5F5E3"]

        keyvault [label="Azure Key Vault\n• Secrets\n• Certificates\n• Keys\n• Private Endpoint", fillcolor="#D5F5E3"]

        database [label="Azure Database\n• PostgreSQL / SQL\n• Private Endpoint\n• Encryption at rest", fillcolor="#D5F5E3"]
    }

    subgraph cluster_attestation {
        label="Confidential Computing Trust"
        style="filled"
        color="#FCF3CF"

        attestation [label="Azure Attestation\n• Validate TEE evidence\n• Verify workload state\n• Issue attestation token", fillcolor="#F9E79F"]
    }

    subgraph cluster_security {
        label="Security Operations"
        style="filled"
        color="#F5EEF8"

        defender [label="Microsoft Defender for Cloud\n• Defender for Containers\n• Vulnerability detection\n• Runtime protection", fillcolor="#E8DAEF"]

        monitor [label="Azure Monitor / Log Analytics\n• AKS logs\n• Audit logs\n• Metrics", fillcolor="#E8DAEF"]

        sentinel [label="Microsoft Sentinel\n• SIEM\n• Detection\n• Correlation\n• Incident response", fillcolor="#E8DAEF"]

        entra [label="Microsoft Entra ID\n• MFA\n• Conditional Access\n• PIM\n• RBAC", fillcolor="#E8DAEF"]
    }

    /* =======================
       USER TRAFFIC
       ======================= */

    user -> waf [label="1. HTTPS"]
    waf -> ingress [label="2. HTTPS"]

    /* =======================
       APPLICATION TRAFFIC
       ======================= */

    ingress -> pod [label="3. Application request"]

    /* =======================
       CONFIDENTIAL EXECUTION
       ======================= */

    pod -> kata [label="4. Execute workload"]
    kata -> tee [label="5. Protected execution\ninside TEE"]

    /* =======================
       IDENTITY
       ======================= */

    pod -> identity [label="6. Workload identity"]
    identity -> entra [label="7. Authenticate / authorize"]

    /* =======================
       ATTESTATION
       ======================= */

    tee -> attestation [label="8. TEE evidence"]
    attestation -> keyvault [label="9. Release secret\nonly after verification"]

    /* =======================
       DATA ACCESS
       ======================= */

    pod -> database [label="10. Private database access"]
    pod -> keyvault [label="11. Retrieve approved secrets"]

    /* =======================
       IMAGE SUPPLY CHAIN
       ======================= */

    acr -> pod [label="12. Pull approved image"]

    /* =======================
       POLICY / NETWORK SECURITY
       ======================= */

    policy -> pod [label="13. Enforce workload security"]
    networkpolicy -> pod [label="14. Restrict pod traffic"]

    /* =======================
       EGRESS
       ======================= */

    pod -> firewall [label="15. Required egress"]
    firewall -> waf [label="16. Approved external destinations"]

    /* =======================
       SECURITY MONITORING
       ======================= */

    defender -> pod [label="17. Runtime / container security"]
    monitor -> pod [label="18. Logs / metrics"]
    monitor -> sentinel [label="19. Security telemetry"]
    defender -> sentinel [label="20. Security alerts"]

    /* =======================
       ADMINISTRATION
       ======================= */

    entra -> policy [label="21. Authorized administration"]
}
```