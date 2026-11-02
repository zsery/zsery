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

## Additional local architecture inputs reviewed

The following are files already present in the user's `zsery/zsery` repository. They are separate from the three SharePoint tabs above and are not treated as newly approved requirements.

### `Book1.xlsx`

Read-only inventory of the workbook:

- 10 worksheets: Cover, `_Enums`, Functionalities, Interfaces, FREQ mapping, EAM App, Siebel EA Export, SREQ Aplikační role, Sheet1, and TA139Arch.
- Functionalities has 955 data rows; Interfaces 54; FREQ mapping 219; SREQ Aplikační role 219; EAM App 555; Siebel EA Export 111.
- FREQ mapping's `Výsledek` values are: 107 `SHODA`, 103 `CHYBÍ V SO`, 6 `CHYBÍ V EXCELU`, 2 `ROZPOR TEXTU`, and 1 `ČÁSTEČNÁ SHODA`. These are the workbook's mapping assessments; they do not by themselves establish approval or current scope.
- The SREQ role sheet records a functionality link for 192 rows, 17 rows with no functionality carrying the same SREQ, 9 links marked for mismatch verification, and 1 marked for correction. It says a change is not evidenced for 215 rows, while 2 are identified as explicitly new elements and 2 as confirmed decisions. This is a useful warning against interpreting every target application responsibility as a change to that application.
- The interface catalog includes `IF_SH_03` (ServiceHub authentication/SSO, OIDC/OAuth2), `IF_IDAAS_01` (OIDC/OAuth2 Authorization Code Flow, shared code, and a DXL token-exchange reference), and `IF_DXL_01` (DXL customer identity/profile/authorization, TMF691 UserInfo/userAssets, REST/OAuth2). These references align with the user's stated MVP SSO direction at a high level. They do not specify the exact CZ token-exchange endpoint/contract or the downstream HTTP-header propagation rule.
- The workbook distinguishes local-portal context transfer from authentication: `F-REQ-CHM-08` / `SREQ-SH-73` describe ServiceHub consuming a protected channel-context cookie; its noted fields are CRM_ID, language, and Return URL, with validity still TBD and cryptographic protection required. This context cookie should be modeled separately from the OIDC/IDaaS session and the DXL access token.
- The entry-visibility decision is unresolved against the FREQ wording: `F-REQ-CHM-21` says WSC and ONSC display the ServiceHub entry point to all authenticated users, while the workbook's newer decision assigns local role/eligibility visibility checks to each channel (`SREQ-PORTAL-12` / `SREQ-PORTAL-13`, linked to `F-REQ-IAM-39`). The workbook marks the text as conflicting and says the FREQ needs clarification.
- Marketplace/Siebel mapping includes CRM ID and V2/V4 segment handling, lookup/unavailability, manual correction, and a rule that a later Siebel lookup should not automatically overwrite saved Marketplace values. These are workbook-stated behaviors and need reconciliation against the latest Martin source and approved requirements before being treated as current.
- The `Sheet1` and `TA139Arch` tabs contain TA-139 business-analysis and architecture material. Statuses such as `TO CONFIRM`, `TO DESIGN`, `TO MODEL`, and `OPEN` are present. Treat the assumptions and target data-foundation design as working analysis, not confirmed Atlas project scope.

### `Atlas.7z` / `Atlas.xml`

- The archive contains one file, `Atlas.xml` (about 112 MB uncompressed; archive timestamp 1 Nov 2026 15:59:46).
- The XML declares a Sparx Enterprise Architect XMI 2.1 export and includes ArchiMate profile declarations. A streaming scan found extensive UML/ArchiMate content, including business-capability, application, integration, data-domain, technology, BPMN, data-model, and sequence-diagram package names. Examples include AppDirect data model and sequence diagrams, IDaaS OAuth2/OIDC, SNOW data model, TMF API model packages, and application/enterprise architecture packages.
- The export also contains the project workspace `90_Sandbox / Zdeněk Šerý sandbox / 01_07_2026_ServiceHub_Atlas_CZ_PR25_0837`, structured into `90.1 Business layer`, `90.2 Application layer`, `90.3 SW Layer`, and `90.4 Infrastructure layer`. The business branch contains VFCZ FREQ/OREQ and BPMN packages; the application branch contains functionality trees for ServiceHub, DXL, IDaaS, Marketplace, CRM/Siebel, ONSC, WSC, SNOW, and others; the SW branch contains customer identity/account model packages and integration/SSO workflows. This gives a concrete route for subsequent blue-layer and data/interface checks. The sandbox location and date-like package name do not establish that the model is current or approved.
- A stereotype scan of that specific ServiceHub/Atlas project subtree found 280 `ArchiMate_Requirement`, 228 `ArchiMate_ApplicationFunction`, 228 `ArchiMate_Realization`, and 18 `ArchiMate_Constraint` elements. It found no explicit `ArchiMate_Capability` elements in that subtree. The full XMI has six `ArchiMate_Capability` elements, all under the separate TA-139 sandbox. This indicates the ServiceHub/Atlas project already has substantial requirements and blue-layer function content, while an explicit ArchiMate capability layer is not present in the inspected project subtree. This is a count of stereotypes, not validation of element-to-element trace links.
- Business analysis is not absent: the same project workspace contains BPMN packages/diagrams, including an integrated customer-onboarding diagram and multiple Group Build processes. The gap found by stereotype scan is specifically the lack of explicit ArchiMate Capability elements in this subtree; it does not mean there is no business-process material.
- Resolving the 228 `ArchiMate_Realization` stereotypes shows they connect application-function `uml:Activity` elements to requirement `uml:Class` elements, including SREQs. Thus the export does contain a blue-function-to-requirement trace; it is not yet a capability-to-requirement-to-function chain in the ServiceHub/Atlas subtree.
- A literal label comparison found 135 ServiceHub functionality rows in Book1 and 44 named ArchiMate Application Functions in the ServiceHub package; after removing the Book1 `F_SH_Lx` prefixes, 11 labels matched exactly. This is only a string comparison: the sources use different granularity and names, so the other labels are not automatically gaps. A requirement/behavior-based crosswalk is needed before changing the blue layer.
- Within that workspace, `90.3 SW Layer / Integration / WF Client base work / SSO` contains one UML Interaction, one CombinedFragment named `Login`, five covered-reference elements, and no `uml:Message` elements in the exported interaction. Therefore the current exported SSO interaction does not yet provide a message-by-message sequence to validate against the user's required ServiceHub → CZ DXL token exchange → downstream DXL header flow.
- The `Customer Identity and Account Model` package contains 15 UML classes, 39 properties, and 19 associations. Class names include `DigitalIdentity`, `CustomerAccount`, `CRMAccountGroup`, `BillingAccount`, `MarketplaceCompany`, `MarketplaceCustomer`, `MarketplaceUser`, `ServiceNowAccount`, `ServiceNowUser`, `AccessAssignment`, and `Ticket`. This is a concrete data-model review target; the inventory alone does not validate its keys, multiplicities, or alignment with the current business rules.
- A separate package named `Entities retations - CZ` contains customer/account concepts such as `Customer TMF629`, `Customer TMF691`, `CRM ID`, Marketplace company/account, ServiceNow account, `User TMF691`, and `UserAsset`; its subtree contains 54 UML Class elements, 32 Property elements, 7 Associations, and 19 Generalizations. Together with the preceding package, this indicates two distinct customer/identity model areas in the export. Whether they are complementary, overlapping, or have different ownership is not established by the inventory and should be checked before consolidating the domain view.
- This establishes that the archive is a substantial EA model export; it does not establish that every model element or relationship has been validated. Detailed model review remains a separate step.

## Current evidence gaps for the broader architecture work

1. Confirm the authoritative current Martin Dostál requirements workbook/version and reconcile its FREQ/SREQ rows to `Book1.xlsx` and the SharePoint Traceability Decomposition.
2. A read-only ID comparison found 157 IDs shared between Book1's FREQ mapping and the EA `90.1 Business layer/VFCZ/FREQs` package. Twelve Book1 IDs are absent from that EA package (`F-REQ-CHM-20`–`27`, `F-REQ-MKT-15`, `F-REQ-ONB-01`, `NFR-01`, `NFR-03`). Text comparison also found 14 mismatches on shared IDs, all `F-REQ-CHM-06`–`19`: the EA export assigns those IDs to direct URL, portal entry, deep-link, and navigation behaviors differently from Book1, which assigns them to customer-context transfer and other reordered entry behaviors. This is evidence of a version/identifier alignment problem; requirement matching must use source text and version history, not IDs alone.
3. A read-only count of formal `ArchiMate_Requirement` names found 110 unique SREQ IDs in the EA ServiceHub/Atlas subtree versus 218 in Book1's `SREQ Aplikační role` sheet. Eighty-seven IDs are shared, 131 Book1 SREQ IDs are not present in the EA subtree, and 23 EA SREQ IDs do not appear in Book1. This indicates that SREQ coverage/version alignment needs a controlled reconciliation; absence from one export is not by itself proof that the SREQ is approved scope or must be added.
4. Verify which of the 103 `CHYBÍ V SO` mappings are genuinely absent from the current, binding Solution Overview and which are mapping/version artifacts.
5. Resolve the two `ROZPOR TEXTU` cases and the single partial match in the workbook, including the ONSC/WSC rule for role/eligibility-controlled ServiceHub entry visibility.
6. For SSO, obtain the CZ DXL token-exchange API contract, token audience/claims/expiry, error behavior, and downstream header propagation details before drawing the sequence as a confirmed design.
7. Review the EA XMI element/relationship IDs and model packages against the business traceability and application-interface catalog; the current scan only inventories structure and selected names.
8. For Marketplace-to-Siebel customer matching, confirm authoritative CRM ID/CA ID semantics, V2/V4 source and update rules, manual override ownership, reconciliation reports, mismatch handling, and behavior when Siebel is unavailable. The reviewed Marketplace BSR does not answer these business/data-lifecycle questions.
