# Provisional staging records and review renderer

This pilot supplies a shared HTML template, a read-only renderer, starter records, synthetic examples, and tests. It implements the staging review page, not the census release report or automated integration. The format is provisional: evaluate it with a few small assignments before expanding it.

## Run the synthetic example

From the repository root, using Python 3.10 or newer (no additional packages):

```sh
python3 analysis/ngo-census/scripts/render-staging-review.py --census-root analysis/ngo-census/tests/fixtures/review-demo --output output/ngo-census/previews/synthetic-demo --strict
python3 -m unittest discover -s analysis/ngo-census/tests -v
python3 -m http.server 8765 --bind 127.0.0.1
```

Open `http://127.0.0.1:8765/output/ngo-census/previews/synthetic-demo/index.html`. The example contains fictional organizations, documents, money, and geometry. Its accepted labels simulate review; they are not actual verified research or owner authorization. The fixture stays outside live staging. Stop the local server when finished.

For a real active assignment, run:

```sh
python3 analysis/ngo-census/scripts/render-staging-review.py --strict
```

The default output is repository-root `output/ngo-census/previews/owner-review/index.html`. Serve and open that path over localhost. No active handoff produces a no-active-assignment page. A malformed record replaces the page with an unavailable notice. Strict mode exits unsuccessfully for validation errors; an output page alone does not establish readiness. Generated HTML, JSON inventories, and copied evidence assets remain untracked.

## Structured records within readable Markdown

Start with [handoff template](../templates/staging/handoff.md) and [review template](../templates/staging/review.md). Each file contains exactly one `<!-- census-record -->` marker followed by a fenced JSON block, with `schema_version` equal to `1`. Put readable transfer history, correction history, limitations, and supporting explanations outside that block. The renderer reads the structured block; it does not interpret prose as a field value. Keep the two representations consistent. Do not activate unfinished templates.

The [complete synthetic handoff](../tests/fixtures/review-demo/staging/handoff.md) and [review](../tests/fixtures/review-demo/staging/review.md) illustrate each supported change type. JSON is embedded in the existing Markdown files to avoid another maintained database or parallel staging inventory.

### Handoff fields

| Field | Meaning |
| --- | --- |
| `assignment`, `objective` | Assignment identity and bounded purpose |
| `base_commit` | Full starting Git commit hash; the synthetic fixture alone uses a non-Git placeholder |
| `researcher_id` | Author/session identity, distinct from the independent reviewer |
| `organizations` | Objects containing permanent `org_id` and display `name` |
| `current_role` | `researcher`, `reviewer`, `steward`, `owner`, or `closed` |
| `from_role`, `to_role` | Addressed transfer; preserve date, reason, expected action, revision/hashes, and history in the handoff |
| `view_stage` | `research`, `reviewed`, or `signoff`; a display request, not permission to act |
| `sources` | Source objects described below |
| `changes` | Individually reviewable proposals described below |
| `integration_ids` | Explicit selected change IDs; empty until an integration subset is chosen |
| `execution_notes` | Append role/session, configuration revision, requested/actual model and effort, changes and reasons; mark unavailable settings unknown |
| `gaps`, `owner_questions` | Lists of unresolved limitations and decisions |
| `reused_count` | Optional count of unchanged previously reviewed observations reused |
| `owner_approval` | Optional recorded owner statement with `digest` and `change_ids`; retain who approved, when, and the permissions granted in handoff prose |

The renderer displays role/stage metadata but does not enforce agent scheduling, confirm an addressed transfer, or identify who edited a file. The role instructions remain binding. Only the steward requests signoff after reconciling the selected subset.

Each source requires `source_id`, `title`, `path`, and the exact retained `sha256`. Also record public `publisher`, `url`, `period`, specific `locator`, and `origin_check` status as applicable. Paths are relative to the census directory and point into `sources/` or `staging/proposed-changes/`. Hash agreement proves file identity, not publisher authenticity, eligibility, or factual accuracy. Accepted retained source-index entries still require the provenance fields specified in the README; the handoff is not a replacement for that index.

### Change fields

Every change includes a unique safe lowercase `change_id`, `org_id`, `kind`, retained destination `target`, concise `summary`, `submission_type` (`finding` or `lead`), `source_ids`, `depends_on`, and expected `before`. Destinations are relative to the census directory. Stage only new material under `staging/proposed-changes/`; never edit retained sources through this renderer.

| Kind | Before and proposed content |
| --- | --- |
| `csv-row` | `key` identifies one row using string-valued fields; `before` and `after` are complete string-valued row objects or null for absence/deletion. The proposed row must match its key. |
| `text` | `before` is the exact previous UTF-8 text, or null if absent; `after_file` identifies the staged proposed text. The page shows before, after, and a difference view. |
| `document` | `before` is the previous SHA-256, or null if absent; `after_file` points to the staged document. New original evidence normally gets a distinct destination rather than replacing earlier evidence. |
| `geojson` | Same file/hash arrangement as documents; requires a FeatureCollection with Polygon, MultiPolygon, or null feature geometry. Coordinates, bounds, and ring closure are checked. |

`depends_on` lists required proposals, such as the retained document and source-index entry supporting a financial row. The selected subset must contain its dependencies. Declare them completely: the renderer cannot infer missing scientific or record dependencies. It supports maintained destinations under `sources/`, `input-data/`, `methods/`, and the census `decisions.md` and `discovery-log.csv` files. Other operations need an explicit format revision, not a workaround.

Leads may propose candidate/discovery records, not accepted financial observations, activities, or footprints. Accepting a lead requires the review scope `lead only`; the page keeps these separate from accepted findings.

GeoJSON inspection in this first version provides raw files, bounding coordinates, and notes. It is not an interactive map and does not validate full polygon topology, ecological validity, or the evidential extent of influence. Those checks remain reviewer work; a public release map is a later implementation step.

### Independent review fields

`review.md` includes the matching `assignment`, distinct `reviewer_id`, `reviewer_type` (`agent` or `human`), `execution_notes`, and `items`. Each item includes `change_id`, `proposal_hash`, `disposition` (`accepted`, `correction requested`, `deferred`, or `rejected`), `rationale`, `reviewed_date`, and `scope`; add a durable `review_id` for retained references.

After independently checking evidence and the exact proposal, obtain its `proposal_hash` from generated `preview.json` and record it with the disposition. Never copy a hash as a substitute for review. Hashes include supporting source identities/content and dependency proposals. A changed proposal, evidence file, or dependency invalidates the affected review. Regenerate, correct or re-review, and record the new hash only after checking the revised content. Preserve correction history in the Markdown.

Append reviewer execution notes both to the handoff and review, as required by the role instructions. Preserve retained group-review references during eventual integration.

## Owner approval and integration boundary

The steward selects independently accepted proposals in `integration_ids`, renders the page, and checks all displayed errors, evidence links, destination before-values, details, and review scopes. The renderer calculates `approval_digest` and `approval_inventory` in `preview.json`. Copy the exact inventory and digest into a labeled handoff section before requesting approval so they survive deletion of generated output.

The digest binds the base commit, selected changes, expected/current before-values, proposed content, source hashes, dependencies, and relevant review records. It excludes the owner response, role transfers, execution/completion notes, and display timestamps. Changing the selected substance requires a new digest and renewed approval; recording approval does not itself change the approved digest. The page separately exposes hashes of the handoff and review files used for rendering.

Record the owner's actual response and permitted actions in the handoff. If using `owner_approval`, its digest and IDs must match the selected subset. The renderer checks consistency of the recorded statement only: it does not authenticate the owner or confer authorization. Integration, commits, staging cleanup, pushing, and publication retain their existing separate permission requirements. This tool performs none of them and never edits retained or staged inputs.

A signoff label is blocked when the selected subset lacks current acceptance, has missing dependencies, or has validation conflicts. Passing these automated checks is necessary but insufficient: scientific review and the steward's complete inspection still apply. The current Git hash is displayed, and retained destinations are compared to expected values; the renderer does not assert that the working tree is clean or identical to its starting commit.

## Testing limits

The synthetic tests exercise changed evidence, stale acceptance and approval, destination conflicts, missing dependencies, source/path isolation, escaping, independent identity, candidate leads, and basic geometry validation. They cannot prove research completeness, factual accuracy, actor independence, owner identity, or correct integration. Pilot the process with a small real assignment only after choosing the model settings and owner-approved scope. Do not treat the fixture as accepted research or place it in the seed list.

## Owner decision entry

Expand a proposal to enter accept, reject, defer, or request changes and an optional comment (required for requested changes). Enter your name, then select **Download my decisions**. All selected proposals are included, even those hidden by a search filter; unselected ones are omitted. Entries live only in the current page: download before refreshing/closing. Give the JSON file to the steward and instruct it to use your choices. No commit, cleanup, push, or publish permission is conveyed.

The export uses schema version 1, type `census-owner-decisions`, self-reported `owner_name`, UTC `exported_at`, a `context` snapshot (assignment, base commit, exact handoff/review hashes, proposal hash map and selected approval digest), and `decisions` containing `change_id`, `choice`, and `comment`. The download is a decision record, not authentication or a replacement for independent review.

Validate before updating staging:

```sh
python3 analysis/ngo-census/scripts/validate-owner-decisions.py /path/to/owner-decisions.json
```

For a synthetic export add `--census-root analysis/ngo-census/tests/fixtures/review-demo`. The validator reads only; it does not copy, import, apply, or authenticate choices. The steward preserves the owner-supplied original and hash in the handoff, plus the owner instruction and successful validation revision, then routes corrections or prepares the accepted subset under existing approval rules. Changed inputs make earlier exports stale. A disagreement remains visible in the original independent review; an owner choice must not erase it or bypass evidence requirements.
