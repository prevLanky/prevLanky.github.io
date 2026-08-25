# Azure Kubernetes Service (AKS) Confidential Containers

What is Azure Kubernetes Service (AKS) Confidential Containers? 
When to use it? 
Why use it?
How to configure it according to security best practices?
How to design the component?
How to design the supporting infrastructure?

```{graphviz}
:caption: AKS Confidential Containers – Secure Azure Architecture
:align: center

digraph architecture {
    rankdir=TB
    fontname="Helvetica"

    node [shape=box style="rounded,filled" fontname="Helvetica"]
    edge [fontname="Helvetica"]

    /* =======================
       INTERNET / EDGE
       ======================= */

    internet [label="INTERNET", fillcolor="#FFFFFF"]

    frontdoor [label="Azure Front Door / WAF\n• TLS\n• WAF\n• DDoS protection", fillcolor="#FFCCCC"]

    appgw [label="Application Gateway / Ingress\n• Routing\n• TLS\n• Application ingress", fillcolor="#FFCCCC"]

    /* =======================
       PRIVATE VNET
       ======================= */

    subgraph cluster_vnet {
        label="Private VNet"
        style="filled"
        color="#E6F2FF"

        /* =======================
           AKS
           ======================= */

        subgraph cluster_aks {
            label="Azure Kubernetes Service (AKS)"
            style="filled"
            color="#CCE5FF"

            api [label="Private AKS API Server\n• Private endpoint\n• Entra ID\n• RBAC", fillcolor="#FFFFFF"]

            subgraph cluster_confidential {
                label="Confidential Workload"
                style="filled"
                color="#E8DAEF"

                application [label="Application\n• Container\n• Non-root\n• Minimal privileges", fillcolor="#D7BDE2"]

                kata [label="Kata Confidential Containers\n• Confidential VM isolation\n• Workload isolation", fillcolor="#D7BDE2"]

                tee [label="Hardware TEE\nAMD SEV-SNP\n• Encrypted memory\n• Hardware-backed isolation", fillcolor="#BB8FCE"]
            }

            controls [label="AKS Security Controls\n• NetworkPolicy\n• Pod Security\n• Workload Identity\n• Azure Policy", fillcolor="#CCE5FF"]
        }

        /* =======================
           DATA SERVICES
           ======================= */

        keyvault [label="Azure Key Vault\n• Secrets\n• Keys\n• Certificates\n• Private Endpoint", fillcolor="#D5F5E3"]

        database [label="Azure Database\n• PostgreSQL / SQL\n• Private Endpoint\n• Encryption at rest", fillcolor="#D5F5E3"]
    }

    /* =======================
       ATTESTATION
       ======================= */

    subgraph cluster_attestation {
        label="Confidential Computing Trust"
        style="filled"
        color="#FCF3CF"

        attestation [label="Azure Attestation\n• Verify TEE evidence\n• Validate workload state\n• Attestation token", fillcolor="#F9E79F"]
    }

    /* =======================
       INGRESS FLOW
       ======================= */

    internet -> frontdoor [label="HTTPS"]
    frontdoor -> appgw [label="HTTPS"]
    appgw -> application [label="Application traffic"]

    /* =======================
       AKS INTERNAL FLOW
       ======================= */

    application -> kata [label="Execute"]
    kata -> tee [label="Protected execution"]

    /* =======================
       AKS CONTROL PLANE
       ======================= */

    api -> application [label="Kubernetes control"]

    /* =======================
       SECURITY CONTROLS
       ======================= */

    controls -> application [label="Enforce security policy"]

    /* =======================
       DATA ACCESS
       ======================= */

    application -> keyvault [label="Private access\nvia Private Endpoint"]
    application -> database [label="Private access\nvia Private Endpoint"]

    /* =======================
       ATTESTATION / SECRET RELEASE
       ======================= */

    tee -> attestation [label="TEE evidence"]
    attestation -> keyvault [label="Verified workload\n→ release secret"]

}
```