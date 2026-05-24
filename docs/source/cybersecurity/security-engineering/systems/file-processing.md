# File Processing system 

This is a design/architecture for how to securely handle files that are uploaded to a webserver from internet.

# Requirements 
- The system needs to be plug-n-play for all kinds of webapps;
- Each file needs to be sanitized;
- Each file need be considered untrustworhy and never be executed;
- Each file need be processed in a sandboxed or seprate ephemeral environment;
- Access to uploaded files need to be controlled and limited;
- The system need to be configurable to fit different deploment models;
- The system need to be DoS resistant;

# Security principles
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


# Use Cases

# Components
## File storage
### Requirements

## Message queue
### Requirements

## File processors (Slave)
### Requirements

## Job orchestrator
### Requirements

## Job storage
### Requirements

