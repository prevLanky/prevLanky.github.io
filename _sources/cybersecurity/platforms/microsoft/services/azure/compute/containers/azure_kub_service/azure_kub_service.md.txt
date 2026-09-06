# Azure Kubernetes Service (AKS) Confidential Containers

# What is Azure Kubernetes Service (AKS) Confidential Containers?
Azure Kubernetes Service (AKS) Confidential Containers allows Kubernetes workloads to run inside a hardware-backed Trusted Execution Environment (TEE).

The purpose is to protect sensitive code and data while they are being processed.

With this type of container an additional layer of isolation is added.

Confidential Containers use Kata Confidential Containers together with confidential-computing hardware such as AMD SEV-SNP.

The main goal is to protect workloads and its memory from threats at the underlying infrastructure layer, while allowing the application to run normally. For example, lets say you want to decrypt some important customer data, without unneccesarily exposing it. If you id this operation in a normal container, the decrpted data would be exosed in RAM, potentially allowing privliged users that has access to the underlying hardware to read the data. But with a confidential container, the operations done inside that container is protected and does not expose it to the underlying infrastructure. Essentially making the operations isolated.

Confidential Containers can also use attestation, which allows the workload or another trusted service to verify that it is running in the expected confidential environment before sensitive secrets are released.

# Why use it?
Traditionally security protects 3 states of data:
- Data at Rest
- Data in Transit
- Data in Use

Confidential Containers addresses the 3rd area.
Data in Use is difficult to protect since the plaintext data must exist somewhere while it is processed. So adding this type of container adds an additional layer of security.

# When to use it? 
You should consider Confidential Containers when the application processes highly sensitive data and protecting data only at rest and in transit is not sufficient.

Important to note that it does not replace and of the other security measures. Because it does not protect against for example:
- SQL injections
- RCE
- Vulnerable application code
- Insecure APIs
- Excessive Kubernetes permissions
- Poor network segementation



# Drawbacks

# Real life use cases

# How to configure it according to security best practices?
# How to design the component?
# How to design the supporting infrastructure?

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

            confidential [
                label="Confidential Container\nProtected workload",
                fillcolor="#D7BDE2"
            ]
        }

        keyvault [
            label="Azure Key Vault\nSecrets",
            fillcolor="#D5F5E3"
        ]

        database [
            label="Database\nApplication data",
            fillcolor="#D5F5E3"
        ]
    }

    /* =======================
       TRUST
       ======================= */

    attestation [
        label="Attestation\nVerify workload",
        fillcolor="#F9E79F"
    ]

    /* =======================
       FLOWS
       ======================= */

    internet -> frontend [
        label="1. HTTPS"
    ]

    frontend -> app [
        label="2. Request"
    ]

    app -> confidential [
        label="3. Runs inside"
    ]

    confidential -> database [
        label="4. Read / write data"
    ]

    confidential -> attestation [
        label="5. Prove it's trusted"
    ]

    attestation -> keyvault [
        label="6. Allow secret access"
    ]

    keyvault -> confidential [
        label="7. Secret"
    ]
}
```

---

```{graphviz}
:caption: What Makes a Container Confidential?
:align: center

digraph architecture {

    rankdir=TB
    fontname="Helvetica"

    node [
        shape=box
        style="rounded,filled"
        fontname="Helvetica"
    ]

    edge [fontname="Helvetica"]

    application [
        label="Application\nSensitive data",
        fillcolor="#D7BDE2"
    ]

    container [
        label="Confidential Container",
        fillcolor="#D7BDE2"
    ]

    tee [
        label="TEE\nHardware-backed protection",
        fillcolor="#F9E79F"
    ]

    host [
        label="Underlying Infrastructure",
        fillcolor="#FFFFFF"
    ]

    application -> container [
        label="Runs inside"
    ]

    container -> tee [
        label="Protected by"
    ]

    tee -> host [
        label="Hardware isolation"
    ]
}
```

---
```{graphviz}
:caption: Attestation and Secret Access
:align: center

digraph architecture {

    rankdir=LR
    fontname="Helvetica"

    node [
        shape=box
        style="rounded,filled"
        fontname="Helvetica"
    ]

    edge [fontname="Helvetica"]

    workload [
        label="Confidential\nContainer",
        fillcolor="#D7BDE2"
    ]

    attestation [
        label="Attestation\nIs this a trusted\nworkload?",
        fillcolor="#F9E79F"
    ]

    keyvault [
        label="Azure Key Vault\nSecret / Key",
        fillcolor="#D5F5E3"
    ]

    workload -> attestation [
        label="1. Prove workload"
    ]

    attestation -> keyvault [
        label="2. If trusted"
    ]

    keyvault -> workload [
        label="3. Release secret"
    ]
}
```