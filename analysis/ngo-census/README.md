# NGO census research workflow

This directory holds the implementation notes for the wild steelhead organization census. The [requirements document](requirements/Steelhead_Organization_Census_Requirements.md) defines the required behavior and scientific safeguards. This README explains where research lives and how to retain and reuse it. The layout below is the intended organization; files and directories are created when needed, not all at once. A database is not required.

## What is repeatable and what is reproducible

Research is a documented, repeatable procedure, not a promise that another agent will discover identical sources or reach identical proposals. Search results, websites, and AI responses change. Retain the evidence and reviewed decisions so users can inspect how findings were reached.

Release reproduction starts after research and review: **agent research → retained evidence and reviewed findings → reproducible report generation**. It reads the selected committed records, narrative, and footprints and retained external evidence. It does not search again, ask an AI to re-extract filings, or repeat judgments. New discoveries and revised interpretations enter the next research assignment rather than modifying an earlier release.

Save substantive AI-written summaries in the relevant reviewed activity/profile notes. If a release needs an authored cross-organization narrative, keep that text in a maintained file such as `methods/report-narrative.md`, with supporting references and review metadata. Route new or revised interpretations through staging, independent review, and owner integration approval before committing them. The report builder uses those exact saved texts or deterministic templates over recorded values; it must not generate fresh AI prose during reproduction. The repository can evolve its narrative file arrangement without changing this rule.

Verify reproduction with web retrieval and AI calls disabled. The same commit and retained inputs must yield the same findings, calculations, map geometry, and substantive narrative; documented formatting timestamps may differ. A model's name or prompt alone does not preserve its output, and storing them is not a substitute for saving the reviewed findings.

## Agent role instructions

Proposed pilot instructions are available for the [researcher](requirements/researcher-agent-instructions.md), [reviewer](requirements/reviewer-agent-instructions.md), and [steward](requirements/steward-agent-instructions.md) agents. These role instructions describe bounded assignments and handoffs; they do not establish that agents or release automation are already running.

## Pilot model and reasoning settings

Keep role settings in [methods/agent-settings.json](methods/agent-settings.json), not as a fixed GPT release in the requirements. The owner selected **GPT-6.1 Sol** (`gpt-6.1-sol`) on 2026-11-11 for all three pilot roles. Keep the model and baseline reasoning settings fixed for the first few assignments, then evaluate evidence quality, missed errors, and correction burden before changing them. If unavailable in the execution environment, report the limitation rather than silently substituting another model. Provisional reasoning settings are researcher **medium**, reviewer **high**, and steward **medium**. Increase effort for consequential ambiguity or conflicts as needed within the assignment scope and record the change. These are starting settings to evaluate, not a guarantee of quality.

Run the reviewer in a fresh session. Give it the addressed handoff, proposed findings, retained sources, applicable methods, and explicit correction history, not the researcher's full chat history or private reasoning. The reviewer must independently examine evidence. A different model is neither required nor sufficient for independent review, and using the same model does not eliminate shared blind spots.

Each role appends an execution note to the handoff: role/session identity, configuration revision, requested model/effort, actual model identifier/release and effort if exposed, and any setting changes with reasons and affected work. Reviewer notes also belong in `review.md` and its retained group-review reference. Unknown actual settings must be labeled unknown with the reason; configuration intent is not proof of runtime settings. Do not overwrite earlier role execution notes.

After a few representative pilot assignments, compare verified quality, errors missed/caught, elapsed time, and correction burden. Include deliberately flawed proposals in isolated test work, never accepted research records. Test changes to model or effort against those same examples before adopting lighter settings or a different reviewer model. Model changes affect future research; reproducing a saved release does not require the original model or fresh AI calls.

## Directory layout

```text
analysis/ngo-census/
├── README.md
├── requirements/
│   └── Steelhead_Organization_Census_Requirements.md
├── input-data/
│   └── seed-candidate-list.md
├── staging/
│   ├── handoff.md
│   ├── review.md
│   └── proposed-changes/
├── sources/
│   ├── entities.csv
│   ├── index.csv
│   ├── org-wildfishcon/
│   │   ├── financial-history.csv
│   │   ├── activities.md
│   │   ├── footprint.geojson
│   │   ├── 990/
│   │   │   ├── 2022-original.pdf
│   │   │   ├── 2022-amended.pdf
│   │   │   └── 2023-original.pdf
│   │   └── program-reports/
│   │       └── 2024-annual-report.pdf
│   └── org-tuwsi/
│       └── activities.md
├── methods/
├── scripts/
├── templates/
├── tests/
├── discovery-log.csv
└── decisions.md
```

Organization names and document filenames in this tree illustrate placement; they do not assert that those filings or reports have been obtained. Add other source categories, such as `t3010/` and `web-captures/`, when appropriate. Avoid empty files and placeholder records that could be mistaken for completed research.

For this census, `sources/` is the self-contained home for both retained original public documents and reviewed research records. This is the census-specific exception to the repository's general `data/raw/` and `data/metadata/` placement conventions. Originals and research interpretation remain visibly separate by filename and subdirectory. Generated reports and exports go under the repository-root `output/ngo-census/<release-label>/` directory and remain untracked.

## File roles

| File or directory | Purpose |
| --- | --- |
| `input-data/seed-candidate-list.md` | Cumulative candidate names and permanent assigned IDs; initializes discovery without implying eligibility |
| `staging/handoff.md` | One active assignment: starting commit, candidate IDs, proposed destinations/changes, evidence, gaps, and final disposition |
| `staging/review.md` | Independent review of the exact proposed revision, item dispositions, corrections, and owner decisions needed |
| `staging/proposed-changes/` | Only new evidence and proposed record changes, not a copy of the retained collection |
| `sources/entities.csv` | One registry of candidate identities, aliases, screening status and rationale, and parent or duplicate references; includes pending, included, excluded, and deferred candidates |
| `sources/index.csv` | One index of retained documents, their origin, exact contents, and location; shared across organizations |
| `sources/<org-id>/financial-history.csv` | Readable financial observations for that organization, by fiscal period and measure, with source and review references |
| `sources/<org-id>/activities.md` | Readable descriptions of programs or coherent bodies of work, their geography, life stages and approved risk codes, supporting sources, and reviewed interpretations |
| `sources/<org-id>/footprint.geojson` | Saved approximate extent of evidenced direct influence, including null geometry when location is unsupported |
| `sources/<org-id>/990/`, `t3010/`, `program-reports/` | Retained original documents, separate from our extracted values and interpretation |
| `discovery-log.csv` | Search batches, candidate discoveries, effort, stopping reasons, and remaining gaps |
| `decisions.md` | Consequential judgments, reasons, sources, and second review where required |
| `methods/` | Codebooks, research conventions, and report configuration as needed |
| `scripts/` | Extraction helpers, validation, and report generation as implemented |

These are maintained research inputs, not disposable report outputs. Reporting reads them at a specified Git commit. Combined CSVs or workbooks may be generated in `output/`; they are not additional authoritative copies to maintain.

Keep entity identity and screening in `entities.csv`, financial values in the organization's financial history, and source metadata in `index.csv`. Reference those records instead of maintaining duplicate values. Relationships can initially be recorded using parent and duplicate fields in the registry and clearly identified activity participants; introduce a separate relationships file only when needed.

## Owner review by exception

Standing owner instruction, adopted 2026-11-11: **assume owner approval unless an owner decision says otherwise**. Researchers and reviewers do not wait for per-entry owner approval before their ordinary addressed handoffs. Their proposals remain unaccepted research until independent review; standing approval is not a scientific review disposition.

The steward may integrate an independently accepted, current, evidence-supported, conflict-free subset under this standing approval, after validating its dependencies, expected retained state, and usable HTML preview. No owner decision JSON is required and no routine owner-response wait is imposed. Record the applicable policy revision, exact eligible change IDs, proposal inventory/digest, and approval basis in the handoff before integration. Distinguish **Approved by standing policy** from **Explicit owner acceptance** and from **Held — unresolved**; never invent a human inspection or signature.

Owner-supplied chat instructions and validated `owner-decisions.json` entries override the default for the named proposals. Accept records explicit acceptance; reject excludes; defer preserves for later; request changes routes a correction with the owner's comment. Unmentioned proposals remain eligible for the standing default if all review and validation conditions pass. Do not request a decision file just to confirm that there are no exceptions. If the owner says a decision file is forthcoming, wait on its affected scope. Preserve all supplied decisions and review history; conflicting owner instructions require clarification for the affected scope.

Unreviewed, rejected, correction-requested, deferred, stale, unsupported, or conflicted proposals are not integration-eligible. Unresolved researcher/reviewer disagreements, material identity/method/estimate questions, and unresolved owner exceptions hold the affected proposals and their dependents. Explicit owner acceptance does not bypass independent review. Other eligible proposals may proceed. An accepted lead stays a lead.

After substantive revision, obtain renewed independent review and regenerate proposal hashes/digest; reevaluate eligibility under this policy. Do not silently discard a prior owner rejection, deferral, or correction request because its exported hash became stale: keep that scope on hold until the exception is demonstrably satisfied or the owner resolves it. Stale exports cannot authorize new content. Preserve the original export and validation revision before editing the handoff.

Standing approval covers eligible retained-data integration only. It does not authorize commits, staging cleanup, agent launches, pushing, or publication. Existing explicit permissions for those actions remain necessary. The serial execution and addressed-handoff rules are unchanged. The owner can suspend or narrow this policy at any time.

## Single assignment staging

Use one shared `staging/` area with exactly one active assignment at a time. There are no batch subdirectories. Do not start another assignment until the steward closes the current one and preserves its disposition. Staging is provisional work, not a source of accepted report inputs, and it is not a security boundary.

Only one census agent may execute at any time across this workflow, including read-only review and preview preparation. Do not overlap researcher, reviewer, or steward turns. A handoff records who should act next; it does not itself start another agent. The owner or coordinating session starts the addressed role only after the sending agent has stopped. While awaiting an owner decision, preserve staging and stop dependent agent execution.

A fresh researcher assignment requires a small explicitly assigned set of seed IDs and an empty staging area: no previous `handoff.md`, `review.md`, or proposal files. An absent staging directory or empty `proposed-changes/` directory is acceptable. Do not erase leftovers to make this condition appear satisfied; send occupied staging back to the steward for closure. A researcher resuming addressed corrections is the exception: reuse the existing assignment rather than demanding empty staging.

Every transfer updates `handoff.md` with `from_role`, `to_role`, `current_role` (matching `to_role`), transfer date, reason, expected next action, and the applicable proposal/review revision or hashes. Preserve the transfer history in the same file. Reviewer and steward entry requires an explicit handoff addressed to that role; a matching `current_role` by itself is insufficient. Every sending agent must stop after its handoff. These fields are excluded from the approval digest.

Track `current_role` in `staging/handoff.md`: `researcher`, `reviewer`, `steward`, `owner`, or `closed`. This controls who acts next, not candidate eligibility. Only that role may change the proposals or their review/integration state. The owner may always steer the assignment. Record each transfer with a short reason; do not run the roles concurrently on one staging assignment.

- The researcher hands frozen proposals to the reviewer. Correction requests return control to the researcher, who then resubmits for review.
- The reviewer hands a dispositioned proposal set to the steward. Questions needing owner judgment transfer control to the owner; after the response, the steward records it and routes corrections or integration to the appropriate role.
- While `current_role` is `owner`, agents preserve the proposal and wait on dependent work. After authorized integration and history capture, the steward records the assignment as `closed`, preserves that record in Git, and clears staging before another fresh researcher assignment.

1. **Researcher:** Initiate the shared local HTML review page from the staging records before handoff, labeled **research proposal**. Read and reuse retained `sources/` records. Put new documents and proposed findings in `staging/proposed-changes/`; use paths relative to the census directory to identify their intended destinations, such as `proposed-changes/sources/org-wildfishcon/financial-history.csv`. Record the assignment, organization IDs, starting commit, additions/corrections, proposed shared-index entries, checks, and gaps in `handoff.md`. Never edit retained records directly as part of this role.
2. **Reviewer:** Refresh that same page from `review.md`, labeled **reviewed proposal**, exposing independent dispositions and correction requests. Check the exact proposed changes against retained evidence and record accepted, correction requested, deferred, or rejected for each substantive proposal in `review.md`. Identify the reviewed revision using a Git commit if authorized, otherwise file paths and content hashes recorded in the review. Changed reviewed content must be checked again; prior review does not automatically apply to later edits.
3. **Steward:** Complete and validate the same owner-facing HTML integration preview, labeled **ready for owner signoff**, at repository-root `output/ngo-census/previews/owner-review/index.html` with a broad summary, file/entry-level before-and-after details, evidence links, reviewer dispositions, and an exact proposal digest. Apply the owner-review-by-exception policy to that exact accepted subset before integration; record standing approval or applicable explicit owner decisions, and hold unresolved exceptions. Check that current destination records still match the starting state or resolve intervening changes explicitly. Retain source IDs and correct destination references, run applicable validation, and record what was integrated and the integration commit when authorized. Staging is not moved wholesale into `sources/`.
4. **Owner:** Inspect any stage as desired and optionally supply exceptions or explicit acceptance through chat or the decision JSON. Routine handoffs and eligible integration do not require per-entry owner action. Resolve consequential questions that the agents cannot settle within approved methods before the affected material is integrated. Deferred material may remain outside accepted storage while other accepted work proceeds. Publication still requires the owner's separate explicit authorization of the reviewed report and selected commit; integrating research does not publish it.
5. **Close and reset:** Record a disposition for every proposal. Preserve unresolved work in an explicit deferred record with retrievable evidence; do not discard it during cleanup. Before clearing/reusing staging, retain its handoff, review, and disposition in Git history through an authorized commit (including source material needed to understand deferred work). The owner may authorize integration, a history-preservation commit, and a later cleanup commit together in the integration signoff. The steward first records closure and preserves the completed handoff, review, and proposal dispositions in the history-preservation commit. In the later authorized cleanup commit, remove the active handoff, review, and all proposal files, after preserving deferred evidence and recording deferred work. Leave staging empty for the next assignment. If committing is not authorized yet, leave staging intact and do not start another assignment.

The independent reviewer may be a separate agent or a human and must identify which. The same actor must not author and independently accept the same finding. Owner integration authorization may be supplied by the standing policy or an explicit decision; release authorization remains a separate explicit human decision; agent review is not human verification. Routine checked observations may share a group review with explicit record IDs and evidence scope; no per-cell approval record is required.

The steward carries accepted review metadata into retained findings or a referenced group-review entry in `decisions.md`: review ID, reviewer identity/type, date, source version/hash, checked record IDs and scope. Preserve these references when staging is cleared. Prior reviewed findings retain their earlier references without repeated checking.

For owner signoff, hash a deterministic inventory of the selected integration subset: change IDs/operations, destinations, proposed file hashes or after-values, expected before-values, source identities/hashes, dependencies, and reviewer dispositions for those changes. Store the inventory in a labeled handoff section, not only in disposable HTML assets. Exclude approval responses, current-role/transfer entries, integration/completion notes, display timestamps, and the digest field itself. This prevents recording approval from changing what was approved. If the selected subset changes, regenerate its digest and reevaluate standing-policy eligibility and any explicit owner exceptions; unrelated deferred items need not invalidate unchanged approved proposals.

At the effort limit or when a requested correction cannot be completed, return the question to the owner or record it as deferred with its reason, next action, and retrievable evidence. Deferred work is not accepted data and need not keep an otherwise dispositioned assignment open indefinitely.

Standing approval authorizes only eligible integration. Any request for additional permission must distinguish (1) an exceptional integration decision, (2) committing the handoff/review and integrated changes, and (3) a subsequent staging-cleanup commit. The owner can authorize these together or separately. Do not ask again for actions already explicitly authorized. Pushing and publishing require their own explicit authorization and are not implied by those permissions.

### Shared review page across roles

The researcher initiates one evolving HTML page at repository-root `output/ngo-census/previews/owner-review/index.html`; the reviewer and steward refresh that same page on their sequential turns. Use one shared renderer, not three independently authored HTML interpretations. Its source is `staging/handoff.md`, `staging/review.md` when present, staged proposals, and relevant retained before-values. The provisional renderer is [scripts/render-staging-review.py](scripts/render-staging-review.py), using [templates/staging-review.html](templates/staging-review.html). HTML and preview assets are derived, untracked output, never the authoritative record of findings, review, or approval.

Label the page **research proposal**, **reviewed proposal**, or **ready for owner signoff**, and show the current role, assignment/seed IDs, source base commit, generation time, and exact input revision/hashes. Research-stage findings are unreviewed; reviewer dispositions come only from `review.md`. Lead-only findings remain distinct from accepted retained findings. A reviewed proposal may contain corrections or deferrals; the label does not imply acceptance of everything. Only the steward can mark a fully reconciled integration subset ready and display its final approval digest. The legacy `signoff` stage label means readiness for integration evaluation, not a mandatory owner-response wait under the standing policy.

Each role refreshes the page before handing off and after substantive corrections or review updates. Rendering does not permit an agent to change another role's findings or decisions. If proposal inputs no longer match the reviewed hashes, visibly flag the affected acceptance as stale and route the changed content for review; never silently carry approval forward. Before owner signoff, the steward checks the complete page, before/after details, evidence links, current review scope, and proposal digest. The owner may inspect earlier stages without approving them. Owner decisions remain recorded in the handoff, not only in HTML.

Use the [provisional staging record format and testing instructions](methods/staging-record-format.md), with starter records in `templates/staging/`. The renderer validates recorded structure, hashes, review freshness, dependencies, and expected destination values; it does not verify scientific truth or authenticate owner approval. A failed rendering step is a recorded handoff limitation, and the steward cannot request final signoff until the required usable page is produced. After staging closes, refresh to a **no active assignment** notice or remove the old preview so a later assignment cannot display a stale proposal as current.

The HTML integration preview is local and untracked; it is not the public census report. The active role provides working file/evidence links over localhost HTTP; the steward verifies them before signoff, records owner decisions in `staging/handoff.md`, and regenerates the preview and reevaluates approval eligibility if substantive proposals change. The recorded standing instruction supplies default approval; the absence of a JSON file is not an integration blocker. Static HTML alone does not authenticate an explicit owner decision. See the [steward instructions](requirements/steward-agent-instructions.md) for the required summary and drill-down views.

Include only additions and corrections in `proposed-changes/`. For an existing table, provide proposed rows or a focused patch and identify the affected record/source IDs and expected previous values; do not duplicate all organizations or their source history. New or amended original documents are retained as distinct files after acceptance. All staging content follows the same public-data and reuse restrictions as retained storage, because staging may itself enter public Git history.

Reporting reads accepted retained files only and excludes `staging/`. An active assignment may coexist with a release generated from an earlier clean committed retained state; staging is not evidence that unreviewed findings have been accepted. The researcher hands off, the reviewer evaluates, and the steward integrates; the same staging directory records that sequence without parallel competing copies.

## Permanent organization IDs

Use the assigned ID from the [seed list](input-data/seed-candidate-list.md), such as `org-wildfishcon`, for the organization directory and cross-references. IDs are permanent even after a name change. Never reassign them or regenerate them from updated names.

Keep the seed list cumulative. Candidate status lives in `entities.csv`, not in the presence or absence of a seed entry. A duplicate retains its ID and points to the canonical entity; exclude it from duplicate counts. Programs have their own IDs and a parent reference where supported, without assuming legal independence.

## Sources and provenance

Here, checking a source's origin means confirming its publisher, organizational identity, and document identity. It does not verify every assertion in the document or every value extracted from it.

### Original source files are the default

Collect and retain actual publicly available source files: IRS 990 PDFs, CRA disclosures, annual reports, program summaries, project descriptions and technical reports. Preserve downloaded originals byte-for-byte. Researcher-written summaries, observation notes, search snippets and short selective extracts do not substitute for an obtainable original. Prefer an available downloadable report over a page that merely describes it, within the assigned effort and document limits; do not expand into unrelated financial extraction just because a filing is retained for identity.

For web-only evidence, retain a faithful, inspectable page capture (such as a browser print-to-PDF or self-contained saved page), with the public URL and retrieval date. Label its capture method, included sections, missing dynamic content or assets, and any limitations. A faithful capture preserves source wording and context; a researcher paraphrase is a separate interpretation. Keep source evidence non-executable in the review interface; a text fallback is not proof that a complete page was captured.

Keep originals/captures separate from extracted observations and activities. Use `staging/proposed-changes/sources/<org-id>/990/`, `t3010/`, `program-reports/` or `web-captures/` for proposed evidence, with corresponding retained destinations under `sources/<org-id>/`. Use the permanent candidate ID. Record source ID, publisher/title, public origin URL, retrieval and publication dates (unknown where appropriate), actual period, intended path, capture type, exact retained-file SHA-256 and relevant pages/sections. Record the upstream filename where a readable local filename differs. An original is stored once and referenced by its source ID; amendments/new captures receive distinct versions and supersession links.

Full retention must respect access/reuse conditions and exclude prohibited private or individual donor information. If a full copy cannot be retained, document the specific reason (for example reuse restrictions, prohibited information, technical failure, or assigned effort limit), attempts made, and what remains missing. Retain a permitted clearly labeled extract or durable external archived copy where feasible; record capture scope and hash accurately. A live URL alone is not retained evidence. Never label a paraphrase as an original or an extract hash as the original-file hash. If the retained evidence is insufficient to inspect a material claim, hold that claim for correction or deferral. An exception is not satisfied merely by choosing short excerpts for convenience.

Start `sources/index.csv` with these fields, adding others only as needed:

| Field | Meaning |
| --- | --- |
| `source_id` | Permanent reference used by financial and activity records |
| `org_id` | Primary organization concerned; other records may reference the same source |
| `path` | Retained file path relative to this census directory, or recorded external archive location |
| `title`, `publisher`, `url` | Document identity and public origin |
| `period`, `published_date`, `retrieved_date` | Time covered and document/retrieval dates, with unknowns explicit |
| `sha256` | Hash of the exact retained contents |
| `origin_checked_by`, `origin_checked_date` | Person and date of the origin check, left pending until actually checked |
| `supersedes_source_id` | Prior source replaced or amended, if applicable |
| `capture_type`, `capture_method` | Original download, faithful web capture, or exception extract; how it was obtained |
| `original_filename` | Publisher filename where provided; unknown for a web-only page |
| `retention_exception`, `capture_limits` | Specific reason and scope when full source retention is unavailable; otherwise none |

Retain permitted original documents without editing their contents. Use fiscal year rather than download year for filing names, and add a distinguishing suffix if necessary. An amendment or replacement gets a new filename and source ID; do not overwrite the old document. Keep the original source record even when a later source supersedes it.

Store each document once. For example, retain a parent organization's filing in the parent folder and reference its source ID from any relevant program record. Do not copy the filing into each program's folder or attribute the parent's entire budget to a program.

Only public organizational evidence is eligible. Do not commit restricted documents, individual donor records, private personal data, or credentials. Where an original contains prohibited information, retain only a permitted extract free of that information and label it as an extract. Respect reuse conditions. Large or non-redistributable evidence may remain in a permitted durable archive, with its hash and retrieval location recorded; a live URL alone is insufficient for reproducibility.

## Reviewed findings and reuse

A financial history is a table intended to be read directly. Each row identifies the organization, financial metric, amount, currency, fiscal period, source ID and locator, and review information. Include reporting boundary and missing-value reasons where applicable. Do not replace unavailable values with zero.

Keep review notes lightweight: reviewer, review date, source version or hash, and scope of the check. One review reference may cover several financial rows checked together. Activity entries similarly identify the supporting source IDs and sections and distinguish documented statements from research interpretation.

Once checked, a historical observation is reused in later releases. A correctly documented 2010 value remains a valid historical observation; it does not become a current-year value. Source-origin checking and extracted-value review are separate checks.

For subsequent research:

1. Read the existing registry, source index, financial history, and activity notes before searching or extracting again.
2. Reuse unchanged reviewed findings; focus research on missing periods, newer disclosures, new activities, and amendments.
3. Reopen review when a source changes, an error or conflict is found, or a method or identity change affects the interpretation. A new report date alone is not a reason to repeat review.
4. Preserve earlier observations and sources. Add an amended or corrected observation with a reference to what it supersedes and record substantive decisions. Git retains the earlier record state.
5. Check the diff and commit the new research. Do not duplicate the entire organization directory for each release.

## Generated output and public viewing

Each generated release lives under `output/ngo-census/<release-label>/`, relative to the repository root. For example:

```text
output/ngo-census/2026-11-11-r1/
├── index.html
├── map.html
├── assets/
├── entities.csv
├── financial-history.csv
├── activities.csv
├── geojson/
│   ├── index.json
│   ├── org-wildfishcon.geojson
│   └── org-tuwsi.geojson
└── manifest.json
```

The HTML report and combined CSV exports are generated from the maintained research records. The `geojson/` directory contains release-specific copies of every included entity's committed footprint; `index.json` lists their IDs, names, paths, and geometry status so the viewer can find all files. These copies are output artifacts, not additional research files to edit. The manifest inventories the release outputs and their hashes; it does not include its own hash.

During prototyping, use GitHub Pages as the provisional host for the static report and GeoJSON viewer, and GitHub Releases for archived downloadable bundles. GitHub Actions can generate and deploy the static bundle without committing generated files to the source tree. Each deployment must assemble the landing page and all retained release directories; publishing only the newest bundle must not remove earlier report/map addresses. This is a provisional hosting choice, not a permanent dependency of the research data or reporting formats.

The anticipated project-site base is `https://toddringler.github.io/steelhead-marine-risk-discussion-manuscript`, based on the current repository owner and name. Confirm the actual address when Pages is configured; it is not asserted to be live. Use this URL convention:

- `<public-base>/ngo-census/` — stable landing page linking to the latest release and the release archive.
- `<public-base>/ngo-census/releases/<release-label>/index.html` — permanent address for a specific report.
- `<public-base>/ngo-census/releases/<release-label>/map.html` — that release's GeoJSON viewer.

These are address conventions, not currently live URLs. GitHub Pages is assumed for the prototype; Pages configuration, deployment workflow, and the final public address remain to be confirmed. The site is static HTML, JavaScript, and data files; it needs no application server or database. The report should provide searchable organization profiles or a searchable organization table, source and commit links, and data downloads. Publishing a newer release updates the landing page without replacing older release bundles.

The map viewer loads all GeoJSON files listed in the selected release's index. It provides pan/zoom, an organization search/list, show/hide controls for individual footprints and all footprints, and zoom to an entity or all visible extents. Selecting a footprint identifies the organization and links to its report entry, supporting activities/sources, and GeoJSON download. Overlapping footprints remain individually selectable through the organization list. Entities with null geometry stay visible in the list with their reason, rather than silently disappearing. Partial mapping and approximation limits remain explicit.

Keep the viewer and footprint data in the archived release bundle. A live basemap may be used for context, but loss of the tile service must not prevent displaying footprints, the organization list, or provenance. Viewing the release must not trigger new research or live geocoding. Ordinary users access the hosted HTTP/HTTPS address; maintainers can also serve the local bundle over HTTP for review. Opening `map.html` directly from a file browser is not the supported viewing method.

For the prototype, archive the exact public bundle and manifest as versioned GitHub Release assets, retaining prior releases unchanged and a separate backup as required. GitHub Pages provides convenient browsing; the archive preserves downloads and reproduction materials. Generated files remain untracked in the source checkout.

## Dated reports and releases

Reports are evidence snapshots published when useful, potentially several times in one year. They retain the observations' own fiscal periods and distinguish new research from actual organizational change. Section 03 of the discussion paper remains an open dependency for the full risk-coded census; discovery and preliminary profile preparation can proceed as described in the requirements.

### Research then preview then publish

Routine research and public report publication are separate actions:

1. **Research:** Add documents, update the source index and reviewed findings, then commit and push whenever useful. Pending research can remain pending. Ordinary pushes may run validation but must not create a GitHub Release, deploy a census report, or change the public latest-release link. New public repository commits do not mean the published evidence snapshot has changed.
2. **Preview:** When accumulated changes merit publication, select an exact committed state and evidence cutoff. Generate and inspect a local report/map preview, clearly labeled as a non-release. Complete required reviews and correct problems in new commits; regenerate the preview from the final candidate commit. Preview artifacts belong in an untracked location such as `output/ngo-census/previews/<commit>/` and must not enter the public release archive or latest-release listing.
3. **Publish explicitly:** For the prototype, use a manually triggered GitHub Actions workflow, provisionally named **Publish census release**. Supply the full generating commit hash, a unique release label, and evidence cutoff, plus any declared activity window or comparison period. The workflow checks out that exact commit, validates it and required reviews, and builds the release bundle under `output/ngo-census/<release-label>/`. Record all supplied parameters in the manifest; do not silently use the latest branch state.
4. **Archive and deploy:** Only after successful checks and explicit publication authorization, publish the frozen bundle and manifest as GitHub Release assets and deploy the static report/map to GitHub Pages. Update the landing page only when that release is available. If validation or publication fails, keep the existing published release in place. Reusing an existing release label must not overwrite its contents; corrections require a new label. Previously published release addresses and archives remain unchanged.

The manual workflow invocation is the explicit request to publish the selected reviewed state; committing research, pushing, or generating a preview is not. This describes the intended prototype mechanism, not an already configured GitHub Actions workflow.

Generate a published report from a clean committed state. The report identifies its generating commit and exact starting seed revision, links to saved GeoJSON, and states evidence cutoff, coverage, and financial-period limits. Web research, AI extraction/interpretation, review, authored narrative, and manual drawing are retained inputs, not tasks to repeat when reproducing a report. Release generation must work without new web retrieval or AI calls.

Use one release manifest for the release label, publication date, cutoff, seed references, generating commit, retained external inputs, reproduction command and environment, review, and output hashes. Archive the report, manifest, any required external evidence, and generating repository snapshot as immutable release assets or another durable archive. A repository link alone is not a backup. The completed manifest and report are generated after the source commit, so their hashes do not need to be embedded in that same commit.

The provisional staging-preview renderer and synthetic tests are available now; see [testing instructions](methods/staging-record-format.md). Census release generation, integration automation, and a public map viewer are not implemented. A runnable release-report command will be documented here when implemented. This README defines file conventions; it does not imply that the reporting system is already built.

## Entering owner decisions

The shared HTML preview supports per-proposal accept/reject/defer/request-changes choices and comments. Download the choices and give the file to the steward with an instruction to use it. Entries are not saved automatically. No file is required for default approval of an eligible reviewed subset. See [decision-file handling](methods/staging-record-format.md#owner-decision-entry) for validation and handoff rules. This interface does not perform Git operations or bypass review.

### Existing extract-based pilot

The Wild Salmon Center demonstration initially used selective researcher extracts. It tests handoffs and interpretation, but does not demonstrate the default original-file collection/reuse requirement. Do not silently relabel its extracts as originals or treat earlier review as acceptance of newly collected files. Filling this gap requires a separately addressed research correction, actual source acquisition/capture, updated provenance/hashes and renewed review of affected proposals.

## Coordinated agent execution

Assign a bounded organization task to the [coordinator](requirements/coordinator-agent-instructions.md) to manage researcher, independent reviewer, corrections and steward without manually relaying chats. One worker executes at a time; the coordinator only waits/monitors while it runs. Completion and addressed file handoffs must both be verified before dispatching the next role. Independent reviewers get fresh sessions. Default limit: two substantive correction rounds, then defer affected work or escalate a concise owner question.

The coordinator keeps an ignored resumable scheduling journal under `output/ngo-census/coordinator/state.json`, uses standing owner approval for eligible integration, and does not gain commit, cleanup or publication authority. No unattended service is installed. The first test uses isolated synthetic data under `output/ngo-census/coordinator-smoke/`, not live staging or retained census evidence.
