# Wild Steelhead Organization Census Requirements

Version 0.12 | Review draft | 11 November 2026

## 1 Purpose and review decision

This document specifies a repeatable system to identify, analyze, and track NGO-like organizations whose activities affect wild steelhead conservation across the entire Pacific Rim. It supports review of conservation effort across geography, life stages, and biological risks, and supplies a traceable institutional evidence base for the steelhead discussion paper.

**Reviewers should approve the scope, entity distinctions, evidence rules, and release criteria, then resolve the decisions in Section 11 before a production baseline is issued. Requirements describe desired system behavior; they do not assert that the census is complete or that an organization's budget measures its conservation effectiveness.**

### Repeatable research and reproducible releases

Research follows a documented, repeatable procedure but may yield different discoveries. Web results, source availability, agent search choices, extraction proposals, and interpretations can change between runs. Search logs and retained evidence make the research traceable and reviewable; they do not promise identical discoveries or AI responses.

Each published release MUST instead be reproducible from retained evidence, reviewed research records and narrative, saved geographic data, and identified analysis code/configuration. The boundary is **agent research → retained evidence and reviewed findings → reproducible report generation**. Reproduction MUST NOT require repeating web searches, re-extracting documents with an AI model, reproducing review judgments, or obtaining identical AI responses. A fresh research run is new research, not reproduction of an old release.

### Goals

- Discover relevant organizations systematically.

- For each organization, document legal identity, operating units, financial reporting boundaries, and relationships.

- For each organization, describe attributable steelhead effort with explicit uncertainty and evidence.

- For each organization, compare documented effort with life stages and risk categories.

- For each organization, reproduce dated evidence snapshots and document changes in methods, identity, and activity.

### Scope

Include independent nonprofits, charities, and comparable nongovernmental bodies across Pacific Rim jurisdictions, including US nonprofits and Canadian registered charities, as well as fiscally sponsored projects, initiatives, coalitions, chapters, and parent organizations. An entity may qualify through direct steelhead work or a documented indirect pathway, such as watershed restoration, harvest policy, estuary protection, marine research, or hatchery reform affecting wild steelhead. Record supportive, adverse, mixed, or uncertain effects without inferring intent.

The geographic scope includes all countries and territories bordering the Pacific Ocean, their relevant inland watersheds, and shared offshore and international Pacific waters. Include organizations headquartered elsewhere when their work affects wild steelhead conservation within this scope. Geographic inclusion does not presume that steelhead occur in every jurisdiction; each included organization still requires an evidenced conservation pathway. Record headquarters separately from operating geography. Distinguish wild steelhead from resident rainbow trout, hatchery steelhead, and salmon generally; broader work requires a stated steelhead relevance rationale. Historical and inactive entities remain available for longitudinal analysis.

Government agencies, Indigenous governments, universities, public partnerships, and other similar institutions will be analyzed in a separate census and, thus, are excluded in this census.

This census can only make use of publicly available data. Inclusion of individual donors, private personal data, and other non-public data sources is prohibited. Personal communications can be used to help identify missing public data sources, but cannot serve as the basis of evidence.

### Requirement conventions

MUST is mandatory for the applicable phase; SHOULD is expected unless a documented exception is approved; MAY is optional. P0 denotes baseline release blockers, P1 denotes the next operational phase, and P2 denotes later analytical capability. IDs remain stable across revisions. Proposed methods in this version require owner approval before being treated as established census practice.

## 2 Governance and operating model

The census owner maintains scope, methods, and release decisions. Researchers maintain the evidence and structured records in the public Git repository. An independent reviewer, either a separate agent or a human, checks proposed findings and release readiness. The same actor must not author and independently accept the same finding. Researcher and steward functions may otherwise be combined; no separate human data steward or application approval system is required. Record reviewer identity and whether review was agent or human. The owner separately approves retained-data integration and authorizes publication; agent review is not human verification.

Each release is a dated snapshot of what is known at a declared evidence cutoff, not a complete account of one calendar or fiscal year. Releases occur when useful, including multiple times in a year; no fixed annual publication or completeness requirement applies. Give each release a unique readable label such as `2026-11-11-r1`, its publication date, and its generating Git commit. The evidence cutoff is the date research closed, distinct from publication date and the periods covered by individual observations. Declare any activity window or comparison period separately, alongside search priorities. Git is the authoritative revision history for maintained records, methods, code, configuration, seed lists, and manually prepared geographic footprints. A clean generating commit and one release manifest identify the exact analysis state. Public commit links make changes inspectable; Git history records edits, while a short decision log explains consequential judgments.

### Agent execution configuration

Select role models and reasoning effort through version-controlled implementation configuration, documented in the [README](../README.md), rather than fixing a GPT release in these requirements. Each agent execution MUST record role/session identity, configuration revision, requested settings, actual model identifier/release and reasoning effort where exposed, and any changes/reasons with affected scope. Mark unexposed actual values unknown; do not infer them from intended settings. Preserve execution notes in handoff history and reviewer provenance in retained review references. Independent review MUST use a fresh reviewer session supplied with evidence and explicit proposals rather than the researcher's full conversation or private reasoning. Different model releases are not required for independent review and do not by themselves establish it. These records document research provenance; release reproduction MUST NOT require rerunning the original model.

### Core operating requirements

**GOV-01 |** P0 | The system MUST maintain the inclusion policy, codebook, named census owner, and a concise decision log in the public repository. Log substantive judgments such as exclusions, disputed classifications, identity merges, and attribution estimates, with supporting source references, date, and reason. Routine transcriptions and formatting changes need only Git history.

**GOV-02 |** P0 | Each candidate MUST have one status: pending, included, excluded, or deferred. Included means reviewed and supported within the declared scope; pending means not yet resolved, and deferred means intentionally postponed with a reason. Exclusions and deferrals MUST retain their reasons and discovery provenance. Workflow status applies to candidates, not every field or source.

**GOV-03 |** P0 | Proposed findings and release readiness MUST receive independent review by a separate agent or human, accurately identified. Material estimates and ambiguous identity decisions MUST be explicitly checked; routine observations MAY share one review record identifying the checked members and source scope, without per-cell approvals. Unchecked observations MUST NOT inherit acceptance unless an owner-approved sampling policy explicitly supports it. Retain accepted review metadata or a stable group-review reference with findings. Each release also requires passed applicable checks, stated limitations, and explicit owner publication authorization; owner integration authorization follows the README standing policy or explicit owner exceptions and is separate from publication.

**GOV-04 |** P1 | The owner SHOULD refresh records when new disclosures, discoveries, corrections, or research priorities justify it, including organizations with missing filings or changed websites. An annual planning review MAY be useful but MUST NOT be a publication schedule or release gate.

### Analytical boundaries

Legal-entity counts answer how many independently constituted bodies are represented. Operating-node counts answer how many projects, chapters, initiatives, or coalitions are represented. Neither is a count of independent budgets. Reports must name their counting unit and date. Financial capacity, program expenditure, attributed steelhead resources, documented activity, and biological outcomes are separate measures.

An organization can address several life stages and risks. Multi-label coverage indicates documented activity, not an additive division of resources. A budget allocation is permitted only when its denominator and mutually exclusive allocation rule are recorded. Network centrality describes observed relationships within the census boundary; it is not evidence of conservation impact.

### Review and change control

Git commits and diffs preserve who changed maintained files, when, and what changed. Substantive judgments also reference the decision log. Do not duplicate Git history in an application audit database or maintain separate versions of every field. Corrections are new commits; prior release commits remain available. Record unresolved disagreements and their disposition in the decision log.

## 3 Entity model and counting rules

A stable entity ID identifies a real organization or operating node across names and years. A legal body and its programs are separate entities linked by dated relationships. Identifiers such as EIN or Canadian registration number are typed identifiers of legal entities, not universal IDs for every project.

| **Object** | **Meaning** | **Counting treatment** |
| --- | --- | --- |
| Legal organization | Independently constituted body with verified legal form | Count once in legal cohort |
| Sponsored project | Program operating through a fiscal sponsor | Operating node unless separate legal status is evidenced |
| Initiative or coalition | Coordinated work or membership arrangement | Node; no assumed independent revenue |
| Chapter or affiliate | Local unit with documented governance | Legal or operating count according to evidence |
| Parent organization | Controller, host, or umbrella body | Count legal identity once; link children |
| Excluded institution reference | Non-NGO partner or funder recorded only to explain an NGO relationship | Exclude from entity counts and financial totals; link to separate census where available |

### Identity requirements

**ENT-01 |** P0 | The system MUST store canonical name, aliases, entity type, legal status, country, identifiers, website, relevance rationale, operating status, and evidence. Unknown status MUST remain explicit.

**ENT-02 |** P0 | Duplicate detection MUST consider identifiers, aliases, domains, addresses, and relationships. Shared names or websites alone MUST NOT trigger an automatic merge.

**ENT-03 |** P0 | Parent, chapter, fiscal sponsor, program, affiliate, predecessor, successor, and merger relationships MUST include source references and effective dates where known. Unknown dates MUST remain explicit. Confidence and a rationale are needed for inferred or ambiguous relationships, not routine verified facts.

**ENT-04 |** P0 | Identity merges and splits MUST preserve prior IDs and aliases and be explained in the decision log. Git MUST retain earlier states so mistaken changes can be reversed and historical releases remain unchanged.

**ENT-05 |** P0 | Entity records MUST distinguish NGO-like candidates from excluded institutional references, separately from legal status. Use the four candidate statuses in GOV-02 for screening; do not introduce a second parallel approval workflow. Excluded institutional references MUST remain outside census counts and budgets.

### Double counting controls

**CNT-01 |** P0 | A financial observation MUST identify the reporting body, period, consolidation boundary, metric, and source. Child programs MUST NOT inherit parent revenue as their own revenue.

**CNT-02 |** P0 | Reports MUST prevent summing a consolidated parent amount with included child amounts. Unknown consolidation boundaries MUST be flagged and excluded from consolidated totals until resolved.

**CNT-03 |** P0 | Known funding transfers and possible financial overlaps MUST be recorded with supporting evidence. Report organization-level values when available; publish combined or net totals only for groups whose reporting boundaries and relevant transfers can be reconciled. Otherwise state that the values cannot be reliably added. Comprehensive reconstruction of interorganizational funding flows MAY be added in a later analytical phase.

**CNT-04 |** P0 | Coalition membership and shared partnerships MUST NOT create additional attributable spending. Joint activities MUST use one activity ID with participating entities and any evidenced allocation.

## 4 Discovery and saturation

Discovery uses P00 through P06 as a repeatable pass framework. The following mapping is proposed for approval and reconciliation with the historical workbook. Preserve any historical labels, queries, and results on import; do not relabel earlier work as if it used this mapping.

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

The system analysis starts from the organization names in [seed-candidate-list.md](../input-data/seed-candidate-list.md), located at `analysis/ngo-census/input-data/seed-candidate-list.md` relative to the repository root. This file is a candidate discovery input, not a roster of organizations verified to do steelhead-relevant work. Every listed candidate requires the same identity resolution, relevance screening, evidence, and review as a newly discovered candidate.

**DIS-06 |** P0 | Each research cycle MUST start from an identified Git revision of the seed list. The list MUST be tracked in the public repository. Record the starting commit and path once in the cycle metadata carried into the release manifest; candidate records MUST retain the imported name and link to the matching entity ID when resolved. A separate seed-input table or hash for each name is not required.

**DIS-07 |** P0 | Seed-list membership MUST NOT establish steelhead relevance, NGO eligibility, legal identity, or census inclusion. Apply the same scope and public-evidence rules to every candidate. Retain pending, excluded, and deferred decisions in the entity records; new seed membership does not override a reviewed decision.

**DIS-08 |** P0 | Add newly discovered organization names to the seed list after duplicate and alias checks, without waiting for relevance approval. Candidate records MUST cite their discovery log entry or source. Batch list updates into understandable Git commits; use the decision log for substantive corrections, consolidations, or removals. Record the resulting seed revision in the release manifest if it changed. Git history and candidate records replace a separate seed-change ledger, and later updates MUST NOT change earlier releases.

### Discovery requirements

**DIS-01 |** P0 | The discovery log MUST record pass, date, researcher, source or search service, query or filter, geographic focus, results reviewed, new candidates, and stopping reason. Record language or translation choices where relevant, and retain failed and zero-yield searches. One concise row per search or coherent search batch is sufficient.

**DIS-02 |** P0 | Candidates MUST retain discovery run IDs, source URLs, screening decision, relevance reason, and duplicate-resolution result. A rediscovered entity MUST link to its existing ID.

**DIS-03 |** P0 | Discovery MUST retain the entire Pacific Rim scope while prioritizing places, organizations, and networks with documented pathways to wild steelhead conservation. A concise coverage log MUST record areas searched, rationale for priorities, language needs, and unsearched areas or other gaps. An exhaustive country-by-stage-by-organization-type matrix is not required. Prioritization MUST NOT silently redefine the scope or turn unsearched areas into evidence of no relevant organizations.

**DIS-04 |** P0 | Partner expansion MUST record the organizations searched and candidates found, reuse existing IDs, and state why a search batch stopped. A list of already searched entities and a declared effort limit are sufficient; a graph traversal service is not required.

**DIS-05 |** P0 | Reports MUST state the search boundary, effort, recent discovery yield, and remaining gaps. A release MAY be issued with incomplete discovery if those limits are explicit. Saturation claims require documented diminishing returns within the searched scope and MUST NOT imply a complete Pacific Rim population census.

### Search stopping rule

Stop a research cycle when the planned priority searches and targeted gap checks are complete, or its declared effort limit is reached. Record the reason and the yield of recent search batches. Newly identified public sources or candidates may initiate additional logged searches. The owner reviews whether further searching is warranted and documents the remaining gaps.

The earlier proposal of two batches of at least 25 results per jurisdiction MAY be tested in the pilot where appropriate. It is optional, not a universal release gate or statistical confidence bound. Preserve the P00–P06 labels for organizing search work without requiring identical effort in every jurisdiction.

## 5 Evidence and organizational analysis

Evidence supports individual claims rather than an entire row by association. A legal filing can support identity and revenue while a program report supports work in an estuary. Neither automatically establishes the other's claims.

### Evidence standards

**EVD-01 |** P0 | Each material finding or reported value MUST carry source IDs and page or section locators directly in its entity, activity, or relationship record. The source index records publisher, title, public URL, publication date if known, access date, period covered, and retained evidence location. Include a short extract or summary where it helps establish relevance or interpret a value. Separate Claim and ClaimSource tables are not required.

**EVD-02 |** P0 | Sources MUST be classified as official filing or registry, organizational report, partner or funder report, independent research, news, or discovery lead. Search snippets and generated summaries MUST NOT be sole evidence for approved material claims.

**EVD-03 |** P0 | Conflicting sources MUST be retained with the selected interpretation, reason, and date; record a reviewer for material interpretations under GOV-03. Missing, not applicable, not disclosed, and estimated MUST be distinguishable from zero.

**EVD-04 |** P0 | The source index MUST identify retained public evidence needed to reproduce reported findings. Store permitted copies or extracts in the repository, with paths resolved by the generating commit. For evidence retained outside Git, the release manifest MUST record a content hash and durable retrieval location. A URL or hash alone does not preserve source content. Respect reuse restrictions; if necessary evidence cannot be retained in a permitted reproducible form, disclose the limitation and do not claim full reproducibility for the affected finding.

**EVD-05 |** P0 | Inferred classifications, disputed identities, share estimates, and other material interpretations MUST use high, medium, low, or unresolved confidence with a short rationale. Routine transcription from a directly applicable source needs a citation and a reported-value label, not an additional confidence assessment. Automated suggestions require human review before inclusion.

**EVD-06 |** P0 | Approved claims MUST be supported by publicly available sources. Personal communications MUST be treated only as discovery leads; approval requires locating and citing the underlying public source. Sources containing prohibited individual donor or private personal data MUST NOT be imported into the census.

### Financial and staffing requirements

The initial profile records reported revenue, its fiscal period and currency, staffing where publicly available, and documented steelhead activities. Research additional expense measures or steelhead-share estimates only where evidence supports them. Missing disclosures MUST be recorded as unknown with a brief reason; they do not prevent an otherwise supported organization from receiving an included profile. The system need not exhaust every possible source to estimate unavailable spending.

**FIN-01 |** P0 | US records MUST support EIN and IRS Form 990 family filing references; Canadian records MUST support charity registration identifiers and CRA T3010 references. Other jurisdictions MUST support applicable local legal identifiers, registries, financial disclosures, and original-language source references, with translated labels and an explicit record of disclosure availability. Legal status and filing availability MUST be verified separately; no filing MUST NOT imply no activity or no revenue.

**FIN-02 |** P0 | Every financial value used MUST record its metric, amount, currency, fiscal period, source and locator, and reporting boundary. Retain fiscal start/end dates, filing year, and amendment status when available; flag incomplete periods. Revenue, expenses, assets, grants, and program spending MUST remain distinct, but profiles are not required to collect all metrics.

**FIN-03 |** P0 | Reports MUST retain native currency and financial periods. Currency conversion MUST record rate, rate source, rate date or averaging period, method, and target currency. Unconverted amounts in different currencies MUST NOT be summed.

**FIN-04 |** P0 | Record staffing when publicly available, with observation date, scope, source, and units. Distinguish headcount, full-time equivalents, contractors, volunteers, and board members when those measures are reported; do not require every category for every entity. Missing staffing data MUST NOT become zero.

**FIN-05 |** P0 | Each financial observation MUST retain its own fiscal period and source date; a release date MUST NOT be substituted for its financial year. Reports MUST state how observations were selected, show the financial years or periods represented, and flag stale, partial-period, or mismatched data. Prefer compatible-period subsets for comparisons; any mixed-period summary MUST disclose its composition and limitations rather than imply a common-year total. New filings and amendments may update the selected observation in a later commit while preserving prior values and releases.

Prefer the relevant official filing for reported financial values and primary program records for activity claims. Organizations outside filing systems remain eligible when relevance and identity can be supported. Third-party estimates must retain their origin and must never be presented as filed values.

## 6 Steelhead effort and biological classification

### Attribution requirements

**ATT-01 |** P0 | A steelhead-share estimate MAY be produced only when evidence supports it. Each estimate used MUST record low/high bounds, compatible denominator and period, scope, method, source references, assumptions, confidence, estimator, and independent reviewer. Bounds MUST satisfy 0 ≤ low ≤ high ≤ 1. A qualitative profile with no monetary estimate is valid when disclosure is insufficient.

**ATT-02 |** P0 | Estimates MUST distinguish directly reported steelhead expenditure, allocated program expenditure, proxy allocation, and qualitative evidence only. General salmon work MUST NOT automatically receive a steelhead allocation.

**ATT-03 |** P0 | A derived monetary range MUST use a compatible expenditure denominator. Revenue multiplied by share MAY be shown only as a labeled capacity proxy, never as attributable spending. Unknown denominator or unsupported share MUST produce no monetary estimate.

**ATT-04 |** P0 | Staff time, financial resources, projects, policy actions, and outcomes MUST be stored as different measures. The system MUST NOT convert one into another without an explicit, reviewed method.

**ATT-05 |** P1 | Sensitivity views SHOULD show results under low and high attribution assumptions and alternative inclusion choices. Midpoints MUST NOT be treated as observed values or sums of ranges as probabilistic confidence intervals.

For example, a hypothetical organization with USD 1 million in compatible program expenditure and a supported 10–20 percent share yields USD 100,000–200,000 in estimated attributed expenditure. If only revenue is known, the same calculation represents a revenue-based capacity proxy. It cannot be added to expenditure estimates in a single effort total. The example is a validation fixture, not census evidence.

### Activity granularity

An activity is a documented program or coherent body of work, not necessarily each individual event or project. Use one activity record when purpose, geography, life-stage/risk coding, period, and financial treatment can be described consistently. Split it only when those differences matter to the analysis. Record evidence-supported work without attempting an exhaustive inventory of every action. Shared activities use one ID with participating entities, preventing duplicated effort.

### Life stages and risks

**BIO-01 |** P0 | Activities MUST support freshwater, estuary, and marine environments, with migration and transition links. Life stages MUST be drawn from Section 02, Steelhead Life Cycle, of the discussion document ([section source](../../../sections/02_life_cycle.tex) and its [life-stage table](../../../tables/life_stage_crosswalk.tex)). Those stages are **Egg / Alevin / Fry; Parr; Smolt; Early Marine Juvenile; Ocean-rearing Steelhead; Returning Adult; Spawner; Post-spawning Freshwater Holding and Downstream Migration; Post-spawning Ocean Recovery; Returning Repeat Spawner.** Unknown and cross-stage work MUST be supported. These are the discussion document’s analytical stage groupings, not a mandatory sequence for every fish. The codebook MUST record the source revision and retain a crosswalk when stage definitions change.

**BIO-02 |** P0 | **Biological risk categories and definitions MUST be drawn from Section 03, Biological Risk Across the Life Cycle, of the discussion document ([section source](../../../sections/03_biological_risk.tex)). OPEN DEPENDENCY: Section 03 is incomplete. Its completion and approval of the resulting risk codebook are prerequisites for running the full census. Each risk code MUST define inclusion, exclusion, examples, and evidence needs before operational use. The codebook MUST record the source revision and retain a crosswalk when risk definitions change.**

**BIO-03 |** P0 | Activity coding MUST store affected geography or population, stage, environment, risk, intervention type, period, direct or indirect pathway, and source references. Add confidence and rationale for interpretive coding under EVD-05. Advocacy or research subject matter MUST NOT establish a demonstrated biological effect.

**BIO-04 |** P0 | Multi-label classifications MUST NOT imply additive spending shares. Allocations MUST specify exclusive partitions or a separate overlap treatment and reconcile to at most 100 percent of the defined denominator.

**BIO-05 |** P1 | Risk–effort comparisons SHOULD use a separate evidence base for biological importance, controllability, and uncertainty. Reports MUST disclose incompatible scales and MUST NOT infer neglected risk solely from few organizational mentions.

## 7 Partner networks and reporting

Relationships explain funding, governance, and collaboration. Their presence, direction, and meaning must be evidenced independently. A website logo may establish a claimed association but does not establish a funding amount, legal control, or current partnership.

### Network requirements

**NET-01 |** P0 | Record evidenced relationships needed to explain governance, sponsorship, funding, shared work, or discovery. Each relationship MUST identify endpoints, type, source references, status, and dates where known. Use one record for a symmetric collaboration. Record confidence only for interpretations or ambiguity; exhaustive partner enumeration is not a baseline requirement.

**NET-02 |** P0 | Edge types MUST distinguish grants, fiscal sponsorship, governance or parentage, coalition membership, joint implementation, research collaboration, and advocacy alignment. An unknown relationship type MUST remain unresolved.

**NET-03 |** P0 | For an evidenced funding relationship, record donor, recipient, purpose, period, amount and currency when available, and any known overlap with financial observations. Unknown amounts remain null. Do not require a complete flow account before including either organization.

**NET-04 |** P1 | Network views SHOULD allow filtering by date, geography, edge type, confidence, and cohort, and show missing or incomplete relationship coverage.

### Reporting requirements

**REP-01 |** P0 | The documented workflow MUST support filtering and exporting research records by available period, geography, entity structure, life stage, risk, and candidate status. Scripted filters and readable tables satisfy analytical filtering; public organization lookup and map interaction are provided by the static viewer under REP-11–12.

**REP-02 |** P0 | Each aggregate MUST disclose counting unit, population boundary, evidence cutoff, currency method, financial-year treatment, unknown coverage, exclusions, methodology version, and double-counting adjustments.

**REP-03 |** P0 | Reports MUST distinguish legal entities, operating nodes, reported financial capacity, supported attributed expenditure, and qualitative activity coverage. Include financial or allocation summaries only where data support them; state when a measure is unavailable. Any published totals MUST be reproducible from exported records and obey the overlap rules in CNT-01–04.

**REP-04 |** P0 | Comparisons between any releases MUST distinguish newly discovered organizations, newer filings, corrections, changed methods or scope, and evidenced changes in organizational identity or activity. A newer filing or improved coverage MUST NOT by itself be presented as growth in organizational resources or conservation effort. Financial change comparisons MUST identify the underlying observation periods and use compatible measures and periods where possible; otherwise explain why the comparison is limited or omit it.

**REP-05 |** P2 | Users MAY compare network structure and effort distribution across risks and stages, provided denominator compatibility, uncertainty, and unresolved coverage remain visible.

**REP-06 |** P0 | Each report MUST identify its starting seed-list path and commit, link to that exact revision or attach a readable copy, and explain that names are candidates rather than verified steelhead organizations. If discovery changed the list, identify its resulting revision and summarize additions or other material changes. The release manifest holds the seed references once; report links MUST use immutable commits, not the latest branch. Retain exact list contents through the referenced Git history and an archived repository snapshot.

**REP-07 |** P0 | Each published report MUST display the public repository URL and full generating Git commit hash with an immutable link. Generate releases only from a clean committed state containing the research records, methods, code, configuration, footprints, saved substantive narrative, and seed references used. Relevant uncommitted or untracked inputs MUST block release; ordinary draft runs may remain uncommitted and MUST be labeled non-release. One release manifest MUST identify the generating commit, release label, publication date, evidence cutoff, any declared activity window/comparison period, starting and resulting seed references, external input paths/hashes, reproduction command and environment/dependency versions, and output paths/hashes. Evidence and inputs stored outside Git MUST have permitted retained copies at recorded retrieval locations. The generating commit need not contain the report or completed output manifest; these may be archived afterward without changing the generating commit reference.

**REP-08 |** P0 | For each included entity in each reporting snapshot, the system MUST produce and retain a GeoJSON file that generally depicts the geographic extent of direct influence supported by that entity’s collective documented activities and actions within its declared activity window, or as evidenced by the cutoff if no fixed window is used. The footprint MUST be derived from activity locations and evidence, rather than headquarters, an organization’s name, broad mission statements, or partner geography alone. A circle or oval approximated as a polygon MAY represent a general activity region; separate areas MUST remain separate polygons or features when a single enclosing shape would misleadingly imply influence between them. For example, documented river restoration on the lower Deschutes may be represented by an approximate circle or oval spanning that region, without implying activity throughout the entire Deschutes basin. The shape depicts the approximate area of documented direct influence, not a precise project boundary, uniform activity coverage, measured biological effect, or demonstrated conservation outcome.

**REP-09 |** P0 | Retain each entity’s approximate footprint as a tracked GeoJSON FeatureCollection with valid Polygon or MultiPolygon geometry, using WGS 84 longitude/latitude coordinates and closed rings. Properties MUST identify entity, activity period or window (unknown where unsupported), supporting activity/source references, and an approximation note describing method and uncertainty. Unsupported locations use null geometry with a reason; partial mapping identifies unmapped activities. A researcher MAY draw or revise a circle or oval manually and commit the actual geometry; the report workflow MUST read the saved geometry rather than reconstructing drawing gestures. Shared cutoff, review, commit, and output hashes belong once in the release manifest. Reports MUST link to each file and explain its approximate meaning and coverage limits. Reproduction uses committed geometry without live geocoding services.

**REP-10 |** P0 | Each report MUST display its release label, publication date, evidence cutoff, and any declared activity window or comparison period. It MUST summarize candidate coverage by pending, included, excluded, and deferred status; distinguish available, not-yet-researched, and unavailable financial information; and show the distribution of financial years or periods represented. Multiple releases in one year are permitted. Publication MUST NOT imply that discovery is complete, every entity has current financial data, or all observations refer to the release year. Previously supported observations MAY be carried forward with their original period and source date and explicit coverage limits.

**REP-11 |** P0 | Each published release MUST provide a static HTML report at a permanent public release address, reachable from a stable census landing address that links to the latest release and earlier releases. The report MUST support finding an organization by name or ID, reading its documented findings and evidence/commit links, and downloading the structured outputs. Publish a self-contained static bundle without requiring an application server or database; retain previous release bundles unchanged. The [census README](../README.md) defines the local output and public-address conventions; record the actual public address when hosting is configured.

**REP-12 |** P0 | Each release MUST provide a browser map viewer for all included entity GeoJSON files, discovered through a release file index. Users MUST be able to pan/zoom, find organizations, show/hide individual or all footprints, zoom to selected extents, and inspect entity identity, approximation/coverage limits, supporting report/evidence links, and raw GeoJSON downloads. An organization list MUST expose overlapping footprints and entities with null geometry and their reasons. The viewer MUST use the frozen release files, retain their entity IDs, and remain capable of showing footprints and provenance without live geocoding or an available basemap service. Archive the viewer, its required assets, file index, and GeoJSON files with the report.

**REP-13 |** P0 | Routine research additions, commits, and pushes MUST NOT automatically create a report release, deploy census outputs, or change the public latest-release pointer. Release creation MUST require an explicit publication action selecting an exact committed analysis state, unique release label, and evidence cutoff, with any activity/comparison windows recorded. Preview generation MUST remain separate from publication and be labeled non-release. The release workflow MUST validate and generate from the selected commit and recorded parameters, verify required reviews, and publish only after successful checks. Failed checks MUST leave the current published report unchanged. Published release labels and contents MUST NOT be overwritten; corrections use a new label. The [census README](../README.md) specifies a manually triggered GitHub Actions workflow for the prototype.

### Interpretation rules

Non-NGO institutions are outside this census and belong in the separate institutional census. When a public source names an excluded institution as a partner or funder, retain only the reference needed to document the NGO relationship, with an exclusion flag and an optional link to the separate census. Do not create a full institutional profile or include institutional budgets in this census. Apply the same reference-only treatment to partners outside the target geography.

Reports must expose unknown values and stale evidence. A blank cell is not evidence that an organization does no marine work. A small attributed budget is not evidence of low effectiveness. A large partner network is not evidence of stronger biological outcomes.

## 8 Data schema and validation

The initial implementation uses readable structured research files in the public repository. The [census README](../README.md) documents directory layout, file roles, naming conventions, and reuse of reviewed research. File organization may evolve without changing the behavioral requirements below. Preserve stable entity, activity, and source IDs and store evidence references directly with findings. Separate claims, seed-event, audit-event, and snapshot-membership tables are not required.

| Record group | Minimum content |
| --- | --- |
| Entities and financial histories | Registry: ID, names/aliases, identifiers, entity type/legal status, candidate status and rationale, website, operating geography, source references. Per-organization history: available revenue, fiscal period/currency, staffing and supported additional measures or estimates, evidence locators and review references |
| Activities | ID, participating entity IDs and roles, program/work summary, period, geography, life stages, risks when approved, intervention/pathway, source references; optional supported allocations |
| Relationships | Endpoint IDs, type, status, dates and funding information where known, source references, confidence only where interpreted |
| Sources | ID, publisher, title, URL, dates, period, retained evidence path or retrieval location; locators can sit with the findings they support |
| Discovery log | Search/batch ID, pass, query/source, date, researcher, geographic focus, effort/yield, new candidates, stopping reason and gaps |
| Decision log | Consequential judgment, affected IDs, date, rationale, evidence, and second review where required |
| Seed list and footprints | Candidate names and permanent assigned IDs in the existing Markdown list; per-entity GeoJSON files with activity/source references and approximation notes |
| Release manifest | Release label, publication date, evidence cutoff, any activity window/comparison period, generating commit, seed references, external inputs, reproduction command/environment, output hashes, review and limitations |

### Repository organization and reuse

Follow the implementation conventions in the [census README](../README.md). It places the organization registry and source index alongside per-organization evidence, financial histories, activity notes, and footprints under `sources/`, while retaining the cumulative seed list under `input-data/`. This is the census-specific source-storage convention; generated release bundles remain under the repository-root `output/ngo-census/<release-label>/` directory and untracked; the README also defines their static HTML and map-viewer entry points.

Git history MUST preserve maintained records and corrections, while source references establish the evidence behind findings. Previously reviewed historical observations MUST be reused when the source and interpretation remain unchanged. Record the reviewer, date, source version, and scope of review with the observation or a referenced group review; source-origin checking alone does not verify extracted values. Re-review is required for changed sources, errors or conflicts, or method/identity changes affecting interpretation, not merely because a new release is being prepared. Retain superseded evidence and observations so prior releases remain reproducible. Use one source index and one manifest per release rather than duplicating shared provenance.

### Staged research integration

The researcher and reviewer MUST use a single-assignment staging area as documented in the [census README](../README.md). Only one assignment may be active there, and only one census agent may execute at any time across researcher, reviewer, and steward roles. A fresh researcher assignment requires a small assigned seed-ID set and empty staging; a correction pass instead requires an addressed return on the existing assignment. Reviewer and steward entry MUST require an explicit handoff addressed to that role, identifying sender, current role, proposal/review revision, and expected next action. Each agent MUST stop after handing off; the owner or coordinating session starts the next role only after the sender stops. While owner signoff is pending, dependent agent execution pauses. The researcher proposes additions or corrections; independent review records dispositions against the exact proposed revision; the steward integrates accepted material into retained files and validates shared references. Reporting MUST exclude provisional staging content. The steward MUST record closure and preserve its handoff, review, and disposition in an authorized Git commit, including explicit deferral of unresolved work, before an authorized cleanup commit removes all active staging files. Empty staging signals readiness for the next fresh assignment. The researcher MUST initiate one shared local HTML review page from authoritative staging records; the reviewer MUST refresh it with independent dispositions; the steward MUST complete and validate it before owner signoff. Use one shared renderer and page location under the README convention, labeled research proposal, reviewed proposal, or ready for owner signoff, with exact input/review revision or hashes. The page MUST provide an overall summary and inspectable file/entry-level changes, evidence links, reviewer dispositions from the review record, and the final proposal identity when ready for signoff. HTML is derived output, not the authoritative findings or approval record. Changed inputs MUST visibly invalidate affected stale acceptance rather than silently carry approval forward; an earlier-stage page does not establish signoff readiness. Before retained-data integration, the steward MUST record the eligible subset and proposal identity plus its approval basis: the standing owner-review-by-exception policy or explicit owner acceptance. No per-entry owner response or JSON file is required for an independently accepted, current, conflict-free subset. Owner exceptions override the default; unresolved issues and dependencies remain held. Substantive changes require renewed review/approval as applicable. Consequential unresolved judgments go to the owner before affected integration, and publication requires separate owner authorization. The [census README](../README.md) and [steward instructions](steward-agent-instructions.md) define the shared HTML lifecycle and final signoff mechanism.

Track the current role in the handoff so proposals are frozen during review and owner signoff; corrections explicitly return control to the researcher. Approval MUST bind to a deterministic inventory of the selected changes, reviewed dispositions, dependencies, and expected prior state, excluding approval/role/completion notes and the digest itself. Preserve that inventory and accepted review metadata beyond staging cleanup.

At effort limits, explicitly defer unresolved corrections with retrievable evidence rather than keeping the assignment open indefinitely. Owner signoff MAY authorize integration, a history-preservation commit, and later cleanup together when those actions are explicitly stated; it MUST NOT imply push or publication permission. No per-batch directory hierarchy or parallel authoritative data collection is required.

### Schema requirements

**DAT-01 |** P0 | Validation MUST check stable ID uniqueness, references between records, required fields applicable to available values, controlled terms, financial units/periods, attribution bounds when estimated, and GeoJSON validity. A database and foreign-key engine are not required.

**DAT-02 |** P0 | Missing material values MUST be distinguishable from zero with a brief reason, such as unknown, not disclosed, or not applicable. Preserve original imported names and source row references when importing historical data.

**DAT-03 |** P0 | Each reported material finding MUST resolve directly to its supporting sources and locators. The generating Git commit identifies the maintained record versions; the release manifest identifies external inputs and generated outputs. Do not maintain a second per-field version history or snapshot-membership database.

**DAT-04 |** P1 | Imports SHOULD avoid duplicate records on rerun and report unmatched or conflicting rows. Stage changes for Git diff review; correction or rollback MAY use Git rather than custom reversible-import machinery.

## 9 Workflows and nonfunctional requirements

### Research to release workflow

1. Plan the snapshot. Declare evidence cutoff, any activity window or comparison period, priority searches, available effort, and known gaps. Publication timing follows useful research progress rather than an annual schedule. Use the approved scope and codebooks; retain historical workbook provenance on initial import.
2. Seed and discover. Start from the recorded seed-list commit, screen candidates, and use P00–P06 to organize searches. Add new names after duplicate checks, link them to discovery evidence, and batch changes into Git commits. Record candidate status separately from seed membership.
3. Document each entity. Resolve identity and parent/program structure. Record available revenue, fiscal period/currency, staffing, and program-level activities with direct source references. Mark unavailable data without requiring unsupported estimates or exhaustive event inventories.
4. Classify and map. Apply Section 02 stages and, once approved, Section 03 risks. Save approximate per-entity GeoJSON geometry, including manually drawn shapes, in Git with activity/source references and limits. Preliminary discovery and profile preparation may proceed before Section 03 is complete, but the full census remains gated by BIO-02.
5. Review and commit. Review material estimates and ambiguous identity decisions with an independent reviewer (separate agent or human). Validate records, inspect diffs, document consequential decisions, and commit all inputs and methods used to generate the report. Release generation requires a clean state.
6. Preview and explicitly release. Prepare and review a non-release preview, then explicitly invoke publication for a selected commit, unique release label, and evidence cutoff under REP-13. Run the documented report command from the generating commit using retained evidence, reviewed records/narrative, and saved geometry, without new web research or AI calls. Generate the bundle under the README output convention and publish its static report and map viewer at the documented public addresses. The report identifies its release label, publication date, evidence cutoff, analysis commit and seed revision, links to entity GeoJSON files, and summarizes candidate coverage, financial availability, financial-period distribution, and comparison limits. Complete one manifest with inputs, environment, review, and output hashes; obtain independent release review and explicit owner publication authorization and archive the report, manifest, evidence as needed, and repository snapshot. Generated output stays out of the source tree’s tracked history.
7. Refresh. Update research files and seeds in later commits. Preserve previous release commits and archives. Issue another dated snapshot when useful, even within the same year. Explain changes in discovery, newer filings, corrections, methods, or actual organizational activity; do not silently rewrite earlier results.

### Nonfunctional requirements

**NFR-01 |** P0 | Each published release MUST be reproducible from its clean generating Git commit, retained external evidence/inputs, reviewed records and saved narrative, saved geometry, and one release manifest. A documented command and recorded dependency/environment versions MUST regenerate the same reported records, classifications, counts, calculations, maps, and substantive narrative without web searching, live source retrieval/geocoding, or new AI calls. Discovery, extraction proposals, agent/human interpretations, review decisions, and manual geometry are retained inputs, not processes to reenact. AI-written substantive narrative MUST be saved, source-linked, independently reviewed, owner-approved for integration, and committed before release generation; deterministic templates may format or summarize saved values without fresh interpretation. Formatting timestamps or other non-analytical metadata may differ if documented. Repeatability of the research procedure does not imply deterministic discoveries. Later research, seed changes, or model changes MUST NOT alter earlier release content.

**NFR-02 |** P0 | Authoritative research data MUST remain editable in open text formats, with stable IDs, units, missing-value reasons, and source references. Reports MUST include readable summaries and machine-readable exports. A workbook MAY be generated for convenience; it is not required as a second authoritative data store.

**NFR-03 |** P0 | The initial workflow MUST use repository permissions and Git review/history for controlled changes, corrections, and release review. A hosted application with multiple editing roles MAY introduce additional access controls when needed; a custom administrative permission system is not required for the repository implementation.

**NFR-04 |** P0 | Retain a backed-up copy of permitted source evidence and an archive of each released generating repository state and output package. Before the first release, verify that a clean checkout or archived snapshot plus retained external inputs can reproduce the analysis. Managed daily backups and recovery-time targets are required only if a later hosted service needs them.

**NFR-05 |** P0 | Collection MUST use publicly available organizational data and respect source access and reuse conditions. Individual donor records, private personal data, and non-public sources MUST NOT be included. Personal communications MAY identify public sources but MUST NOT support census claims. Source captures and exports MUST exclude prohibited personal data and credentials.

**NFR-06 |** P2 | The initial implementation SHOULD complete the pilot and report generation on the declared research environment without unnecessary manual steps. Establish measured capacity and response-time targets only if data volume or a hosted application creates an operational need; fixed large-scale benchmarks are not required.

**NFR-07 |** P0 | Research files and reports MUST use clear field definitions, readable tables, understandable validation messages, and text explanations of maps or graphics. Keyboard interaction, interface contrast, and other application-specific requirements apply only if an interactive interface is built.

**NFR-08 |** P1 | Automated extraction SHOULD log failures and support retry without duplicate records during research. Retain selected outputs as proposed research, subject to independent review and owner integration approval. Release reproduction MUST read the retained reviewed results, not rerun extraction or AI classification; changed extraction results are new proposals. Machine-proposed classifications remain unaccepted until the review/integration rules in GOV-03 are satisfied.

## 10 Validation and acceptance

Use a small set of clearly labeled examples that exercise actual analytical risks. Cover distinct identities and structures, missing evidence, multiple currencies, overlapping budgets, shared activities, seed changes, and approximate geography. One example may cover several checks. Include an additional jurisdiction or translated source when that capability is introduced; an exhaustive regional test matrix is not a pilot prerequisite. Record expected and actual results in a concise validation report.

| Test ID | Requirements | Passing result |
| --- | --- | --- |
| AC-01 | ENT-01–05, DAT-01 | Verified duplicate identifiers resolve once; similar names remain separate pending evidence; a mistaken merge can be corrected through Git and the decision log without losing old IDs |
| AC-02 | CNT-01–04 | A USD 1m parent amount including a USD 200k child reports USD 1m in a supported combined view; coalition membership creates no budget |
| AC-03 | CNT-03, NET-03 | An evidenced internal grant is flagged; a supported reconciled view removes overlap once, while insufficient evidence results in separate values and an explicit warning against adding them |
| AC-04 | FIN-01–05 | Available revenue retains its fiscal period, source date, currency, reporting boundary and source; different currencies are not added without conversion; missing staffing remains unknown; mixed-period summaries disclose their composition |
| AC-05 | ATT-01–04 | A supported 10–20% share of USD 1m compatible expense yields USD 100k–200k; revenue-based capacity is labeled separately; absent evidence produces a valid qualitative profile without an estimate |
| AC-06 | BIO-01–04 | A program can have several stage/risk labels without multiplying spending; supported additive allocations cannot exceed 100%; shared work retains one activity ID |
| AC-07 | EVD-01–05, DAT-03 | Material reported findings resolve directly to retained sources and locators; interpretive confidence and conflicts are recorded without requiring separate claim tables |
| AC-08 | DIS-01–05 | Logged priority searches and recent yields support the stated stopping reason; unsearched areas remain disclosed gaps; release does not require the optional 25-result batches |
| AC-09 | NET-01–03 | A typed source-backed relationship distinguishes funding from membership; repeat partner searches do not duplicate candidates |
| AC-10 | REP-01–04, NFR-01–02 | With web retrieval and AI calls disabled, a clean reproduction regenerates the same records, counts, calculations, maps, and substantive narrative from retained reviewed inputs and the identified commit. Saved AI-written text is reused, not regenerated. Readable and machine-readable outputs agree; documented non-analytical metadata differences are permitted. A fresh discovery run is not required to find identical sources. |
| AC-11 | GOV-02–03, NFR-03–04 | Fresh research starts with assigned seed IDs and empty staging; reviewer/steward start only from addressed handoffs after the prior agent stops. No census agents overlap. Steward closure preserves the review history before clearing all active staging files. One shared HTML renderer carries the page from research proposal through reviewed proposal to steward-validated signoff readiness, using authoritative records and exact input hashes; changed inputs flag stale review. Candidate and role states remain distinct; proposal editing freezes during independent review and owner signoff. Accepted group-review metadata survives integration and staging reset. Recording approval leaves the proposal digest unchanged; modifying an approved value requires renewed review/signoff. Unresolvable corrections are explicitly deferred, and commit/cleanup permissions match recorded owner authorization. Independent review uses a fresh session; requested/actual model and effort (or explicit unknowns) are recorded and retained with review provenance. Separate owner publication authorization is recorded. |
| AC-12 | DAT-02–04, REP-04 | Import preserves source row/name references; repeated import avoids duplicates; a rename remains the same entity and Git shows the change |
| AC-13 | ENT-05, EVD-06, NFR-05 | Excluded institutional profiles remain outside census counts; a necessary public partner reference may remain; personal communication alone cannot support inclusion or findings |
| AC-14 | DIS-06–08, GOV-02, NFR-01 | Starting seeds map to candidates without automatic inclusion; new discoveries enter a later list revision with provenance; earlier report reproduction remains unchanged |
| AC-15 | REP-06 | The report links to its exact starting seed revision, states candidate-only meaning, and identifies the resulting revision and change summary if different; archived Git state retains those lists |
| AC-16 | REP-07, NFR-01 | The report displays the generating commit and immutable public link; relevant uncommitted or untracked inputs block release; one manifest resolves retained external evidence, command/environment, and output hashes |
| AC-17 | REP-08–09, BIO-03, NFR-01 | A lower Deschutes program has an approximate regional polygon, not a headquarters or whole-basin proxy; disjoint work stays separate; unknown locations remain null; committed geometry and evidence links reproduce the map without reenacting manual drawing |
| AC-18 | REP-04, REP-10, FIN-05 | Two releases in the same year have unique labels, publication dates, cutoffs, and generating commits. Reports show candidate coverage, distinguish unresearched from unavailable financial information, and summarize represented fiscal periods. A carried-forward observation retains its original dates; a newer filing, correction, or discovery is distinguished from actual organizational change. Incomplete annual data does not block release. |
| AC-19 | REP-11–12, REP-08–10 | A release bundle exists under the README output convention, and a stable public landing address links to its permanent HTML report and map. Name/ID lookup and data downloads work. The viewer loads every indexed GeoJSON file, supports layer visibility and extent controls, exposes overlapping and null-geometry entities, and links findings to provenance. Footprints and the list remain usable without basemap tiles; a later release leaves earlier bundles unchanged. |
| AC-20 | REP-13, GOV-03, REP-07 | Committing/pushing a new source or generating a preview does not create a release, deploy a report, or change the public landing pointer. Explicit publication uses the supplied commit, label, cutoff, and recorded parameters. Missing review or failed validation prevents publication; an existing label cannot be overwritten. Successful publication preserves earlier release bundles and updates the latest link only when the new release is available. |

### Release gate

All P0 requirements applicable to the release must pass. Each included entity must have a stable ID, supported inclusion reason, and source references. Reported financial values require metric, period, currency, reporting boundary, and evidence. Estimates are optional, but any published material estimate requires its method, bounds, assumptions, and independent review. Every included entity has a saved footprint file, with null geometry allowed where location evidence is insufficient.

The release must identify a clean generating commit, have independent release review and explicit owner publication authorization, and pass reproduction from retained inputs. Unresolved identity or budget overlap blocks only the affected inclusion or aggregate. A release need not cover a complete year or use the same fiscal year for every entity. Missing disclosures and incomplete discovery are permitted when clearly disclosed; they must not be converted into zeros or completeness claims. Git history, direct evidence references, and the single manifest provide the required provenance without separate audit or approval services.

## 11 Open decisions and phased implementation

### Decisions for owner review

| **ID** | **Decision** | **Proposed default and consequence** |
| --- | --- | --- |
| OD-01 | Historical pass mapping | Reconcile P00–P06 with workbook before migrating search history |
| OD-02 | Search stopping rule | Agree priority searches and effort limits; report yield and gaps; test numerical saturation batches only where useful |
| OD-03 | Relevance and geographic coverage | Require an evidenced pathway to wild steelhead; agree evidence-based Pacific Rim search priorities and disclose unsearched areas; retain unsupported leads as deferred |
| OD-04 | Financial observation selection | Select the latest usable evidence available by the cutoff, retain each observation’s fiscal period and source date, and compare compatible-period subsets; disclose missingness and mixed periods |
| OD-05 | Attribution denominator | Prefer compatible program expense; allow separately labeled revenue capacity proxies |
| OD-06 | Effort allocation | Retain overlapping activity coverage; permit additive resource partitions only with supported allocations |
| OD-07 | Taxonomy authority and incomplete risk section | Complete Section 03 of the discussion document and approve its resulting risk codebook before running the full census; approve the life-stage codebook drawn from Section 02 jointly with manuscript reviewers before production coding |
| OD-08 | File formats and repository layout | Use a few structured text files with direct source references; introduce a database or hosted interface only for demonstrated needs |
| OD-09 | Release timing and archiving | Issue dated snapshots when useful, including multiple releases per year; optional annual planning review carries no publication obligation; agree durable archives and evidence backup locations |
| OD-10 | Publication and source retention | Confirm public-source eligibility, licensing, permitted source copies, and exclusion of prohibited personal data |
| OD-11 | Prototype hosting and address | Provisionally use GitHub Pages for the report/map and GitHub Releases for download archives. Confirm configuration and actual public address in the README; preserve earlier release addresses on deployment. Revisit the hosting choice after prototyping if needed |

### Phase 0 Repository and baseline reconciliation

Use the existing public repository and seed list. Choose simple record formats, establish a concise source index and decision log, and document initial workbook provenance. Preserve original row/name references, route excluded institutional profiles to the separate census, and retain permitted public evidence. Agree search priorities and the release command/manifest structure. Record the outstanding Section 03 dependency without inventing risk categories.

### Phase 1 Small reproducible pilot

Use a small diverse candidate sample to exercise screening, available financial data, program-level activities, relationships, approximate GeoJSON, direct evidence links, and Git history. Discovery and profile preparation can proceed while Section 03 is incomplete; mark risk coding pending. Exercise AC-01–20 for capabilities used, with risk-code checks deferred until the codebook is approved. Produce a clearly labeled pilot from a clean commit and demonstrate that another person can reproduce its reported results from the archive. No database, hosted application backend, or comprehensive funding reconciliation is required; implement the static report and GeoJSON viewer under REP-11–12.

### Phase 2 Pacific Rim census and dated releases

Begin the full census only after Section 03 and its risk codebook are completed and approved under BIO-02. Extend research according to documented steelhead connections and search priorities across the Pacific Rim scope. Use P00–P06 to organize discovery, report yield and remaining gaps, and issue dated evidence snapshots when useful, including multiple releases per year, from clean commits with linked seeds, GeoJSON files, and one manifest each. All applicable P0 checks, including approved risk coding, must pass for a full release. Completion of every geographic search or optional saturation batch is not a release prerequisite; claims must match actual coverage. Neither a complete annual financial dataset nor an annual publication is required.

### Phase 3 Additional analysis when justified

Add comparative risk analysis, sensitivity views, deeper funding-flow reconciliation, or network exploration as evidence and research needs justify them. Introduce a database, multiuser interface, or service targets only if the repository workflow becomes inadequate. Preserve the same public provenance, scope boundaries, and reproducibility controls.

### Context register

The methodological starting point is the Steelhead Organizations Chat, conversation ID 6ac57769-bca8-83e9-80cb-fbf6a05e0e02, including its separation of Organizations and Institutions — Non-NGO and its handling of relevance review before inclusion. The referenced baseline artifact is steelhead_nonprofit_census_updated.xlsx. Its authoritative copy, checksum, sheet inventory, and historical definitions are to be entered during Phase 0. Historical non-NGO records MUST be routed to the separate institutional census; only necessary relationship references remain here.

This requirements version establishes a reviewable specification. Approval of a requirements draft does not approve estimates, certify organizational status, or establish biological outcomes. Subsequent changes require versioned decisions and traceable acceptance evidence.

## Provisional owner decision interface

**OWN-01 | P0 |** The shared staging HTML MUST let the owner enter accept, reject, defer, or request changes and a comment per proposal, and export a decision file bound to the exact assignment, proposal hashes, evidence/review revision, and selected-subset digest. Unselected proposals imply no decision. The steward MUST validate supplied decisions before changing staging, preserve the owner response and original researcher/reviewer positions, and route corrections through the serial handoff process. Stale decisions MUST require renewed owner inspection. Acceptance MUST NOT bypass independent review or evidence requirements, or imply permission for Git operations or publication. See the [record format](../methods/staging-record-format.md#owner-decision-entry) and role instructions.

### Standing owner integration approval

The [README owner-review-by-exception policy](../README.md#owner-review-by-exception), adopted 2026-11-11, governs routine integration approval and supersedes any earlier wording that requires a fresh owner response for every item or subset. It does not waive independent review, evidence validation, unresolved exceptions, or explicit permissions for commits and staging cleanup. The HTML remains inspectable at all stages; owner decision exports are optional overrides. Changed content requires renewed applicable review and policy evaluation; unresolved prior owner exceptions remain held.
