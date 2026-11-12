# Census development notes

Implementation status and prototype history belong here. This is not an alternative operating policy: use [workflow.md](workflow.md), [requirements](requirements/Steelhead_Organization_Census_Requirements.md) and the [format reference](methods/staging-record-format.md). Preserve historical reviews/inventories as recorded; this documentation consolidation does not migrate data or retrospectively certify it.

## Implementation status

Available: versioned seed list, role/coordinator instructions, configured model intent, staged Markdown/JSON handoff and review formats, shared static HTML renderer, optional owner-decision export and read-only validator, synthetic behavior tests, and a manually exercised coordinated research/review/correction/steward pilot. Agents perform documented integration; no automatic integration command, persistent coordinator daemon or scheduled service is installed.

Not implemented as a complete system: release-report builder, public static census/map viewer, clean/offline release reproduction command/environment/archive verification, manual publication workflow, Pages deployment and retained release archive. Their required behavior remains in the requirements; no command or public URL is claimed to work until verified. Document capability and failed checks honestly rather than embedding permanent workarounds in every role file.

The seven agreed organization deliverables are documented, but existing pilot records and current starter templates/validators have not been automatically migrated to a complete first-pass profile. Existing fixtures demonstrate renderer behavior, not complete new scientific schemas. Any migration needs a bounded reviewed assignment. Financial-data.md replaces the intended maintained financial-history CSV; do not silently delete legacy data or maintain two authorities.

## Renderer limitations

- The `signoff` display stage still says “ready for owner signoff,” and the explicit owner-approval field may say “Not recorded” when standing policy applies. That means no recorded explicit statement, not a new owner-response requirement. Preserve the actual policy basis/IDs/digest in handoff and durable review records; do not fabricate `owner_approval` to alter the label. Dedicated standing/explicit/held labels remain future UI work.
- The renderer is read-only. It validates selected structural/path/hash/before-state/dependency conditions; it does not enforce scheduling, actor identity, complete scientific schemas, all seven deliverable fields, complete source capture, scientific accuracy or owner authentication. Geometry checks cover supported types, finite bounds and closed rings, not full topology or ecological validity. Raw GeoJSON/bounds are not an interactive map.
- Text changes use whole-file before/after proposals. Paragraph/program-level independent decisions require explicit proposal boundaries or held scope, not silent partial acceptance. A source-index metadata change can invalidate multiple dependent review hashes; measure and simplify mechanical overhead without weakening review freshness.
- Source snapshots use hash-named assets; unsafe captured file extensions are served as text, not active HTML. This protects inspection, but is not proof of faithful capture completeness.
- Owner inputs live only in the current page. Download before refresh/close; no automatic save or repository write. Export matching is intentionally strict, including handoff/review bytes; validate before edits and preserve the original context/validation record. A stale export cannot authorize revised content or erase earlier exceptions.
- After integration, current destinations differ from approved pre-integration before-values, so re-rendering the same proposals can correctly show expected conflicts. Preserve the zero-error pre-integration HTML/JSON/assets under the preview directory (for example `frozen-pre-integration/`) and label it an inspection snapshot. Keep authoritative inventory/history outside output; do not rewrite original preconditions to manufacture a passing post-integration preview. A dedicated integrated-state display is future work.
- No handoff yields a no-active-assignment notice; invalid input replaces the page with an unavailable notice. A page existing on disk alone does not prove usable links or valid data. Tests do not establish browser accessibility, complete actor isolation or scientific quality; record visual/HTTP checks actually performed.

## Pilot evidence and lessons

The initial Wild Salmon Center experiment retained short researcher-created extracts. It exercised handoff/rendering but did not satisfy the later default of actual original public files or faithful captures. The later fresh coordinated pilot retained four PDF evidence files/captures with explicit donor-page/collateral-content omissions, independent checks, one metadata correction and retained review history. These are historical pilot results, not proof of full census completion or current legal status. Inspect `sources/org-wildsalmoncenter/review-history/` where present and the generating records for exact scope/hashes.

The synthetic coordinator test exercised researcher → fresh reviewer → researcher correction → fresh reviewer → mock steward. It caught an injected unsupported claim and verified only eligible mock integration. Its report recorded an output-scope scratch-file deviation and an unknown initial dispatch timestamp. Results live under ignored `output/coordinator-smoke/`; no scientific findings come from that fixture. Test deliberately flawed inputs only in isolated clearly synthetic work.

Pilot research time and total workflow time differ substantially: source acquisition/privacy checking, exact evidence review, handoff formatting, dependencies and rendering add overhead. Future comparison should record role timestamps/actual effort, missed/caught errors, correction burden and source sufficiency—not just counts or declared model names. Keep baseline configured model/effort stable for representative assignments before testing changes against the same examples. A fresh reviewer on the same model can still share blind spots; model diversity is not a substitute for independent evidence checking.

## File and Git issues

Earlier generated paths used repository-root `output/ngo-census/`. They were moved under `analysis/ngo-census/output/`, leaving manuscript output separate. Historical immutable handoffs/review inventories keep their original path strings; apply that prefix mapping to locate moved generated artifacts. Do not rewrite accepted source/history bytes merely to clean up an old display path. The old two-commit scheme that committed staging then deleted it is retired; workflow §8 defines ignored staging and deliberate durable retention.

Repository-wide `*.pdf` ignore currently also affects census evidence. Required retained PDFs must not silently disappear from an authorized commit/archive. Check ignored files before committing; a scoped ignore-rule change or explicitly authorized inclusion needs deliberate handling. This documentation rewrite does not change ignore rules, add evidence to Git or claim ignored originals are backed up. Generated output and staging remain ignored.

Historical workbook reconciliation remains open: establish authoritative copy, checksum, sheet inventory/row references and original P00–P06 meanings before importing historical searches; route institutional profiles outside the NGO census. Retain original labels rather than rewriting history to match the current proposed pass mapping. Optional numerical saturation experiments are not required search/document caps or proof of full Pacific Rim completeness.

## Deployment and release output

Provisional hosting intent is GitHub Pages for static browsing and GitHub Releases for immutable download bundles, with a separate backup. These are implementation choices, not dependencies of the retained records or proof of a live deployment. A prospective manually triggered “Publish census release” action would accept full commit, unique release label, cutoff and declared windows, validate/review/build, then archive/deploy only with explicit authorization. A normal push must never trigger publication.

Expected local bundle under `output/<release-label>/`: `index.html`, `map.html`, assets, derived entity/financial/activity/relationship exports as applicable, `geojson/index.json`, per-entity saved geometry copies, and `manifest.json` (output hashes excluding itself). The report uses reviewed research-summary text and saved other narratives. GeoJSON index identifies ID/name/path/geometry status; null and overlapping entities remain discoverable. Required public viewer behavior, offline map availability and comparisons are in REP-01–13.

Anticipated project base from earlier repository context: `https://toddringler.github.io/steelhead-marine-risk-discussion-manuscript` (unverified/not asserted live). Intended addresses:

- `<public-base>/ngo-census/`: stable latest/archive landing page.
- `<public-base>/ngo-census/releases/<release-label>/index.html`: permanent report.
- `<public-base>/ngo-census/releases/<release-label>/map.html`: permanent map.

A deployment must assemble all retained release directories so new publication leaves earlier addresses intact. Archive viewer/assets/data with report/manifest and source snapshot. A live basemap may supply context, but tile loss must not prevent footprints/list/provenance; no live geocoding. Immutable bundles—not a Git link alone—supply durable release archives.

## Consolidation review — 12 November 2026

The document rewrite keeps existing requirement IDs/priorities and file names, adds only workflow.md and this notes file, and moves exact seven-deliverable definitions to the existing format reference. Role files now contain checklists. It resolves staging commits versus ignored staging, financial CSV versus Markdown, geographic direct influence versus labeled focus, routine owner signoff versus standing exceptions, and old search/document caps versus time/coverage limits.

Before/after preservation checks are recorded under ignored `output/document-consolidation/`. They verify requirement IDs/priorities and acceptance/open-decision IDs, local document links, critical-safeguard coverage, and unchanged research/evidence/scripts/templates/test bytes. These are document checks, not a scientific release review. Detailed prose tightening and implementation/schema/template work remain separate to-do items.

## Implementation phases

Retained planning material moved from the requirements during the 12 November scrub; these are implementation goals, not proof of completed capabilities.

### Phase 0 Repository and baseline reconciliation

Use the existing public repository and seed list. Choose simple record formats, establish a concise source index and decision log, and document initial workbook provenance. Preserve original row/name references, route excluded institutional profiles to the separate census, and retain permitted public evidence. Agree search priorities and the release command/manifest structure. Record the outstanding Section 03 dependency without inventing risk categories.

### Phase 1 Small reproducible pilot

Use a small diverse candidate sample to exercise screening, available financial data, program-level activities, relationships, approximate GeoJSON, direct evidence links, and Git history. Discovery and profile preparation can proceed while Section 03 is incomplete; mark risk coding pending. Exercise AC-01–20 for capabilities used, with risk-code checks deferred until the codebook is approved. Produce a clearly labeled pilot from a clean commit and demonstrate that another person can reproduce its reported results from the archive. No database, hosted application backend, or comprehensive funding reconciliation is required; implement the static report and GeoJSON viewer under REP-11–12.

### Phase 2 Pacific Rim census and dated releases

Begin the full census only after Section 03 and its risk codebook are completed and approved under BIO-02. Extend research according to documented steelhead connections and search priorities across the Pacific Rim scope. Use P00–P06 to organize discovery, report yield and remaining gaps, and issue dated evidence snapshots when useful, including multiple releases per year, from clean commits with linked seeds, GeoJSON files, and one manifest each. All applicable P0 checks, including approved risk coding, must pass for a full release. Completion of every geographic search or saturation challenge is not a release prerequisite; claims must match actual coverage. Neither a complete annual financial dataset nor an annual publication is required.

### Phase 3 Additional analysis when justified

Add comparative risk analysis, sensitivity views, deeper funding-flow reconciliation, or network exploration as evidence and research needs justify them. Introduce a database, multiuser interface, or service targets only if the repository workflow becomes inadequate. Preserve the same public provenance, scope boundaries, and reproducibility controls.
