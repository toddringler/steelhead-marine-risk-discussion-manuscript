# Wild steelhead organization census

Identify, analyze and track NGO-like organizations whose work affects wild steelhead conservation across the Pacific Rim. Research retains actual public evidence and qualified findings; reports reproduce reviewed records rather than repeat web searches or AI judgments. Coverage is explicit, not presumed complete.

## Start here

Give the coordinator a permanent seed ID, research questions, assignment type (**first pass** or **research iteration**) and any custom time budget. Default is one organization and 30 research minutes; searches/documents are reported counts, not hard caps. A coordinated assignment authorizes sequential role dispatch, not commits, cleanup or publication. Existing staging requires resumption/closure, not overwriting.

| Document | Authority |
| --- | --- |
| [Requirements](requirements/Steelhead_Organization_Census_Requirements.md) | Census objectives, scientific safeguards, required outputs and acceptance criteria |
| [Workflow](workflow.md) | Single operating procedure: staging, serial handoffs, fresh review, corrections, owner exceptions, integration, retention, closure and release boundary |
| [Format reference](methods/staging-record-format.md) | Exact deliverable contents, canonical record fields, IDs, hashes, templates and commands |
| [Coordinator](requirements/coordinator-agent-instructions.md) | Scheduling, completion gates, routing, recovery and escalation |
| [Researcher](requirements/researcher-agent-instructions.md) | Evidence collection and deliverable checklist |
| [Reviewer](requirements/reviewer-agent-instructions.md) | Independent checks and dispositions |
| [Steward](requirements/steward-agent-instructions.md) | Eligible integration and retained-record validation |
| [Development notes](development-notes.md) | Prototype status, limitations, history and implementation options |
| [To-do list](TODO.md) | Pending improvements and later tightening pass |

Read repository `AGENTS.md` first. Scientific obligations belong in requirements, shared operating rules in workflow, syntax/field definitions in the format reference. Role checklists reference those homes. If documents conflict, apply current owner instructions and resolve the conflict explicitly rather than silently waiving evidence or review. Existing data is not automatically migrated by a documentation change.

## Directory map

All paths below are under `analysis/ngo-census/`. This census keeps retained originals and reviewed research together under `sources/`, an exception to the repository's general raw-data layout. Repository-root `output/` remains for the manuscript/LaTeX.

```text
analysis/ngo-census/
├── README.md, workflow.md, development-notes.md, TODO.md
├── requirements/                  # requirements and four role checklists
├── methods/                       # format reference, codebooks, agent-settings.json
├── input-data/seed-candidate-list.md
├── staging/                       # ignored; one active assignment
│   ├── handoff.md
│   ├── review.md
│   └── proposed-changes/          # only new/revised material and focused row proposals
├── sources/
│   ├── entities.csv              # canonical identity and screening
│   ├── index.csv                 # retained source-file provenance
│   └── <org-id>/                  # permanent candidate-list ID
│       ├── org-summary.md
│       ├── activities.md
│       ├── relationships.md
│       ├── financial-data.md
│       ├── research-status.md
│       ├── research-summary.md
│       ├── footprint.geojson
│       ├── 990/, t3010/, program-reports/, web-captures/
│       └── review-history/       # necessary durable reviews/decisions/inventories
├── discovery-log.csv, decisions.md
├── scripts/, templates/, tests/
└── output/                       # ignored generated material and local journals
    ├── previews/owner-review/
    ├── coordinator/
    └── <release-label>/
```

Create records when needed, without misleading empty evidence/profile placeholders. A completed first pass must address every organization deliverable substantively or document investigated gaps; iterations stage only relevant changes. Permanent IDs survive name changes. Discovery alone is a lead, not inclusion. Shared financial CSV/workbook exports are generated derivatives, not second authoritative records.

## Inspect work

The researcher, reviewer and steward successively refresh `output/previews/owner-review/index.html`. [Render/serve commands](methods/staging-record-format.md#commands) use a localhost server rooted only in the preview directory. The HTML is disposable output; authoritative proposals/review remain in staging and accepted findings/history in retained files.

The owner can inspect any stage and optionally export decisions. Eligible reviewed integration uses standing owner approval; no routine owner click or decision file is required. See [owner review by exception](workflow.md#5-owner-review-by-exception). Unresolved evidence/review issues and owner exceptions still hold affected proposals.

Original public documents or faithful web captures are the default; summaries remain separate. Permissions, capture exceptions and excluded personal/donor material must be documented. Before any authorized cleanup, necessary evidence, review history and decisions are retained outside ignored staging. Commit, cleanup, push and publication permissions remain distinct. See [workflow](workflow.md).

No continuously running service is installed. The current tools support staging review, not a completed public report/release system; see [implementation status](development-notes.md#implementation-status).
