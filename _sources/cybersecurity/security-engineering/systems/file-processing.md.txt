# File Processing system 

This is a design/architecture for how to securely handle files that are uploaded to a webserver from internet.

```{graphviz}
:caption: Secure File Upload & Scanning Architecture
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
        label="Edge Node Pool (Internet-facing)"
        style="filled"
        color="#FFE6E6"

        browser [label="User Browser\n(Anonymous / JWT-based)", fillcolor="#FFFFFF"]
        web [label="Webserver (FastAPI)\n• Upload API\n• Status API\n• JWT Issuer", fillcolor="#FFCCCC"]
    }

    subgraph cluster_control {
        label="Control Node Pool (Trusted Internal)"
        style="filled"
        color="#E6F2FF"

        jobmaster [label="Job Master\n• Valkey consumer\n• Orchestrates scans\n• Updates DB\n• Moves files", fillcolor="#CCE5FF"]
        valkey [label="Valkey\n(Stream + Consumer Groups)", fillcolor="#CCE5FF"]
        postgres [label="PostgreSQL\n• Files\n• Jobs\n• user_id ownership", fillcolor="#CCE5FF"]
        minio [label="MinIO Object Storage\nBuckets:\n• incoming/\n• clean/\n• quarantine/", fillcolor="#CCE5FF"]
    }

    subgraph cluster_scanner {
        label="Scanner Node Pool (Sandbox / Untrusted)"
        style="filled"
        color="#FDEBD0"

        scanner [label="ClamAV Workers\n• Stateless\n• Stream-based scan\n• No DB/Storage access", fillcolor="#FAD7A0"]
    }

    /* =======================
       USER FLOW
       ======================= */

    browser -> web [label="1. Upload file\n(POST /upload)"]
    web -> browser [label="2. Return file_id + JWT"]

    /* =======================
       FILE INGESTION
       ======================= */

    web -> minio [label="3. Stream upload → incoming/"]
    web -> postgres [label="4. Insert file row\nstatus=QUEUED\nuser_id"]
    web -> valkey [label="5. XADD scan job\n(file_id, user_id)"]

    /* =======================
       JOB ORCHESTRATION
       ======================= */

    valkey -> jobmaster [label="6. XREADGROUP\n(one master claims job)"]
    jobmaster -> postgres [label="7. UPDATE status=SCANNING\n(atomic claim)"]
    jobmaster -> minio [label="8. GET object\nfrom incoming/"]
    jobmaster -> scanner [label="9. Stream bytes\n(scan request)"]

    /* =======================
       SCANNING RESULTS
       ======================= */

    scanner -> jobmaster [label="10. Scan verdict\n(CLEAN / INFECTED)"]
    jobmaster -> postgres [label="11. UPDATE status\nCLEAN / INFECTED"]
    jobmaster -> minio [label="12a. Move to clean/\n(if CLEAN)"]
    jobmaster -> minio [label="12b. Move to quarantine/\n(if INFECTED)"]
    jobmaster -> valkey [label="13. XACK job\n(remove from stream)"]
}
```


## Requirements 
- The system needs to be plug-n-play for all kinds of webapps;
- Each file needs to be sanitized;
- Each file need be considered untrustworhy and never be executed;
- Each file need be processed in a sandboxed or seprate ephemeral environment;
- Access to uploaded files need to be controlled and limited;
- The system need to be configurable to fit different deploment models;
- The system need to be DoS resistant;

## Security principles
- principle of Least privlige
- Separation of concerns
- Trust boundries
- Blast-radius containment (isolation)
- zero-trust (later stage, but prepared for)
- Minimal retention, store artefact/metadata instead of complete file
- Non-repudiation (for when user login is used)
- Immutable
- Defense in depth
- Store artefact/metadata


## Use Cases

## Components
### File storage
#### Requirements

### Message queue
#### Requirements

### File processors (Slave)
#### Requirements

### Job orchestrator
#### Requirements

### Job storage
#### Requirements

