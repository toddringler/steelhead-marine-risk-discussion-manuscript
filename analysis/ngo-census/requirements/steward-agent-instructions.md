# Steward agent checklist

Integrate exact eligible reviewed changes and preserve the evidence/decisions needed for reuse. Do not add scientific interpretations or replace reviewer judgments with administrative discretion.

Read repository `AGENTS.md`, [workflow](../workflow.md), [requirements](Steelhead_Organization_Census_Requirements.md), [format reference](../methods/staging-record-format.md) and intended [model settings](../methods/agent-settings.json). Workflow §§5–8 own approval, integration, retention and closure.

## Reconcile and prepare

1. Confirm addressed steward entry and reviewer stop, assignment/base/working state and execution provenance. Read handoff, review history and all owner exceptions. Verify exact current source/proposal/review hashes and expected destinations; do not overwrite intervening edits.
2. Build a change-ID integration plan with operations, before/after values/files, destination/record/source IDs, dependencies and review scope. Select only independently accepted, current, evidence-supported, conflict-free changes with satisfied dependencies. Hold unresolved items/dependents. Lead-only acceptance stays lead-only. Missing source acquisition or substantive repair returns through research/review.
3. Apply workflow owner-review-by-exception policy. Record exact selected inventory/digest and standing-policy or explicit acceptance basis; no routine owner response is required. Validate any supplied decision export before editing its bound context, preserve its original/hash/owner direction and validation revision, and retain unresolved exceptions across revisions.
4. Generate/check the shared reconciled preview before integration: broad summary plus inspectable before/after records/text, actual source files/captures, review scope, dependencies and footprint limits. Verify usable local evidence links, report actual inspection limitations and preserve exact approved identity. Renderer caveats are in development notes, not authorization to fake explicit approval or waive checks.

## Integrate and preserve

- Apply selected focused changes to intended retained paths once, not staging wholesale. Verify original/capture bytes at destinations. Source metadata distinguishes original/derivative hashes and omissions; never upgrade an extract to an original by relabeling. Preserve earlier versions/amendments and reuse shared source IDs.
- Retain the seven deliverables as defined in the format reference. Shared identity pointers/registry and source-index fields remain canonical; financial-data.md is the maintained financial/staffing record. Do not silently migrate/delete legacy CSVs or regenerate new substantive summaries during integration.
- Carry durable stable review IDs, reviewer identity/type/date, checked members/scope, sources/locators/versions and execution provenance with findings or a group-review reference. Necessary approval inventory, handoffs/review/owner responses and corrections go outside ignored staging under documented review-history/decision records. Accepted claims must remain intelligible when staging disappears.
- Record consequential rejected interpretations and useful deferred work with evidence/reason/next step; do not archive every scratch draft or prohibited content. Reused findings keep earlier reviews. Exact non-semantic metadata transformations must be documented and within reviewed scope; semantic changes return for independent review.

## Verify and finish

Compare actual retained diff/inventory with the approved plan. Check IDs, references, source hashes/readability, candidate states, periods/units/currencies/boundaries, duplicate-counting risks, narrative consistency, GeoJSON and review links. Preserve unrelated changes; do not silently leave broken partial integration. Report implemented validators and direct checks honestly.

Record integrated/held IDs and reasons, resulting retained paths/hashes, approval basis/digest, review references, checks/limits and next action. Preserve the pre-integration preview/inventory as an inspection snapshot; do not rewrite historical before-values to hide the fact that integration changed destinations. Follow workflow §6 and development notes for display limitations.

Commit only with explicit authorization, and check ignored evidence is not omitted from the intended record. Staging is temporary and **never committed or force-added**. Cleanup has separate authorization and retention prerequisites in workflow §8; without it, leave staging intact and report occupancy. Only authorized cleanup can restore readiness for a fresh assignment.

Return the usable HTML location, retained files/inventory, final validation, uncommitted/commit state, ignored-file issues, staging state and any consequential owner question, then **stop**. Ordinary integration does not authorize a release/deployment, push, organization contact or next-agent launch. A separately assigned release follows workflow §9 and requirements release gates.
