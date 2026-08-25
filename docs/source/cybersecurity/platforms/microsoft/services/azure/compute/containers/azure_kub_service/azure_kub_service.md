# Azure Kubernetes Service (AKS) Confidential Containers

What is Azure Kubernetes Service (AKS) Confidential Containers? 
When to use it? 
Why use it?
How to configure it according to security best practices?
How to design the component?
How to design the supporting infrastructure?

```{graphviz}
:caption: Simple AKS Confidential Container High-Level Architecture
:align: center

digraph architecture {
    rankdir=TB
    fontname="Helvetica"

    node [shape=box style="rounded,filled" fontname="Helvetica"]
    edge [fontname="Helvetica"]

    /* =======================
       INTERNET
       ======================= */

    internet [label="Internet", fillcolor="#FFFFFF"]

    frontend [label="Azure Front Door\n/ WAF", fillcolor="#FFCCCC"]

    /* =======================
       AZURE
       ======================= */

    subgraph cluster_azure {
        label="Azure"
        style="filled"
        color="#E6F2FF"

        subgraph cluster_aks {
            label="Azure Kubernetes Service (AKS)"
            style="filled"
            color="#CCE5FF"

            app [label="Application", fillcolor="#D7BDE2"]

            confidential [label="Confidential Container\nProtected workload", fillcolor="#D7BDE2"]
        }

        keyvault [label="Azure Key Vault\nSecrets", fillcolor="#D5F5E3"]

        database [label="Database\nApplication data", fillcolor="#D5F5E3"]
    }

    /* =======================
       TRUST
       ======================= */

    attestation [label="Attestation\nVerify workload", fillcolor="#F9E79F"]

    /* =======================
       FLOWS
       ======================= */

    internet -> frontend [label="1. HTTPS"]
    frontend -> app [label="2. Request"]

    app -> confidential [label="3. Runs inside"]

    confidential -> database [label="4. Read / write data"]

    confidential -> attestation [label="5. Prove it's trusted"]

    attestation -> keyvault [label="6. Allow secret access"]

    keyvault -> confidential [label="7. Secret"]
}
```

---

```{graphviz}
:caption: What Makes a Container Confidential?
:align: center

digraph architecture {
    rankdir=TB
    fontname="Helvetica"

    node [shape=box style="rounded,filled" fontname="Helvetica"]
    edge [fontname="Helvetica"]

    application [label="Application\nSensitive data", fillcolor="#D7BDE2"]

    container [label="Confidential Container", fillcolor="#D7BDE2"]

    tee [label="Protected Environment\nHardware-backed protection", fillcolor="#F9E79F"]

    host [label="Underlying Infrastructure", fillcolor="#FFFFFF"]

    application -> container [label="Runs inside"]
    container -> tee [label="Protected by"]
    tee -> host [label="Isolated from"]
}
```

---
```{graphviz}
:caption: Attestation and Secret Access
:align: center

digraph architecture {
    rankdir=LR
    fontname="Helvetica"

    node [shape=box style="rounded,filled" fontname="Helvetica"]
    edge [fontname="Helvetica"]

    workload [label="Confidential\nContainer", fillcolor="#D7BDE2"]

    attestation [label="Attestation\nIs this a trusted\nworkload?", fillcolor="#F9E79F"]

    keyvault [label="Azure Key Vault\nSecret / Key", fillcolor="#D5F5E3"]

    workload -> attestation [label="1. Prove workload"]
    attestation -> keyvault [label="2. If trusted"]
    keyvault -> workload [label="3. Release secret"]
}
```