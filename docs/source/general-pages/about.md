# About

```{graphviz}
:caption: Secure File Processing & Flashcard Architecture
:align: center
:engine: dot

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
        web [label="Webserver (FastAPI)\n• Upload API\n• Status API\n• Flashcard API\n• JWT Issuer", fillcolor="#FFCCCC"]
    }

    subgraph cluster_control {
        label="Control Node Pool (Trusted Internal)"
        style="filled"
        color="#E6F2FF"

        jobmaster [label="Job Master\n• Valkey consumer\n• Orchestrates scans\n• Updates DB\n• Moves files", fillcolor="#CCE5FF"]
        valkey [label="Valkey\n(Stream + Consumer Groups)", fillcolor="#CCE5FF"]
        postgres [label="PostgreSQL\n• Files\n• Jobs\n• Flashcards\n• user_id ownership", fillcolor="#CCE5FF"]
        minio [label="MinIO Object Storage\nBuckets:\n• incoming/\n• clean/\n• quarantine/", fillcolor="#CCE5FF"]
    }

    subgraph cluster_scanner {
        label="Scanner Node Pool (Sandbox / Untrusted)"
        style="filled"
        color="#FDEBD0"

        scanner [label="ClamAV Workers\n• Stateless\n• Stream-based scan\n• No DB/Storage access", fillcolor="#FAD7A0"]
    }

    subgraph cluster_ai {
        label="AI Worker Node Pool (Trusted Compute)"
        style="filled"
        color="#E8F8F5"

        aiworker [label="AI Processing Workers\n• Parse PDF/DOCX\n• Extract text\n• Generate flashcards\n• Apply user preferences", fillcolor="#D1F2EB"]
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

    /* =======================
       AI PROCESSING
       ======================= */

    postgres -> aiworker [label="14. Poll / Subscribe\nfor CLEAN files"]
    aiworker -> minio [label="15. Read clean file"]
    aiworker -> postgres [label="16. Store flashcards\n(JSON, user_id)"]

    /* =======================
       USER INTERACTION
       ======================= */

    browser -> web [label="17. GET /status\n(Authorization: JWT)"]
    web -> postgres [label="18. Query file/job status\n(user_id scoped)"]
    web -> browser [label="19. Return status"]

    browser -> web [label="20. GET /flashcards\n(JWT)"]
    web -> postgres [label="21. Fetch flashcards\n(user_id scoped)"]
    web -> browser [label="22. Flashcards\nPractice UI"]
}
```
