
The core overview of my enterprise architcture that i will call "Platform Cell".
This is a combination of Platform engineering + cell architecture + federation.


The goal is to take the good parts of different types of architectures to be able to fulfill the following core principles:
- Be able to consume services from a central point while allowing space to exercise autonomy;
- Clear security boundry;
- Isolation with controlled freedom;
- Minimize "bubbles" (reinventing the wheel);
- Use centralized and standardized services whenever possible;



Governance
Central platform
Area platforms, + internal dev platform + another
Internet access?
Mirroring platform? How is the best practice handled? Internal github for all appproved 3PPs? or allow each area to retreive 3PP as they like?

centralized operation, decentrralized consumption.


The architecture stays conceptually the same as the company grows. You add Areas, capacity and platforrm capabilitites rather than redesigning the whole environment.
Core capabilities used at every step are:
- IAM
- Storage
- Network
- Compute
- Security
- Monitoring
- Backup
- Platform management and automation
- Governance

                    CENTRAL PLATFORM
                          │
       ┌──────────────────┼──────────────────┐
       │                  │                  │
   IDENTITIES         CONNECTIVITY       COMPUTE
       │                  │                  │
       ├────────────── DATA & STORAGE  ──────┤
       │                  │                  │
   SECURITY          OBSERVABILITY      MANAGEMENT
       │                  │                  │
       └──────────────────┬──────────────────┘
                          │
                     AREA PLATFORMS

