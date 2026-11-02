# Atlas / ServiceHub SharePoint review

**Review date:** 2026-11-02

**Purpose:** working notes for the VFCZ solution architecture review. These notes distinguish observed document content from architectural interpretation and user-provided design constraints.

## Scope and verified SharePoint structure

The three rightmost browser tabs were checked in order from right to left. They were the Marketplace folder, the Use Case Specification, and the BRD. A prior note identifying RACI as one of these three tabs was incorrect; RACI was not among the three rightmost tabs at the time of this check.

### BRD and Use Cases

SharePoint path observed for the BRD's parent folder:

`2. Portfolio > Atlas Expansion - Czech > Interlock-Pack > CZ local folder > Business Requirements Document`

Visible contents of `Business Requirements Document`:

- `Use Cases/` (one child document; no further subfolders observed)
- `PR25_0837_ServiceHub_Atlas_BRD.docx`
- `PR25_0837_ServiceHub_Atlas_Traceability_Decomposition.xlsx`

The `Use Cases/` folder contains `PR25_0837_ServiceHub_Atlas_Use_Case_Specification.docx` and no visible child folders.

### Marketplace

SharePoint path observed:

`3. Design > SecureByDesign > 1. Baseline Security Requirements > 4. MarketPlace`

The folder contains one visible workbook, `BSR_Appdirect_2023_Update...xlsx`, and no visible child folders.

## Source facts

### BRD

- 25 pages; cover version 0.7.
- Revision table includes v0.1 (13 Oct 2026) and v0.2 (23 Oct 2026).
- It covers the CZ-local integration of Group ServiceHub and Atlas as a customer portal.
- Scope details and project dependencies are described in the BRD. The user identified the Atlas CZ Launch Architecture Board as the binding source for overall project scope.
- The BRD does not specify the technical DXL CZ token negotiation and downstream header propagation.

### Use Case Specification

- 51 pages and 12 use cases; document v0.1, updated 14 Oct 2026.
- UC005 describes a user accessing ServiceHub with customer relationship, role, CRM/customer context obtained from DXL.
- It describes authentication and customer/role context at use-case level. It does not provide the technical DXL CZ token exchange, token format, API contract, or downstream header handling.

### Traceability Decomposition workbook

- One worksheet (`Traceability`), 26 visible data rows.
- Columns connect customer journey and description to UC ID/name/description, process ID/name/description, value stream, capability, and sub-capability.
- Customer journeys represented: Buy Atlas, Upgrade M365 to Atlas, Access and View Atlas, Get Support for Atlas, and Downgrade Atlas to M365.
- Value streams include Sell, Build, and Run.
- Capabilities include Product & Pricing Management, Service Onboarding, Exception Handling, Channel & Entry Management, Identity & Access Management, Service Visibility, Support Management, and Service Offboarding.
- Sub-capabilities include Marketplace Company Identifier/Data Readiness, Atlas Subscription Readiness, Managed Service Onboarding, Data Consistency, Entry Points and Navigation, Authorization Input Readiness, Customer Context Input Readiness, Atlas Service Data Availability, Channel Handling, Routing & Forwarding, Assisted Support, Escalation Handling, Support Request Visibility/Update, and Termination Handling.

### Marketplace BSR / AppDirect workbook

- 16 worksheets: Introduction, Initial Questionnaire, and security areas 1–14.
- The baseline's Introduction states version 2.6, released 1 April 2019. The workbook title and project-team comments indicate a 2023 AppDirect update.
- Questionnaire identifies AppDirect SaaS Marketplace; personal/C3/C4 data, external APIs, cloud hosting/external connectivity, and third-party involvement are marked Yes. Vodafone SSO and web-app questions are marked No, despite the SaaS Marketplace description. These are AppDirect assessment answers, not Atlas facts.
- The workbook marks retention of personal data and local privacy/regulatory measures as No. Cryptographic key management is Partial; comments describe AppDirect as sole key owner/manager and logical tenant separation. API control responses are mostly blank in the current response column; one visible response states TLS 1.2+ with termination in a trusted network zone.
- Treat this as a historical, supplier-specific security assessment and checklist of control topics. Do not use its AppDirect answers as evidence for Atlas or ServiceHub architecture.

## Architecture interpretation

### Business layer (yellow in the user's model)

The Traceability workbook is the strongest direct input for the business layer. It provides a trace from customer journeys through use cases and business processes to value streams, capabilities, and sub-capabilities. It can seed capability and process views and help trace business requirements to UC IDs.

### Application layer (blue in the user's model)

BRD and Use Cases provide application context and interactions for ServiceHub, Atlas, and DXL. UC005 and the Traceability sub-capabilities around authorization input, customer context input, and Atlas service data availability are useful anchors for logical application services and information flows. The sources do not define complete component boundaries, API contracts, data schemas, or sequence-level token handling; those need EA and technical-interface evidence.

### Physical applications (green in the user's model)

The Marketplace workbook assesses AppDirect as a third-party SaaS product. It is not an inventory or deployment description of Atlas/ServiceHub and should not be used to assert their physical components or hosting controls.

## User-provided design constraint (not established by these documents)

The user stated that SSO is part of Atlas MVP: the user authenticates at ServiceHub; ServiceHub negotiates a token with DXL CZ using a CZ-specific call; it then places the returned token in headers for subsequent DXL calls to VFCZ. This is a required design constraint from the user, but the reviewed BRD and Use Case Specification do not document its technical sequence or contract.

## Follow-up items for the architecture review

1. Map Traceability customer journeys, use cases, processes, capabilities, and sub-capabilities to the EA model, preserving source IDs.
2. Validate blue-layer application services, information objects, interfaces, and ownership for ServiceHub, Atlas, DXL CZ, CRM/Siebel, and SNOW against the XMI/UML exports and current technical documentation.
3. Add the user-stated SSO/token flow as a sequence/interface view only after its DXL CZ contract, token claims, audience, expiry, error handling, and forwarding rules are evidenced.
4. Reconcile the AppDirect security checklist only as generic control prompts; obtain current Atlas/ServiceHub security responses separately.
5. Use the Traceability workbook as a mapping source, not as proof that each capability or sub-capability has an approved requirement or implementation owner.

## Read-only and provenance note

No cell values were entered during this review. Spreadsheet navigation consisted of switching worksheets and scrolling. During one return to the Marketplace SharePoint listing, its workbook showed a recent `Modified: About a minute ago` timestamp attributed to the signed-in account. The initiator and cause were not established; do not infer from the screenshot alone that content changed or that the timestamp was caused by navigation.
