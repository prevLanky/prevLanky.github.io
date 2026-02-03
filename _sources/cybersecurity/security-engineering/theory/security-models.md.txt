# Security Models

## Bell-LaPadula Model
This model focuses on confidentiality and access control based on security levels (e.g., classified vs unclassified).

### Pros & Cons
**Pros**
- Strong focus on confidentiality  
- Clear access rules  

**Cons**
- Ignores integrity  
- Not practical for many modern systems  

## The Biba Integrity Model
The Biba model focuses on protecting data integrity by preventing unauthorized modification.

### Pros & Cons
**Pros**
- Strong integrity guarantees  
- Useful for systems where data accuracy is critical  

**Cons**
- Can be too restrictive  
- Does not address confidentiality  

## The Clark-Wilson Model
This model enforces integrity using controlled processes, separation of duties, and well-defined transactions.

### Pros & Cons
**Pros**
- Practical for commercial systems  
- Supports auditing and accountability  

**Cons**
- More complex to implement  
- Requires well-defined processes  