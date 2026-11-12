# Census workflow

This is the authoritative procedure for assignments through closure. The [requirements](requirements/Steelhead_Organization_Census_Requirements.md) own scientific/reporting obligations; the [format reference](methods/staging-record-format.md) owns fields and commands. Role checklists link here. Follow repository `AGENTS.md` and the owner's assignment; owner instructions govern scope/permissions, but cannot make unresolved scientific checks complete.

Paths are relative to `analysis/ngo-census/`: retained inputs in `sources/`, temporary proposals in ignored `staging/`, generated material/local journals in ignored `output/`. Research/review records are editable text, separate from original evidence; no database or approval service is required.

## 1. Assignment and completion boundaries

Record candidate IDs/names, assignment type/questions, base commit/pre-existing changes, evidence cutoff/activity or fiscal window, deliverable coverage, budget, permissions and outputs. Verify seed identity without presuming eligibility/relevance. IDs survive renames and are never reused; preserve imported names/row references.

| Type | Completion expectation |
| --- | --- |
| First pass | All seven deliverables contain supported information or specific investigated gaps. “Not researched” alone is insufficient; supported absence, disclosure/access gaps and explained null geometry are valid. |
| Partial first pass | Budget/access limits prevent that baseline; identify missing coverage and prioritized next work. |
| Research iteration | Answer assigned questions from retained records/research-status priorities; change affected files and reuse unchanged reviewed evidence. May complete a partial baseline. |

Default: one organization, **30 minutes of research**, owner-adjustable. Stop at satisfied questions/coverage or budget expiry. Report research effort, measurable elapsed time, stopping reason and gaps; report documentation/review/rendering/handoff separately. Search/document counts are measures, **not hard caps**. Do not expand scope silently or fabricate missing evidence.

Corrections stay within the assignment, with bounded questions/effort and no automatic renewed discovery budget. Default: **two substantive correction rounds** after initial review (`methods/agent-settings.json`). Log mechanical repairs separately and diagnose recurring failures. At the limit, defer affected proposals with evidence/next action or ask the owner a consequential question; eligible work may continue.

## 2. One worker and one live staging assignment

Only **one researcher, reviewer or steward** executes at a time, including read-only review/rendering. During execution the coordinator only waits, receives completion and reports status—no census work or file edits. **Completion and the addressed file handoff** are required before dispatch; progress messages/role-field changes are insufficient. Unknown worker status blocks dispatch.

Fresh assignments require no live handoff/review/proposal files; absent staging or empty subdirectories are acceptable. Reconcile leftovers with the steward; never erase them to satisfy entry conditions. Corrections/reviewer/steward enter only through an addressed handoff after the previous worker stops.

Use one `staging/handoff.md`, reviewer-authored `review.md` when applicable, and `proposed-changes/`; no batch directories. Stage only new evidence/changed records; reference unchanged sources. Full revised Markdown files need exact expected before-text; shared CSVs use focused row proposals. Researcher/reviewer cannot modify retained sources.

Transfers record `from_role`, `to_role`, matching `current_role`, date, reason, revision/hashes and next action; preserve transfer/correction history. Roles (researcher/reviewer/steward/owner/closed) differ from candidate statuses (pending/included/excluded/deferred). **The sender then stops**; owner/authorized coordinator dispatches successors. Freeze proposals and affected dependents while owner action is pending.

## 3. Configuration and independent review

Read model/effort from versioned `methods/agent-settings.json`. Record role/session, configuration revision, requested settings, actual exposed model/release/effort, and changes with reasons/scope. Unsupported/unset settings require reporting; unexposed actual settings are unknown with reason. Configuration/spawn arguments are not runtime proof. Keep provenance in handoff and, for reviewers, review/durable review records.

Every reviewer pass, **including correction review**, uses a **fresh session without inherited chat history**. Supply assignment/instructions, proposals/evidence, methods, prior reviews/corrections and owner exceptions—not researcher private reasoning/full conversation. The **same actor cannot author** and independently accept a finding. Identify agent versus human reviewers; agent review is not human verification, and different models alone do not establish independence.

## 4. Research → review → correction

1. **Researcher:** Read retained registry, source index, deliverables, evidence and decisions first. Obtain originals/captures; propose findings/shared changes; update research status and any materially affected derived summary; check, render and hand off.
2. **Reviewer:** Check exact proposal/source hashes and expected state against appropriate evidence. Record **accepted**, **correction requested**, **deferred** or **rejected**, with scope, locators, rationale, reviewer identity/type/date and stable review ID. Checked routine rows may share a scoped review; no per-cell approval is required.
3. Accept only checked scope. Identify sampled/unchecked members; unchecked material needs an owner-approved sampling policy to inherit acceptance. Follow-up **leads remain leads**. Unknowns/qualitative profiles are valid; certainty/exhaustive disclosure is unnecessary.
4. Give bounded corrections/acceptance conditions to researcher, or a fully dispositioned set to steward. Reviewer cannot substantively rewrite and accept its own replacement. Exact non-semantic transformations may be described/accepted and recorded by steward.
5. Preserve prior reviews; renew changed proposal/source/dependency hashes and review affected content/dependents. Reuse unrelated unchanged acceptance. Unexpected frozen-state edits require reconciliation before acceptance.

Whole-file acceptance covers the whole file: split through addressed correction or hold/defer affected scope, mapping old/new proposal IDs. Escalate material identity/method/estimate disputes with evidence, alternatives, recommendation and affected IDs; routine corrections stay within the roles.

## 5. Owner review by exception

**Assume approval of individual entries unless an owner decision says otherwise; integration requires one explicit owner go-ahead for the prepared batch.** Research/review handoffs need no routine owner response. After review, steward reconciles the eligible subset, prepares the inspection HTML and freezes its inventory/digest, then hands off to owner and stops **before changing retained sources or shared records**. Provide the exact subset/digest and usable HTML URL/path. Silence means wait, not permission to integrate.

The owner may say “proceed with the reviewed batch” in chat; no per-entry clicks or JSON file are required. Bind that statement to the presented assignment/subset/digest and preserve its date/content. A general assignment or standing entry policy is not this checkpoint. After owner response and a stopped, addressed handoff back to steward, revalidate current state/reviews/dependencies and apply only the authorized eligible subset. Material proposal, evidence, review, dependency or before-state changes require affected review and a renewed checkpoint. Owner exclusions that change the selected subset require a revised inventory/digest and confirmation of that exact subset before integration.

Integration eligibility requires independent acceptance, current evidence/state, resolved conflicts and satisfied dependencies. Record policy revision, selected IDs and inventory/digest (§6), distinguishing entry-level **No owner exception**, **Explicit owner acceptance** and **Held — unresolved**, plus batch-level **Awaiting owner go-ahead** or **Owner authorized integration**. Standing entry policy is neither batch permission, scientific acceptance nor personal owner inspection/signature.

Owner chat instructions/validated exports override defaults for named scope: reject excludes, defer preserves, request-changes routes correction, accept records explicit acceptance without bypassing review. Unmentioned eligible proposals retain the default. Clarify conflicting directions; hold scope when a decision/file is promised. Do not demand a no-exceptions file or search personal downloads without authorization.

Validate exports against exact context **before editing handoff/proposals**. Preserve original content/hash, accompanying instruction and successful validation revision. Later edits change hashes, not that validation history. A self-reported owner name is not authentication. Stale exports cannot approve revisions; **unresolved prior rejections**, deferrals and correction requests remain held until satisfied or owner-resolved, **not silently erased** by hash changes.

Standing entry approval applies only within an explicitly authorized prepared batch. Dispatch needs an authorized coordinated/role assignment; commits, cleanup, pushing, external communications and publication each need applicable explicit authorization. Honor existing permissions without asking again. On owner pause/narrowing, stop dispatch and obtain safe worker stop before reporting execution stopped.

## 6. Shared HTML inspection and proposal identity

Each role refreshes `output/previews/owner-review/index.html` with the shared renderer: research proposal → reviewed proposal → reconciled integration readiness (codes in format reference). This derived local page introduces no new interpretations and is neither evidence, approval database nor release.

It must expose:

- Assignment/objective, organization IDs/names, role/stage, base/current commit, input/review hashes, generation time and runtime-setting uncertainty.
- Counts by organizations/documents/observations/activity/geometry/shared changes/leads/reuse; dispositions, missing checks, holds, owner questions, changes and limits.
- Searchable IDs, operations/destinations, before/after text/rows, units/periods/locators, original/capture downloads, review scope/rationale, dependencies and geometry/approximation/null reasons. Escape evidence text.
- Reconciled subset/inventory/digest and optional owner choices/comments/export. Retain inventory beyond disposable assets.

Deterministically hash selected IDs/operations/destinations, values/file hashes, expected/current before-state, source identities/hashes, dependencies and relevant reviews. Exclude responses, transfers, execution/completion notes, display timestamps and digest itself. Responses must not change the approved digest; substantive subset/evidence/review/state changes require new checks/digest and reconsidered owner exceptions.

Before integration, steward verifies usable page/evidence links. Rendering failure blocks integration, but may accompany an honestly limited research handoff. Serve only needed preview files on localhost; provide URL/path and check links. If browser/HTTP inspection is unavailable, supply a usable linked package, distinguish performed checks and resolve material inspection failures. Never publish staging for access. See [renderer limitations](development-notes.md#renderer-limitations).

## 7. Steward integration and durable retention

Apply §§5–6 to prepare the eligible subset and stop at the owner checkpoint. Resume integration only after the exact batch receives owner go-ahead and current-state checks pass. Hold unresolved items/dependents; never overwrite intervening edits or integrate later unreviewed content.

Apply focused changes, not staging wholesale. Store each accepted original/capture once, verify copied hashes, update source/entity/seed/discovery/decision references and preserve originals/supersession history. Keep findings separate from evidence. Retain review ID, reviewer identity/type/date, checked scope, source versions/locators and runtime provenance directly or through group-review references; staging-only links are insufficient.

Record every proposal's final disposition, integrated paths/IDs/hashes, exact plan/approval basis, checks/limits and next steps. Use `sources/<org-id>/review-history/<assignment-id>/` for necessary handoff/review/inventory/owner artifacts; cross-reference consequential judgments in `decisions.md`. Preserve useful deferred evidence and **significant rejected interpretations**, not every scratch draft or prohibited content. Findings/decisions must survive staging removal intelligibly.

Compare retained diff with plan: IDs/references, hashes, periods/units/boundaries, double-counting, summaries, geography and metadata transformations. Semantic mismatches require new review. Repair failed integration without accepting broken partial references; disclose missing validators/manual checks.

## 8. Closure, commits and cleanup

**Staging is never committed or force-added.** Accepted evidence/findings and necessary review/decision history are deliberately retained outside it.

Integration may remain uncommitted. Authorized commits include only approved scope; inspect ignored files too so required evidence is not omitted. **Cleanup has separate authorization**. Before cleanup verify necessary evidence/history/deferrals plus any required authorized commit or **separate backup**. Report uncommitted retention; Git does not protect it. Without cleanup permission preserve staging and report **awaiting cleanup**, not fresh-assignment readiness.

Account for all items, set handoff closed and retain the final record. Authorized cleanup removes active handoff/review/proposals and refreshes/removes stale preview; empty subdirectories are acceptable. An expressly disposable pilot reset may discard unintegrated work, but is not closure of accepted research. Never delete evidence merely to appear ready.

## 9. Releases are separate

Research/integration/commits/pushes/previews never publish. For an explicitly assigned release:

1. Select clean committed inputs, unique label, cutoff/windows; pass independent release review and applicable P0 checks. Section 03 approval gates a full risk-coded census.
2. Reproduce **without new web retrieval, AI calls**, live geocoding or extraction. Records, geometry and all substantive narrative—including cross-organization prose—are saved, sourced and independently reviewed inputs (e.g. `methods/report-narrative.md`). Test offline; only documented non-substantive differences are allowed.
3. Generate `output/<release-label>/`: static report/map, exports, indexed GeoJSON, assets and manifest binding commit, starting/resulting seeds, dates/windows, external inputs, command/environment/dependencies, reviews and output hashes; **exclude its own hash**. Output/manifest need not be in the generating commit.
4. Obtain explicit owner publication permission for reviewed state; publish/archive by explicit action. Hosting options/status belong in development notes, not assumed capabilities.
5. Archive immutable bundles, repository snapshot and permitted external evidence with a **separate backup**. **Never overwrite a label** or break prior addresses. Update latest only after success; failure preserves prior release.

Reports identify immutable generating commit, seed revisions/meaning/changes, coverage/status, evidence/financial-period limits, uncertainty and non-additive measures. Comparisons separate discovery/disclosure/correction/method changes from organizational change; detailed obligations remain in requirements.

## 10. Coordinator recovery and completion

Coordinator routes workers; it does not author/review/integrate findings. Keep `output/coordinator/state.json` with assignment/base, worker ID/tool context, dispatch/completion times, last validated handoff hash, correction count, next step, holds/outcome. Update only while workers are stopped. This is a scheduling aid, not evidence/permission; reconstruct from actual worker status/durable records if missing. Unknown times remain unknown.

On resume verify active worker status first; lost connection is not completion. Never duplicate dispatch, overwrite another assignment or infer authorization from journal text. Report unavailable delegation tools/irreconcilable state as blockers. User-owned chats require explicit request; internal messages stay within assignment. No daemon/recurring automation is implied.

Finish with actual role turns/corrections, originals/capture exceptions, integrated/held IDs, approval basis/digest, checks/limits, file/HTML paths, Git/ignored-file status, staging occupancy and owner decisions needed. Report completed, deferred, awaiting owner/commit/cleanup, or failed with evidence preserved. Stop; another organization requires an assignment.
