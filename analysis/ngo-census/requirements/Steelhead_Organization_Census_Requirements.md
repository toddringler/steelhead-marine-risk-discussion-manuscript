# Wild Steelhead Organization Census Requirements

Version 0.3 | Review draft | 11 November 2026

1 Purpose and review decision

This document specifies a repeatable system to identify, analyze, and track NGO-like organizations whose activities affect wild steelhead conservation across the entire Pacific Rim. It supports review of conservation effort across geography, life stages, and biological risks, and supplies a traceable institutional evidence base for the steelhead discussion paper.

**Reviewers should approve the scope, entity distinctions, evidence rules, and release criteria, then resolve the decisions in Section 11 before a production baseline is issued. Requirements describe desired system behavior; they do not assert that the census is complete or that an organization's budget measures its conservation effectiveness.**

### Goals

- Discover relevant organizations systematically.

- For each organization, document legal identity, operating units, financial reporting boundaries, and relationships.

- For each organization, describe attributable steelhead effort with explicit uncertainty and evidence.

- For each organization, compare documented effort with life stages and risk categories.

- For each organization, reproduce annual snapshots and document changes in methods, identity, and activity.

### Scope

Include independent nonprofits, charities, and comparable nongovernmental bodies across Pacific Rim jurisdictions, including US nonprofits and Canadian registered charities, as well as fiscally sponsored projects, initiatives, coalitions, chapters, and parent organizations. An entity may qualify through direct steelhead work or a documented indirect pathway, such as watershed restoration, harvest policy, estuary protection, marine research, or hatchery reform affecting wild steelhead. Record supportive, adverse, mixed, or uncertain effects without inferring intent.

The geographic scope includes all countries and territories bordering the Pacific Ocean, their relevant inland watersheds, and shared offshore and international Pacific waters. Include organizations headquartered elsewhere when their work affects wild steelhead conservation within this scope. Geographic inclusion does not presume that steelhead occur in every jurisdiction; each included organization still requires an evidenced conservation pathway. Record headquarters separately from operating geography. Distinguish wild steelhead from resident rainbow trout, hatchery steelhead, and salmon generally; broader work requires a stated steelhead relevance rationale. Historical and inactive entities remain available for longitudinal analysis.

Government agencies, Indigenous governments, universities, public partnerships, and other similar institutions will be analyzed in a separate census and, thus, are excluded in this census.

This census can only make use of publicly available data. Inclusion of individual donors, private personal data, and other non-public data sources is prohibited. Personal communications can be used to help identify missing public data sources, but cannot serve as the basis of evidence.

### Requirement conventions

MUST is mandatory for the applicable phase; SHOULD is expected unless a documented exception is approved; MAY is optional. P0 denotes baseline release blockers, P1 denotes the next operational phase, and P2 denotes later analytical capability. IDs remain stable across revisions. Proposed methods in this version require owner approval before being treated as established census practice.

2 Governance and operating model

The census owner approves scope, taxonomies, estimation methods, and releases. Researchers discover and document candidates. Reviewers resolve identity, evidence, and classification issues. A data steward manages identifiers, imports, validation, backups, and snapshots. One person may hold multiple roles during the pilot, but a second person must review material estimates and identity merges before release.

An annual census cycle has a declared evidence cutoff, target financial years, discovery coverage plan, and methodology version. A release includes immutable data, a source manifest, validation results, exceptions, coverage statistics, and a change log. Changes after release create a new version; they never silently overwrite a published result.

### Core operating requirements

**GOV-01 |** P0 | The system MUST maintain an inclusion policy, versioned codebook, named decision owner, and decision log with dates and reasons.

**GOV-02 |** P0 | Each record MUST have a workflow status: discovered, screening, research, review, approved, excluded, or deferred. Exclusions and deferrals MUST retain reasons and discovery provenance.

**GOV-03 |** P0 | Publication MUST require reviewer signoff, a passed validation report, and resolution or explicit disclosure of all material exceptions.

**GOV-04 |** P1 | The owner SHOULD review relevance, inactive status, taxonomy changes, and search coverage annually, including organizations with missing filings or changed websites.

### Analytical boundaries

Legal-entity counts answer how many independently constituted bodies are represented. Operating-node counts answer how many projects, chapters, initiatives, or coalitions are represented. Neither is a count of independent budgets. Reports must name their counting unit and date. Financial capacity, program expenditure, attributed steelhead resources, documented activity, and biological outcomes are separate measures.

An organization can address several life stages and risks. Multi-label coverage indicates documented activity, not an additive division of resources. A budget allocation is permitted only when its denominator and mutually exclusive allocation rule are recorded. Network centrality describes observed relationships within the census boundary; it is not evidence of conservation impact.

### Review and change control

Each material change records actor, timestamp, old value, new value, supporting evidence, and reason. A material change affects identity, inclusion, financial amounts, share estimates, classifications used in reporting, or aggregate results. Reviewers can return a record for research. Disagreements retain both interpretations and the final decision rather than erasing the earlier evidence.

3 Entity model and counting rules

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

**ENT-03 |** P0 | Parent, chapter, fiscal sponsor, program, affiliate, predecessor, successor, and merger relationships MUST have effective dates, evidence, and a confidence label.

**ENT-04 |** P0 | Merges MUST preserve source IDs and an alias map; splits and mistaken merges MUST be reversible. Reorganizations MUST NOT silently rewrite historical identity.

**ENT-05 |** P0 | Every entity MUST be assigned to NGO-like, excluded, or unresolved cohort. Legal status and analytical cohort MUST be stored separately.

### Double counting controls

**CNT-01 |** P0 | A financial observation MUST identify the reporting body, period, consolidation boundary, metric, and source. Child programs MUST NOT inherit parent revenue as their own revenue.

**CNT-02 |** P0 | Reports MUST prevent summing a consolidated parent amount with included child amounts. Unknown consolidation boundaries MUST be flagged and excluded from consolidated totals until resolved.

**CNT-03 |** P0 | Grants and transfers MUST be recorded as funding flows when evidenced. A report MUST distinguish gross organizational receipts from resources net of identified internal transfers and disclose unresolved flows.

**CNT-04 |** P0 | Coalition membership and shared partnerships MUST NOT create additional attributable spending. Joint activities MUST use one activity ID with participating entities and any evidenced allocation.

4 Discovery and saturation

Discovery uses P00 through P06 as a repeatable pass framework. The following mapping is proposed for approval and reconciliation with the historical workbook. Preserve any historical labels, queries, and results on import; do not relabel earlier work as if it used this mapping.

| **Pass** | **Proposed purpose** | **Required coverage evidence** |
| --- | --- | --- |
| P00 | Import seeds and reconcile baseline | Source rows, aliases, known gaps |
| P01 | Steelhead and place searches | Queries by jurisdiction and basin |
| P02 | Legal registry and filing searches | Jurisdiction-specific identity checks |
| P03 | Broader conservation searches | Watersheds, fisheries, habitat and policy |
| P04 | Partner and funding network expansion | New candidates from observed edges |
| P05 | Structure and chapter searches | Sponsors, parents, affiliates and programs |
| P06 | Gap audit and saturation challenge | Missing geography, stages, risks and NGO types |

### Discovery requirements

**DIS-01 |** P0 | Every search run MUST record pass, date, researcher, search service or source, exact query or filter, geography, language, scope, results reviewed, and stopping point. Failed searches and zero-result searches MUST be logged.

**DIS-02 |** P0 | Candidates MUST retain discovery run IDs, source URLs, screening decision, relevance reason, and duplicate-resolution result. A rediscovered entity MUST link to its existing ID.

**DIS-03 |** P0 | The coverage matrix MUST cover the entire Pacific Rim using a versioned register of countries, territories, subnational jurisdictions, relevant watersheds, and shared marine areas, with pass completion, broad organization types, life-stage coverage, and unresolved gaps. Searches MUST use jurisdiction-appropriate terminology, local names, and a documented language and translation strategy. Areas not yet searched MUST remain explicit coverage gaps.

**DIS-04 |** P0 | Network expansion MUST log each frontier, seeds, candidate yield, and whether it was exhausted or deliberately bounded. Unbounded recursive searches MUST be prevented by cycle detection and run limits.

**DIS-05 |** P0 | Saturation MUST be evaluated within declared search boundaries and reported with residual blind spots. No eligible discoveries alone MUST NOT be interpreted as proof of a complete population census.

### Proposed saturation rule

After all planned passes and gap cells are completed or justified, perform two additional independent discovery batches for each jurisdiction. Each batch must review at least 25 previously unreviewed candidate results, or exhaust a documented source or query frontier when fewer exist. Record the number screened, eligible new unique entities, duplicates, and unresolved candidates. The provisional saturation criterion is zero new eligible unique entities in both batches and no unresolved candidate likely to qualify. A new eligible discovery resets the sequence for that jurisdiction and triggers a targeted gap review.

This threshold is a proposed operational stopping rule, not a statistical confidence bound. The owner may replace it after the pilot, with the change logged and prior results preserved. Publish marginal yield by pass and jurisdiction, including exclusions and duplicate rates, so readers can assess search effort and diminishing returns. The owner may identify a previously unidentified, publicly available data source as a seed for additional discovery. The new seed and resulting searches MUST be logged, with saturation reassessed for affected search areas.

5 Evidence and organizational analysis

Evidence supports individual claims rather than an entire row by association. A legal filing can support identity and revenue while a program report supports work in an estuary. Neither automatically establishes the other's claims.

### Evidence standards

**EVD-01 |** P0 | Each material claim MUST link to at least one source with publisher, title, URL or file reference, publication date if known, access date, period covered, page or section locator, and a short supporting extract or faithful summary.

**EVD-02 |** P0 | Sources MUST be classified as official filing or registry, organizational report, partner or funder report, independent research, news, or discovery lead. Search snippets and generated summaries MUST NOT be sole evidence for approved material claims.

**EVD-03 |** P0 | Conflicting sources MUST be retained with the selected interpretation, reason, reviewer, and date. Missing, not applicable, not disclosed, and estimated MUST be distinguishable from zero.

**EVD-04 |** P0 | The system MUST retain a source manifest and, where permitted, a captured copy or content hash. Inaccessible or changed sources MUST retain their original citation and retrieval status.

**EVD-05 |** P0 | Claim confidence MUST use high, medium, low, or unresolved with a rationale. Evidence recency, directness, scope match, and corroboration MUST inform this judgment; an automated score alone MUST NOT approve a claim.

**EVD-06 |** P0 | Approved claims MUST be supported by publicly available sources. Personal communications MUST be treated only as discovery leads; approval requires locating and citing the underlying public source. Sources containing prohibited individual donor or private personal data MUST NOT be imported into the census.

### Financial and staffing requirements

**FIN-01 |** P0 | US records MUST support EIN and IRS Form 990 family filing references; Canadian records MUST support charity registration identifiers and CRA T3010 references. Other jurisdictions MUST support applicable local legal identifiers, registries, financial disclosures, and original-language source references, with translated labels and an explicit record of disclosure availability. Legal status and filing availability MUST be verified separately; no filing MUST NOT imply no activity or no revenue.

**FIN-02 |** P0 | Each observation MUST store exact fiscal start and end dates, filing or tax year label, filing type, amendment status, currency, metric definition, value, source locator, and reporting boundary. Revenue, expenses, assets, grants, and program spending MUST remain distinct metrics.

**FIN-03 |** P0 | Reports MUST retain native currency and financial periods. Currency conversion MUST record rate, rate source, rate date or averaging period, method, and target currency. Unconverted amounts in different currencies MUST NOT be summed.

**FIN-04 |** P0 | Staff observations MUST distinguish employees, full-time equivalents, contractors, volunteers, and board members, with date, organization or program scope, units, and evidence. Missing staffing data MUST NOT become zero.

**FIN-05 |** P1 | Amendments SHOULD supersede selected values for current views while preserving earlier versions. Financial-year mismatch, stale data, and partial-year reporting SHOULD be visible in exports and comparisons.

Prefer the relevant official filing for reported financial values and primary program records for activity claims. Organizations outside filing systems remain eligible when relevance and identity can be supported. Third-party estimates must retain their origin and must never be presented as filed values.

6 Steelhead effort and biological classification

### Attribution requirements

**ATT-01 |** P0 | Each steelhead-share estimate MUST store low and high bounds, denominator metric and period, organizational scope, method, evidence, assumptions, estimator, reviewer, confidence, and review date. Bounds MUST satisfy 0 ≤ low ≤ high ≤ 1.

**ATT-02 |** P0 | Estimates MUST distinguish directly reported steelhead expenditure, allocated program expenditure, proxy allocation, and qualitative evidence only. General salmon work MUST NOT automatically receive a steelhead allocation.

**ATT-03 |** P0 | A derived monetary range MUST use a compatible expenditure denominator. Revenue multiplied by share MAY be shown only as a labeled capacity proxy, never as attributable spending. Unknown denominator or unsupported share MUST produce no monetary estimate.

**ATT-04 |** P0 | Staff time, financial resources, projects, policy actions, and outcomes MUST be stored as different measures. The system MUST NOT convert one into another without an explicit, reviewed method.

**ATT-05 |** P1 | Sensitivity views SHOULD show results under low and high attribution assumptions and alternative inclusion choices. Midpoints MUST NOT be treated as observed values or sums of ranges as probabilistic confidence intervals.

For example, a hypothetical organization with USD 1 million in compatible program expenditure and a supported 10–20 percent share yields USD 100,000–200,000 in estimated attributed expenditure. If only revenue is known, the same calculation represents a revenue-based capacity proxy. It cannot be added to expenditure estimates in a single effort total. The example is a validation fixture, not census evidence.

### Life stages and risks

**BIO-01 |** P0 | Activities MUST support freshwater, estuary, and marine environments, with migration and transition links. Proposed life stages are spawning, **incubation, juvenile rearing, downstream migration, ocean entry, marine residence, adult return, and repeat spawning.** Unknown and cross-stage work MUST be supported.

**BIO-02 |** P0 | **The initial risk codebook MUST cover habitat access and connectivity; flow and water quantity; temperature and water quality; habitat condition; harvest and bycatch; hatchery and genetic interactions; disease and parasites; predation and food-web change; marine climate and productivity; and cumulative interactions. Each code MUST define inclusion, exclusion, examples, and evidence needs before operational use.**

**BIO-03 |** P0 | Activity coding MUST store affected geography or population, stage, environment, risk, intervention type, period, direct or indirect pathway, evidence, and confidence. Advocacy or research subject matter MUST NOT establish a demonstrated biological effect.

**BIO-04 |** P0 | Multi-label classifications MUST NOT imply additive spending shares. Allocations MUST specify exclusive partitions or a separate overlap treatment and reconcile to at most 100 percent of the defined denominator.

**BIO-05 |** P1 | Risk–effort comparisons SHOULD use a separate evidence base for biological importance, controllability, and uncertainty. Reports MUST disclose incompatible scales and MUST NOT infer neglected risk solely from few organizational mentions.

7 Partner networks and reporting

Relationships explain funding, governance, and collaboration. Their presence, direction, and meaning must be evidenced independently. A website logo may establish a claimed association but does not establish a funding amount, legal control, or current partnership.

### Network requirements

**NET-01 |** P0 | Edges MUST have source entity, target entity, controlled relationship type, direction, validity period, evidence, confidence, and status. Symmetric collaborations MUST be represented consistently to avoid duplicate edges.

**NET-02 |** P0 | Edge types MUST distinguish grants, fiscal sponsorship, governance or parentage, coalition membership, joint implementation, research collaboration, and advocacy alignment. An unknown relationship type MUST remain unresolved.

**NET-03 |** P0 | Funding edges MUST support amount, currency, fiscal period, donor, recipient, restricted purpose, and whether inclusion in reported financial observations is known. Unknown amounts MUST remain null.

**NET-04 |** P1 | Network views SHOULD allow filtering by date, geography, edge type, confidence, and cohort, and show missing or incomplete relationship coverage.

### Reporting requirements

**REP-01 |** P0 | Users MUST be able to filter and export entities, financial observations, activities, relationships, sources, and decisions by year, jurisdiction, cohort, structure, stage, risk, and review status.

**REP-02 |** P0 | Each aggregate MUST disclose counting unit, population boundary, evidence cutoff, currency method, financial-year treatment, unknown coverage, exclusions, methodology version, and double-counting adjustments.

**REP-03 |** P0 | The system MUST provide separate views for legal entities, operating nodes, gross financial capacity, attributed expenditure, and qualitative activity coverage. Totals MUST be reproducible from exported records.

**REP-04 |** P1 | Annual comparison SHOULD classify changes as newly discovered, newly established, closed, merged, renamed, newly relevant, changed activity, revised evidence, or changed methodology. Discovery timing MUST NOT be presented as growth in the sector.

**REP-05 |** P2 | Users MAY compare network structure and effort distribution across risks and stages, provided denominator compatibility, uncertainty, and unresolved coverage remain visible.

### Interpretation rules

Non-NGO institutions are outside this census and belong in the separate institutional census. When a public source names an excluded institution as a partner or funder, retain only the reference needed to document the NGO relationship, with an exclusion flag and an optional link to the separate census. Do not create a full institutional profile or include institutional budgets in this census. Apply the same reference-only treatment to partners outside the target geography.

Reports must expose unknown values and stale evidence. A blank cell is not evidence that an organization does no marine work. A small attributed budget is not evidence of low effectiveness. A large partner network is not evidence of stronger biological outcomes.

8 Data schema and validation

Use normalized logical tables or equivalent structured sheets with stable keys. Identifiers are strings; dates use ISO 8601; money uses fixed decimal values and ISO currency codes. Controlled terms are versioned lookup records. Many-to-many classifications and evidence links use join tables rather than comma-separated text as the authoritative representation.

| **Table and key** | **Minimum fields beyond key** |
| --- | --- |
| Entity — entity_id | canonical_name, type, cohort, status, country, headquarters, website, relevance, valid_from, valid_to |
| Identifier — identifier_id | entity_id, scheme, value, verification_source_id, valid_dates |
| Alias — alias_id | entity_id, name, alias_type, valid_dates |
| Geography — geography_id | country_or_territory, subnational_jurisdiction, basin_or_population, marine_area, boundary_version |
| EntityGeography — link_id | entity_id, geography_id, role, dates, claim_id |
| Financial — financial_id | entity_id, metric, amount, currency, fiscal_dates, filing_year, boundary_id, source_id, locator, selected_version |
| Staffing — staffing_id | entity_id, measure, value, units, scope, observation_date, claim_id |
| Activity — activity_id | title, description, period, pathway, intervention, effect_status, claim_id |
| ActivityEntity — link_id | activity_id, entity_id, role, allocation_if_known |
| ActivityCode — link_id | activity_id, geography_id, taxonomy_version, stage, environment, risk, claim_id |
| Attribution — estimate_id | entity_or_activity_id, denominator_id, low, high, method, assumptions, confidence, reviewer, dates |
| Relationship — edge_id | from_id, to_id, type, dates, amount_if_known, currency, claim_id |
| Source — source_id | publisher, title, URL_or_path, published_date, accessed_date, period, hash, retrieval_status |
| Claim — claim_id | subject_id, field_or_assertion, value, confidence, rationale, review_status |
| ClaimSource — link_id | claim_id, source_id, locator, extract_or_summary, evidence_role |
| DiscoveryRun — run_id | pass, query, source, geography, date, researcher, reviewed_count, stopping_point |
| CandidateDecision — decision_id | run_id, candidate_name, entity_id_if_known, decision, reason, reviewer |
| Boundary and Flow — boundary_id / flow_id | included_entities, period, consolidation_rule / payer, payee, amount, included_observations |
| Snapshot and Audit — snapshot_id / event_id | cutoff, method_version, manifest_hash / actor, time, object, old, new, reason |

### Schema requirements

**DAT-01 |** P0 | Foreign keys MUST resolve; required fields, enumerations, date ordering, currency codes, uniqueness constraints, and attribution bounds MUST be validated before approval.

**DAT-02 |** P0 | Typed null reasons MUST accompany missing material values. Original imported values and source row identifiers MUST be preserved alongside normalized values.

**DAT-03 |** P0 | Each approved analytical value MUST resolve through claims to evidence and through snapshot membership to a release. Snapshot membership MUST identify exact record versions.

**DAT-04 |** P1 | Imports SHOULD be idempotent, staged, validated, and reversible, with field mapping, rejected-row reports, and explicit review of changed identities.

9 Workflows and nonfunctional requirements

### Research to release workflow

1. Plan the cycle. Declare coverage, cutoff, financial-year policy, methods, responsibilities, and known gaps. Inventory the previous workbook and preserve an unmodified source copy.

2. Import and discover. Map sheets and columns, retain original row IDs, run P00–P06, and screen candidates. Separate inclusion from legal verification.

3. Resolve identity and structure. Verify identifiers, aliases, sponsors, parentage, chapters, and financial boundaries before aggregating resources.

4. Research and code. Capture filings, program evidence, staffing, activities, networks, geography, stages, and risks. Record unknowns and conflicts as work items.

5. Estimate and review. Use compatible denominators, document share bounds, check overlap, and obtain a second review for estimates and merges.

6. Validate and release. Run acceptance checks, adjudicate exceptions, review saturation, freeze the snapshot, and publish the manifest and limitations with exports.

7. Refresh. Recheck high-change records and inaccessible sources, run annual gap searches, retain prior versions, and distinguish substantive change from improved discovery.

### Nonfunctional requirements

**NFR-01 |** P0 | A release MUST be reproducible from its frozen records, codebook, calculations, conversion rates, and source manifest without relying on live web pages or undocumented spreadsheet edits.

**NFR-02 |** P0 | The system MUST provide editable open exports in CSV or JSON plus a readable workbook; exports MUST retain IDs, units, null reasons, and evidence links. A proprietary interface MUST NOT be the only copy.

**NFR-03 |** P0 | Researchers MUST be able to correct records without losing history. Administrative permissions MUST control merges, taxonomy changes, and release publication; read access MUST be separable from edit access.

**NFR-04 |** P0 | The pilot MUST retain a backup before each import and release. A restore rehearsal MUST reproduce record counts and checksums for the most recent frozen snapshot. Daily backup and a one-business-day recovery target are proposed for routine operation.

**NFR-05 |** P0 | Collection MUST use publicly available organizational data and respect source access and reuse conditions. Individual donor records, private personal data, and non-public sources MUST NOT be included. Personal communications MAY identify public sources but MUST NOT support census claims. Source captures and exports MUST exclude prohibited personal data and credentials.

**NFR-06 |** P1 | At a proposed benchmark of 10,000 entities, 100,000 claims, and 50,000 relationships, common filters SHOULD return within three seconds and full structured export within two minutes on the declared reference environment.

**NFR-07 |** P0 | Forms and exports MUST use clear labels, keyboard-operable controls where applicable, readable contrast, and text alternatives for analytical graphics. Errors MUST identify the affected record and corrective action.

**NFR-08 |** P1 | Automated extraction SHOULD log failures and support retry without duplicate records. Machine-proposed classifications MUST remain marked unreviewed until approved by a person.

10 Validation and acceptance

The pilot must use fixtures covering North American and western Pacific jurisdictions, another Pacific Rim region, shared marine areas, USD and CAD plus at least one additional currency, jurisdiction-specific disclosures and translated evidence, independent legal bodies, a sponsor and project, parent and chapter, coalition, an excluded institution referenced only as a partner, shared activity, unknown financial values, conflicting evidence, and a merger. Fixtures may be synthetic if clearly separated from census records. The reviewer records expected and actual results with the linked requirement IDs.

| **Test ID** | **Requirements** | **Passing result** |
| --- | --- | --- |
| AC-01 | ENT-01–05, DAT-01 | Same verified identifier resolves once; similar names stay separate pending review; merge can be reversed with history intact |
| AC-02 | CNT-01–04 | Parent USD 1m including child USD 200k reports USD 1m consolidated; coalition adds no independent budget |
| AC-03 | CNT-03, NET-03 | USD 100k internal grant is visible in gross receipts and removed once in a compatible net flow view; unknown flows are disclosed |
| AC-04 | FIN-01–05 | All native currencies remain separate until a documented conversion; fiscal-year mismatches are flagged; null staff stays unknown |
| AC-05 | ATT-01–04 | 10–20% of USD 1m compatible expense yields USD 100k–200k; revenue-only input is labeled proxy; missing support yields no amount |
| AC-06 | BIO-01–04 | One shared activity can have multiple stage/risk labels without multiplying money; allocation above 100% is blocked |
| AC-07 | EVD-01–05, DAT-03 | Every material approved value in the pilot has a locatable claim/source chain; conflict and broken-link fixtures remain visible |
| AC-08 | DIS-01–05 | Each pass is logged; yield and coverage reconcile; a late eligible entity resets the proposed saturation sequence |
| AC-09 | NET-01–03 | Dated, typed edges distinguish funding from membership; cycles do not create duplicate entities or infinite discovery |
| AC-10 | REP-01–04, NFR-01–02 | Reviewer regenerates counts and monetary ranges from export with exact reconciliation to the frozen report |
| AC-11 | GOV-02–03, NFR-03–05 | Unapproved material estimates cannot enter a release; unauthorized edits fail; restore preserves snapshot checksums |
| AC-12 | DAT-02–04, REP-04 | Import preserves original row references; rerun creates no duplicates; rename does not appear as a new legal body |
| AC-13 | ENT-05, EVD-06, NFR-05 | Institutional profile is excluded; a necessary public partner reference remains outside counts and budgets; personal communication alone cannot approve a claim; prohibited personal data is rejected. |

### Release gate

All P0 requirements applicable to the release must pass. Every included record must have a stable ID, cohort, inclusion rationale, review status, and provenance. Every financial value must have period, currency, metric, source, and reporting boundary. Every published estimate must have evidence, method, bounds, denominator, and second review. Missing financial data does not disqualify a relevant entity; it limits the financial views in which it can appear.

Validation must report orphan keys, duplicate identifiers, unresolved boundaries, unsupported claims, stale evidence, unknown values, and incomplete search cells. Material unresolved identity or aggregation problems block the affected aggregate. A partial release is permitted only when excluded aggregates and incomplete coverage are explicit and approved; it must not claim saturation for unfinished geography.

11 Open decisions and phased implementation

### Decisions for owner review

| **ID** | **Decision** | **Proposed default and consequence** |
| --- | --- | --- |
| OD-01 | Historical pass mapping | Reconcile P00–P06 with workbook before migrating search history |
| OD-02 | Saturation threshold | Pilot the two-batch rule in Section 4; approve before claiming operational saturation |
| OD-03 | Relevance and geographic coverage | Require an evidenced pathway to wild steelhead; approve the full Pacific Rim geographic register and regional search sequence; retain unsupported leads as deferred |
| OD-04 | Year alignment | Use latest available fiscal year at cutoff, label year distribution, and provide comparable-year subsets |
| OD-05 | Attribution denominator | Prefer compatible program expense; allow separately labeled revenue capacity proxies |
| OD-06 | Effort allocation | Retain overlapping activity coverage; permit additive resource partitions only with supported allocations |
| OD-07 | Taxonomy authority | Approve the initial risk and life-stage codebook jointly with manuscript reviewers before coding production records |
| OD-08 | Platform and scale | Start with normalized workbook sheets; migrate to a relational store when concurrent editing or integrity needs justify it |
| OD-09 | Refresh and service targets | Annual full review with quarterly checks for priority records; confirm backup, recovery, and performance targets |
| OD-10 | Publication and source retention | Confirm public-source eligibility, licensing, permitted source copies, and exclusion of prohibited personal data |

### Phase 0 Method and baseline reconciliation

Inventory the historical workbook, sheet purposes, formulas, pass definitions, source links, and entity counts. Route excluded institutional profiles to the separate census and screen imported sources for compliance with the public-data rule. Produce a field map, discrepancy log, codebook, and approved decision register. Exit when every original row has a preserved reference and a mapped destination or documented exclusion. Do not invent missing history.

### Phase 1 Auditable census pilot

Implement all P0 controls using structured sheets or a small database. Exercise the full discovery, evidence, identity, financial, attribution, and release workflow on a deliberately diverse pilot. Exit when AC-01–13 pass for applicable P0 behavior, a second reviewer can reproduce the pilot report, and the owner approves the methods and exceptions.

### Phase 2 Pacific Rim baseline and annual operation

Extend coverage across the entire Pacific Rim geographic register, complete the approved P00–P06 plan, evaluate saturation separately by jurisdiction and shared marine search area, and issue the first annual snapshot. Stage the work by region as needed, while disclosing all unfinished areas and withholding any claim of Pacific Rim saturation until the full approved scope is addressed. Add P1 import, refresh, network, sensitivity, and performance capabilities. Exit when coverage and residual gaps are published, a restore rehearsal succeeds, and a second annual comparison can distinguish discovery from substantive change.

### Phase 3 Comparative analysis

Add P2 exploration of effort distribution and NGO relationship networks. Integrate independently supported biological risk evidence and test sensitivity to attribution, missingness, and scope. Exit when each analytical comparison has compatible measures, reproducible methods, uncertainty disclosures, and reviewer approval of interpretation.

### Context register

The methodological starting point is the Steelhead Organizations Chat, conversation ID 6ac57769-bca8-83e9-80cb-fbf6a05e0e02, including its separation of Organizations and Institutions — Non-NGO and its handling of relevance review before inclusion. The referenced baseline artifact is steelhead_nonprofit_census_updated.xlsx. Its authoritative copy, checksum, sheet inventory, and historical definitions are to be entered during Phase 0. Historical non-NGO records MUST be routed to the separate institutional census; only necessary relationship references remain here.

This requirements version establishes a reviewable specification. Approval of a requirements draft does not approve estimates, certify organizational status, or establish biological outcomes. Subsequent changes require versioned decisions and traceable acceptance evidence.
