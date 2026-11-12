# Wild Steelhead Organization Census Requirements

Version 0.14 | Tightened review draft | 12 November 2026

## 1 Purpose and scope

Identify, analyze and track NGO-like organizations affecting wild steelhead conservation across the **entire Pacific Rim**. Document identity, resources, relationships, activities, life stages/risks and change over time, with evidence and uncertainty. Research is repeatable but may discover different evidence; release reproduction reuses saved reviewed inputs without new research (NFR-01).

Include independent nonprofits/charities and comparable bodies, sponsored projects, initiatives, coalitions, chapters and parents, including historical/inactive entities. Geography covers Pacific-bordering countries/territories, relevant inland watersheds and shared offshore/international waters; organizations headquartered elsewhere qualify through an evidenced in-scope pathway. Geographic scope does not presume steelhead occur everywhere.

Distinguish headquarters from operations, wild steelhead from hatchery fish/resident trout/salmon generally, and direct from indirect conservation pathways. Record supportive, adverse, mixed or uncertain effects without inferring intent. Government agencies, Indigenous governments, universities, public partnerships and similar institutions belong in a separate census; necessary partner references remain excluded from NGO totals. Public-data restrictions are in EVD-06/NFR-05.

### Requirement conventions

Imperative statements in identified requirements have MUST force unless qualified by SHOULD or MAY. MUST is mandatory for the applicable phase; SHOULD is expected unless a documented exception is approved; MAY is optional. P0 denotes baseline release blockers, P1 denotes the next operational phase, and P2 denotes later analytical capability. IDs remain stable across revisions. Proposed methods in this version require approval before being treated as established census practice.

## 2 Governance

The [workflow](../workflow.md) owns operations/permissions; the [format reference](../methods/staging-record-format.md) owns file fields; the [README](../README.md) provides navigation. The owner sets scope/methods and release decisions; coordinator routes, researcher proposes, independent reviewer checks, and steward integrates. Author and independent reviewer MUST differ; agent review is not human verification.

### Core operating requirements

**GOV-01 |** P0 | Maintain the inclusion policy, codebook, named owner and concise decision log in the public repository. Consequential judgments MUST identify affected records, evidence, date and reason; routine transcription/formatting uses Git history.

**GOV-02 |** P0 | Each candidate MUST be pending, included, excluded or deferred. Included requires reviewed scope support; exclusion/deferral requires reasons and discovery provenance. These screening states are separate from agent roles and review dispositions.

**GOV-03 |** P0 | Findings and release readiness MUST receive independent review by an identified separate agent or human. Check every material estimate and ambiguous identity; group reviews identify exact checked records and evidence scope. Unchecked records MUST NOT inherit acceptance without an owner-approved sampling policy. Retain durable review references. Integration follows standing policy/owner exceptions; publication requires separate explicit owner authorization and passed release checks.

**GOV-04 |** P1 | Research SHOULD be refreshed when disclosures, discoveries, corrections or priorities warrant it, including missing filings/changed websites. An annual planning review MAY occur but MUST NOT impose annual publication.

Reports distinguish legal-entity counts, operating-node counts, financial capacity, expenditure, attributed effort and biological outcomes; state counting unit/date. Network centrality describes observed connections, not impact. Git preserves revisions; the decision log explains consequential judgments rather than duplicating per-field history.

## 3 Entity model and counting rules

Permanent entity IDs survive names/years. Legal identifiers identify legal bodies, not every program; dated relationships connect operating nodes to bodies.

| **Object** | **Meaning** | **Counting treatment** |
| --- | --- | --- |
| Legal organization | Independently constituted body with verified legal form | Count once in legal cohort |
| Sponsored project | Program operating through a fiscal sponsor | Operating node unless separate legal status is evidenced |
| Initiative or coalition | Coordinated work or membership arrangement | Node; no assumed independent revenue |
| Chapter or affiliate | Local unit with documented governance | Legal or operating count according to evidence |
| Parent organization | Controller, host, or umbrella body | Count legal identity once; link children |
| Excluded institution reference | Non-NGO partner or funder recorded only to explain an NGO relationship | Exclude from entity counts and financial totals; link to separate census where available |

### Identity requirements

**ENT-01 |** P0 | Store canonical name, aliases, entity type, legal status, country, identifiers, website, relevance rationale, operating status and evidence. Unknowns MUST remain explicit.

**ENT-02 |** P0 | Duplicate checks MUST consider identifiers, aliases, domains, addresses and relationships. Shared names/websites alone MUST NOT trigger merges.

**ENT-03 |** P0 | Structure/succession relationships—parent, chapter, sponsor, program, affiliate, predecessor, successor and merger—MUST have evidence and effective dates where known. Unknown dates remain explicit; inferred/ambiguous relationships need confidence and rationale.

**ENT-04 |** P0 | Merges/splits MUST preserve earlier IDs/aliases and an evidenced decision. Git history MUST support correction and unchanged historical releases.

**ENT-05 |** P0 | Distinguish NGO candidates from excluded institutional references independently of legal status. Use GOV-02 screening states; institutional references MUST remain outside NGO counts and budgets.

### Double counting controls

**CNT-01 |** P0 | Financial observations MUST identify reporting body, period, consolidation boundary, metric and source. Programs MUST NOT inherit parent revenue as their own.

**CNT-02 |** P0 | Consolidated parent amounts MUST NOT be added to included child amounts. Unknown boundaries MUST be flagged and excluded from consolidated totals until resolved.

**CNT-03 |** P0 | Record evidenced transfers and possible financial overlap. Combined/net totals MUST use reconciled boundaries and transfers; otherwise report separate values with an explicit non-additivity warning. Comprehensive funding-flow reconstruction is optional later work.

**CNT-04 |** P0 | Coalition/partnership membership MUST NOT create attributable spending. Shared work MUST retain one activity ID, participants and any evidenced allocation.

## 4 Discovery and saturation

P00–P06 organize discovery; reconcile their proposed mapping with the historical workbook before importing earlier searches. Preserve original historical labels/queries/results.

| **Pass** | **Proposed purpose** | **Required coverage evidence** |
| --- | --- | --- |
| P00 | Initialize from the versioned seed list and reconcile baseline | Seed path, Git revision, content hash, source entries, aliases, known gaps |
| P01 | Steelhead and place searches | Queries by jurisdiction and basin |
| P02 | Legal registry and filing searches | Jurisdiction-specific identity checks |
| P03 | Broader conservation searches | Watersheds, fisheries, habitat and policy |
| P04 | Partner and funding network expansion | New candidates from observed edges |
| P05 | Structure and chapter searches | Sponsors, parents, affiliates and programs |
| P06 | Gap audit and saturation challenge | Missing geography, stages, risks and NGO types |

### Candidate seed list

Initialize from the versioned [candidate seed list](../input-data/seed-candidate-list.md); apply the same screening to seeds and new discoveries.

**DIS-06 |** P0 | Start research from an identified, tracked seed-list commit/path carried into cycle/release metadata. Preserve imported names and resolved IDs. No per-name seed-hash table is required.

**DIS-07 |** P0 | Seed membership MUST NOT establish identity, NGO eligibility, steelhead relevance or inclusion. Apply the same evidence/screening rules to all candidates and retain prior decisions.

**DIS-08 |** P0 | Add discovered names after duplicate/alias checks without waiting for relevance acceptance. Retain discovery provenance, batch versioned updates, explain consequential corrections/merges/removals and identify any resulting seed revision. Later lists MUST NOT change earlier releases.

### Discovery requirements

**DIS-01 |** P0 | Log each search/coherent batch: ID/pass, date, researcher/service, query/filter, geography, results reviewed, new candidates and stopping reason. Retain failed/zero-yield searches and language/translation choices.

**DIS-02 |** P0 | Candidates MUST retain discovery run/source references, screening decision, relevance rationale and duplicate-resolution result. Rediscovery MUST reference the existing ID.

**DIS-03 |** P0 | Prioritize evidenced steelhead connections without narrowing Pacific Rim scope. Log searched areas, priorities, language needs and gaps. Unsearched areas MUST NOT imply no organizations; an exhaustive regional matrix is unnecessary.

**DIS-04 |** P0 | Partner expansion MUST record entities searched, candidates found and stopping reasons, reusing existing IDs. A search list and bounded effort suffice; no traversal service is required.

**DIS-05 |** P0 | Report search boundaries, effort, recent yield and gaps. Incomplete discovery MAY support a qualified release. Saturation claims MUST show diminishing returns within the searched scope, never Pacific Rim completeness.

Search completion follows assigned questions/coverage and the declared time budget, not query/document counts. Record stopping reasons and remaining gaps; [workflow §1](../workflow.md#1-assignment-and-completion-boundaries) defines effort and first-pass/iteration boundaries.

## 5 Evidence and organizational analysis

Evidence supports specific claims, not unrelated findings by association.

### Evidence standards

**EVD-01 |** P0 | Every material finding/value MUST cite retained source IDs and exact pages/sections. The source index records publisher/title, public URL, publication/access dates, period and retained location. Helpful extracts/summaries MAY accompany evidence; separate claim tables are unnecessary.

**EVD-02 |** P0 | Classify sources as official filing/registry, organizational report, partner/funder report, independent research, news or discovery lead. Snippets/generated summaries MUST NOT be sole support for approved material claims.

**EVD-03 |** P0 | Retain conflicting evidence, selected interpretation, reason/date and applicable independent review. Missing, not applicable, not disclosed and estimated MUST remain distinct from zero.

**EVD-04 |** P0 | Retain obtainable permitted originals unchanged or faithful web captures, separate from summaries. Substitute extracts require a specific retention/access/effort exception, included/omitted scope and original/derivative hash distinction. Retained evidence MUST resolve from the generating commit; external evidence needs a durable retained copy, location and manifest hash. A URL/hash alone is insufficient. Disclose evidence that cannot be preserved and limit reproducibility claims accordingly.

**EVD-05 |** P0 | Material interpretations—including inferred classifications, disputed identity and allocations—MUST state high/medium/low/unresolved confidence and rationale. Direct transcription needs evidence and a reported-value label, not extra confidence scoring. Machine proposals require GOV-03 review; agent review MUST NOT be called human verification.

**EVD-06 |** P0 | Approved claims MUST use public evidence. Personal communications MAY locate public sources but MUST NOT support findings. Prohibited individual donor/private personal content MUST NOT be imported.

### Financial and staffing requirements

Initial coverage seeks available revenue and staffing with periods/sources, plus documented activities. Missing disclosure is a documented gap, not automatic exclusion. Prefer official filings for financial values and primary program evidence for activities; label third-party estimates accurately. Evidence need not support every resource measure.

**FIN-01 |** P0 | Support US EIN/990 and Canadian charity/T3010 identifiers/disclosures, and applicable local identifiers/filings elsewhere. Retain original-language references, translated labels and disclosure availability. Verify legal status separately from filing availability; no filing MUST NOT imply no revenue/activity.

**FIN-02 |** P0 | Financial values MUST identify measure, amount/currency, fiscal period, reporting boundary and source/locator. Retain available fiscal start/end, filing year and amendment status; flag partial periods. Keep revenue, expenses, assets, grants and program spending distinct without requiring every metric.

**FIN-03 |** P0 | Retain native currency/periods. Conversion MUST record rate, source, date/averaging period, method and target currency. Unconverted currencies MUST NOT be summed.

**FIN-04 |** P0 | Record available staffing with measure, value/units, date/period, scope and source. Distinguish headcount, FTE, contractors, volunteers and board members where reported. Missing staffing MUST NOT become zero; every category is not required.

**FIN-05 |** P0 | Each observation MUST keep its own fiscal period/source date. Reports MUST explain selection, represented periods and stale/partial/mixed-period limits; prefer compatible-period comparisons. New disclosures/amendments MAY update selection while preserving earlier observations/releases. Release date MUST NOT replace fiscal year.

## 6 Steelhead effort and biological classification

### Attribution requirements

**ATT-01 |** P0 | Steelhead-share estimates are optional and require evidence. Each MUST retain low/high bounds, compatible denominator/period, scope, method, assumptions, sources, confidence, estimator and independent reviewer; 0 ≤ low ≤ high ≤ 1. Qualitative profiles without estimates are valid.

**ATT-02 |** P0 | Distinguish reported steelhead expenditure, allocated program expenditure, proxy allocation and qualitative evidence. General salmon work MUST NOT automatically receive a steelhead share.

**ATT-03 |** P0 | Monetary attribution MUST use a compatible expenditure denominator. Revenue × share MAY appear only as a separate capacity proxy, never attributable spending. Unsupported shares/denominators MUST produce no estimate.

**ATT-04 |** P0 | Staff time, money, projects, policy actions and outcomes MUST remain distinct measures; conversion requires an explicit reviewed method.

**ATT-05 |** P1 | Sensitivity views SHOULD expose low/high assumptions and alternative inclusion choices. Midpoints MUST NOT become observed values, nor summed ranges probabilistic confidence intervals.

An activity is a coherent program/body of work, not every event. Split when geography, classification, period or financial treatment meaningfully differs. Shared activities retain one ID and participants (CNT-04).

### Life stages and risks

**BIO-01 |** P0 | Use Section 02, Steelhead Life Cycle ([source](../../../sections/02_life_cycle.tex), [table](../../../tables/life_stage_crosswalk.tex)), for life-stage labels: **Egg / Alevin / Fry; Parr; Smolt; Early Marine Juvenile; Ocean-rearing Steelhead; Returning Adult; Spawner; Post-spawning Freshwater Holding and Downstream Migration; Post-spawning Ocean Recovery; Returning Repeat Spawner.** Support freshwater/estuary/marine environments, transitions and unknown/cross-stage work. These are analytical groupings, not a compulsory sequence. Record codebook source revision and crosswalk changes.

**BIO-02 |** P0 | Risk definitions MUST come from Section 03, Biological Risk Across the Life Cycle ([source](../../../sections/03_biological_risk.tex)). **Section 03 is incomplete; its completion and risk-codebook approval are prerequisites for the full census.** Before use, each code MUST define inclusion/exclusion, examples and evidence needs. Record source revision and crosswalk changes.

**BIO-03 |** P0 | Activity coding MUST record geography/population, stage, environment, approved risk or pending state, intervention, period, direct/indirect pathway and evidence. Interpretive coding needs EVD-05 confidence/rationale.

**BIO-04 |** P0 | Multi-label coverage MUST NOT imply additive spending. Resource partitions MUST define exclusivity/overlap treatment and reconcile to at most 100% of the denominator.

**BIO-05 |** P1 | Risk–effort comparisons SHOULD separately evidence biological importance, controllability and uncertainty. Disclose incompatible scales; few organizational mentions MUST NOT alone imply neglected risk.

## 7 Partner networks and reporting

A claimed association/logo alone does not establish funding, control or a current partnership.

### Network requirements

**NET-01 |** P0 | Record necessary governance, sponsorship, funding, collaboration and discovery connections with endpoints, type, evidence, status and known dates. Symmetric collaboration MUST have one canonical record; only ambiguous/inferred links need confidence. Exhaustive networks are unnecessary.

**NET-02 |** P0 | Distinguish grants, sponsorship, parentage/governance, coalition membership, implementation, research collaboration and advocacy alignment. Unsupported types MUST remain unresolved.

**NET-03 |** P0 | Funding links MUST identify donor/recipient, purpose, period, available amount/currency, evidence and known financial overlap. Unknown amounts remain null; a complete flow account is not required for inclusion.

**NET-04 |** P1 | Network views SHOULD filter by period, geography, type, confidence and cohort, exposing missing/incomplete coverage.

### Reporting requirements

**REP-01 |** P0 | Support filtering/export by available period, geography, structure, stages, risk and candidate status. Scripted analysis/readable tables suffice; public lookup/map interaction follows REP-11–12.

**REP-02 |** P0 | Aggregates MUST declare counting unit, population boundary, cutoff, currency/financial-period treatment, unknowns/exclusions, method version and double-counting adjustments.

**REP-03 |** P0 | Reports MUST separate legal entities, operating nodes, capacity, supported attributed expenditure and qualitative coverage. Financial/allocation summaries require evidence, reproducible exports and CNT-01–04 overlap controls; disclose unavailable measures.

**REP-04 |** P0 | Release comparisons MUST separate discovery, newer disclosures, corrections, method/scope changes and actual organizational change. Financial comparisons require compatible measures/periods, or explicit limits/omission. Better evidence coverage MUST NOT appear as organizational growth.

**REP-05 |** P2 | Users MAY compare network/effort distributions across stages/risks where denominator compatibility, uncertainty and coverage limits remain visible.

**REP-06 |** P0 | Reports MUST identify/link the exact starting seed path/commit, its candidate-only meaning, and any resulting revision/change summary. Preserve lists in Git and archived source state; manifest holds references once. Links MUST be immutable, not latest-branch pointers.

**REP-07 |** P0 | Reports MUST display repository URL and full generating commit with immutable link. Release generation requires clean committed records/methods/configuration/narrative/geometry/seeds; relevant uncommitted/untracked inputs block release. One manifest MUST bind label, publication/cutoff/windows, commit, seed revisions, retained external paths/hashes, reproduction command/environment/dependencies, review and output hashes. External evidence requires permitted retained copies. Non-release drafts MAY be uncommitted; output/manifest need not belong to the generating commit.

**REP-08 |** P0 | Each included entity MUST have saved, evidenced **geographic areas of focus**, with periods/cutoff and separate areas/features. Label restoration/research/advocacy/other focus; do not imply uniform coverage, ownership, direct implementation or biological effect. Headquarters, partner locations, broad mission or policy jurisdiction alone MUST NOT define extent. Approximate regional circles/ovals are permitted.

**REP-09 |** P0 | Footprints MUST be GeoJSON FeatureCollections with WGS 84 Polygon/MultiPolygon features and closed rings. Include stable feature/entity IDs, activity/source references and locators, focus type, period, approximation and uncertainty. Unsupported areas use null geometry/reasons; identify unmapped coverage. Reports MUST link/explain saved files. Reproduction reads committed geometry without live geocoding or reenacting manual drawing; shared provenance belongs in the manifest.

**REP-10 |** P0 | Reports MUST show label, publication date, cutoff/windows, candidate-status coverage, financial availability versus unresearched/unavailable data and represented fiscal periods. Carried-forward observations keep original dates/limits. Multiple releases per year are permitted; publication MUST NOT imply complete discovery, current data for all entities or common-year observations.

**REP-11 |** P0 | Provide permanent static HTML release reports and a stable latest/archive landing page. Support organization name/ID lookup, readable findings, evidence/commit links and downloads. Bundles MUST be self-contained without a backend/database and preserve earlier release addresses/content.

**REP-12 |** P0 | A browser viewer MUST discover every released footprint through an index; support pan/zoom, name/ID lookup, individual/all layer controls and extent fitting; and expose identity, focus limits, evidence/report links and raw files. Overlapping and null-geometry entities MUST remain findable with reasons. Archive viewer/assets/index/data; footprints/list/provenance MUST work without basemap tiles or live geocoding.

**REP-13 |** P0 | Publication MUST be an explicit action selecting reviewed commit, unique label and cutoff/windows, with successful validation and owner authorization. Research, commits, pushes and previews MUST NOT publish or alter latest pointers. Failures preserve prior release; labels/content MUST NOT be overwritten. Preview output is non-release.

Institutional partners remain reference-only, without profiles/budgets in NGO totals. Unknown/stale evidence MUST remain visible: blank marine coverage does not prove no work, small budgets do not prove low effectiveness, and large networks do not prove stronger outcomes.

## 8 Data schema and validation

Use the seven [organization deliverables](../methods/staging-record-format.md#organization-deliverables), shared entity/source/discovery/decision records and permitted evidence. Their exact fields, paths and canonical authority are defined once in the format reference. First-pass/iteration coverage follows [workflow §1](../workflow.md#1-assignment-and-completion-boundaries).

Reviewed findings MUST remain reusable with durable source/review references. Reopen only for changed sources, errors/conflicts or relevant method/identity changes; retain superseded history. Ignored staging MUST stay outside accepted report inputs and Git. Before authorized disposal, deliberately retain accepted evidence/findings, necessary reviews/decisions, useful deferrals and significant rejections outside staging. Workflow governs closure; all generated output stays under `analysis/ngo-census/output/`.

### Schema requirements

**DAT-01 |** P0 | Validate stable ID uniqueness, record references, required applicable fields, controlled terms, financial units/periods, attribution bounds and GeoJSON. No database/foreign-key engine is required.

**DAT-02 |** P0 | Distinguish missing material values from zero with reasons. Preserve imported names and source-row references.

**DAT-03 |** P0 | Every material reported finding MUST resolve to retained sources/locators. Generating commit and manifest identify record versions, external inputs and outputs; no per-field version database is required.

**DAT-04 |** P1 | Imports SHOULD avoid duplicate records and report unmatched/conflicting rows. Stage scoped changes for review; Git MAY support correction/rollback.

## 9 Nonfunctional requirements

**NFR-01 |** P0 | A documented command with recorded environment/dependencies MUST reproduce the same findings, classifications, counts, calculations, maps and narrative from the clean generating commit, retained evidence, reviewed records/text, saved geometry and manifest. No new web retrieval/geocoding, extraction or AI calls. Save, source-link, independently review and authorize substantive AI prose before committing; deterministic formatting MAY reuse it. Only documented non-analytical differences are permitted. Later research/method/seed/model changes MUST NOT alter previous releases.

**NFR-02 |** P0 | Authoritative research MUST use editable open text with stable IDs, units, missing-value reasons and sources. Reports need readable summaries and machine-readable exports; workbooks MAY be derived conveniences, not duplicate authorities.

**NFR-03 |** P0 | Use repository permissions and Git review/history for controlled changes and release review. A custom approval system is unnecessary; add hosted access controls only when needed.

**NFR-04 |** P0 | Back up permitted evidence and archive each released source state/output bundle. Before first release, verify reproduction from a clean checkout/archive plus retained external inputs. Hosted daily-backup/recovery targets apply only if a later service needs them.

**NFR-05 |** P0 | Use public organizational data and respect access/reuse conditions. Exclude private/non-public content, individual donor records and credentials from captures/exports. Personal communications MAY locate public evidence but MUST NOT support findings.

**NFR-06 |** P2 | The prototype SHOULD run on its declared environment without unnecessary manual steps. Set measured performance/capacity targets only when scale or hosting warrants them.

**NFR-07 |** P0 | Research/reports MUST use clear fields, readable tables, understandable validation and explanations of graphics/maps. Interactive interfaces require keyboard access and appropriate contrast.

**NFR-08 |** P1 | Automated research extraction SHOULD log failures and retry without duplication. Outputs remain proposals until GOV-03 review/integration; changed extractions are new proposals. Reproduction MUST reuse saved reviewed findings rather than rerun extraction/classification.

## 10 Validation and acceptance

Use labeled examples addressing identity, missing evidence, currencies, overlap, shared work, seeds and geography. Record expected/actual results; add jurisdiction/translation cases when introduced. Examples may cover several checks without an exhaustive regional matrix.

| Test ID | Requirements | Passing result |
| --- | --- | --- |
| AC-01 | ENT-01–05, DAT-01 | Duplicates resolve once; similar names remain pending; merges are reversible without losing IDs/history. |
| AC-02 | CNT-01–04 | USD 1m parent including USD 200k child totals USD 1m; coalition membership creates no budget. |
| AC-03 | CNT-03, NET-03 | Supported transfers/overlap removed once in reconciled totals; otherwise separate values and non-additivity warning. |
| AC-04 | FIN-01–05 | Values retain period/date, currency, scope and source; no unconverted sums or missing-to-zero staffing; mixed periods disclosed. |
| AC-05 | ATT-01–04 | Supported 10–20% of compatible USD 1m expense yields USD 100k–200k; revenue proxy separate; unsupported estimate omitted. |
| AC-06 | BIO-01–04 | Multiple labels do not multiply spending; supported partitions ≤100%; shared work uses one activity ID. |
| AC-07 | EVD-01–05, DAT-03 | Material findings resolve to retained sources/locators, with interpretation confidence and conflicts. |
| AC-08 | DIS-01–05 | Logged effort/yield supports stopping reason; gaps disclosed; no query/document-count completeness claim or cap. |
| AC-09 | NET-01–03 | Typed evidence distinguishes funding from membership; repeated discovery reuses existing candidates. |
| AC-10 | REP-01–04, NFR-01–02 | Offline clean reproduction regenerates records, calculations, geometry and saved narrative without web/AI; exports agree. Only documented non-analytical differences allowed. |
| AC-11 | GOV-02–03, NFR-03–04 | Verify stopped/addressed serial handoffs, fresh reviewers, bounded corrections, exact current hashes and dependencies. Owner exceptions override standing defaults without bypassing review; response recording preserves digest. Durable review/runtime provenance and necessary history survive authorized cleanup; staging is never committed; action permissions are explicit. The preview matches authoritative records and exposes stale review. |
| AC-12 | DAT-02–04, REP-04 | Import retains original names/rows, avoids duplicates, and preserves identity through renames/corrections. |
| AC-13 | ENT-05, EVD-06, NFR-05 | Institutional profiles stay outside NGO totals; public partner references allowed; personal communications alone cannot support findings. |
| AC-14 | DIS-06–08, GOV-02, NFR-01 | Seeds do not auto-include; new names retain discovery provenance/version; prior reproduction unchanged. |
| AC-15 | REP-06 | Report resolves starting/resulting seed revisions, candidate-only meaning and changes in archived source state. |
| AC-16 | REP-07, NFR-01 | Report shows clean generating commit/immutable link; relevant uncommitted inputs block release; manifest resolves external inputs, command/environment and output hashes. |
| AC-17 | REP-08–09, BIO-03, NFR-01 | Lower Deschutes example uses a supported regional focus polygon, not headquarters/whole basin. Disjoint/null areas and focus types stay visible; saved geometry reproduces without drawing/geocoding. |
| AC-18 | REP-04, REP-10, FIN-05 | Two same-year releases have distinct labels/cutoffs/commits; show candidate coverage, unavailable versus unresearched finances and actual fiscal periods. Carry-forward/discovery/correction is not automatically organizational change. |
| AC-19 | REP-11–12, REP-08–10 | Permanent report/map and archive links work; name/ID lookup/downloads and every indexed footprint—including overlaps/nulls—are inspectable. Layer/extent controls, provenance and tile-independent viewing work; earlier bundles remain unchanged. |
| AC-20 | REP-13, GOV-03, REP-07 | Research/push/preview does not publish. Explicit commit/label/cutoff publication requires passed checks/review/owner permission; labels immutable; failure preserves earlier release; latest updates only after success. |

### Release gate

All applicable P0 checks MUST pass. Included entities need supported identity/relevance, source references and saved footprints (null with reason allowed). Reported values/estimates need required evidence, scope and review. A clean generating commit, independent release review, explicit owner publication authorization and reproducibility are mandatory. Unresolved identity/overlap blocks only affected inclusions/aggregates; disclosed incomplete discovery or mixed financial years do not alone block a release.

## 11 Decisions requiring confirmation

### Decisions for owner review

| **ID** | **Decision** | **Proposed default and consequence** |
| --- | --- | --- |
| OD-01 | Historical pass mapping | Reconcile P00–P06 with workbook before migrating search history |
| OD-02 | Search stopping rule | Use assigned questions/coverage and owner-adjustable time budgets; report search/document counts and gaps without count caps; refine defaults from measured pilot effort |
| OD-03 | Relevance and geographic coverage | Require an evidenced pathway to wild steelhead; agree evidence-based Pacific Rim search priorities and disclose unsearched areas; retain unsupported leads as deferred |
| OD-04 | Financial observation selection | Select the latest usable evidence available by the cutoff, retain each observation’s fiscal period and source date, and compare compatible-period subsets; disclose missingness and mixed periods |
| OD-05 | Attribution denominator | Prefer compatible program expense; allow separately labeled revenue capacity proxies |
| OD-06 | Effort allocation | Retain overlapping activity coverage; permit additive resource partitions only with supported allocations |
| OD-07 | Taxonomy authority and incomplete risk section | Complete Section 03 of the discussion document and approve its resulting risk codebook before running the full census; approve the life-stage codebook drawn from Section 02 jointly with manuscript reviewers before production coding |
| OD-08 | File formats and repository layout | Use a few structured text files with direct source references; introduce a database or hosted interface only for demonstrated needs |
| OD-09 | Release timing and archiving | Issue dated snapshots when useful, including multiple releases per year; optional annual planning review carries no publication obligation; agree durable archives and evidence backup locations |
| OD-10 | Publication and source retention | Confirm public-source eligibility, licensing, permitted source copies, and exclusion of prohibited personal data |
| OD-11 | Prototype hosting and address | Provisionally use GitHub Pages for the report/map and GitHub Releases for download archives. Confirm configuration and actual public address in development notes; preserve earlier release addresses on deployment. Revisit the hosting choice after prototyping if needed |

Implementation phases and deployment options are recorded in [development notes](../development-notes.md#implementation-phases). Approval of this specification does not assert that those capabilities exist. Section 03 remains the full-census gate in BIO-02.

## Owner decision capability

**OWN-01 |** P0 | Shared review HTML MUST support accept/reject/defer/request-changes and comments, exporting decisions bound to assignment, exact proposals, evidence/review revision and selected digest. Unselected entries imply no override. Validate supplied decisions before editing their context; preserve owner responses and original reviews. Stale exports MUST NOT authorize revisions or erase unresolved restrictions. Choices MUST NOT bypass review or authorize Git/publication actions.

See [workflow owner policy](../workflow.md#5-owner-review-by-exception) for operations and [development notes](../development-notes.md) for current limitations.
