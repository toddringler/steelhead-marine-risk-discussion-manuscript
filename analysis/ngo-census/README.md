# NGO census research workflow

This directory holds the implementation notes for the wild steelhead organization census. The [requirements document](requirements/Steelhead_Organization_Census_Requirements.md) defines the required behavior and scientific safeguards. This README explains where research lives and how to retain and reuse it. The layout below is the intended organization; files and directories are created when needed, not all at once. A database is not required.

## Directory layout

```text
analysis/ngo-census/
├── README.md
├── requirements/
│   └── Steelhead_Organization_Census_Requirements.md
├── data/
│   └── seed-candidate-list.md
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
├── discovery-log.csv
└── decisions.md
```

Organization names and document filenames in this tree illustrate placement; they do not assert that those filings or reports have been obtained. Add other source categories, such as `t3010/`, when appropriate. Avoid empty files and placeholder records that could be mistaken for completed research.

For this census, `sources/` is the self-contained home for both retained original public documents and reviewed research records. This is the census-specific exception to the repository's general `data/raw/` and `data/metadata/` placement conventions. Originals and research interpretation remain visibly separate by filename and subdirectory. Generated reports and exports still go under the repository-root `output/` directory and remain untracked.

## File roles

| File or directory | Purpose |
| --- | --- |
| `data/seed-candidate-list.md` | Cumulative candidate names and permanent assigned IDs; initializes discovery without implying eligibility |
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

## Permanent organization IDs

Use the assigned ID from the [seed list](data/seed-candidate-list.md), such as `org-wildfishcon`, for the organization directory and cross-references. IDs are permanent even after a name change. Never reassign them or regenerate them from updated names.

Keep the seed list cumulative. Candidate status lives in `entities.csv`, not in the presence or absence of a seed entry. A duplicate retains its ID and points to the canonical entity; exclude it from duplicate counts. Programs have their own IDs and a parent reference where supported, without assuming legal independence.

## Sources and provenance

Here, checking a source's origin means confirming its publisher, organizational identity, and document identity. It does not verify every assertion in the document or every value extracted from it.

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

## Dated reports and releases

Reports are evidence snapshots published when useful, potentially several times in one year. They retain the observations' own fiscal periods and distinguish new research from actual organizational change. Section 03 of the discussion paper remains an open dependency for the full risk-coded census; discovery and preliminary profile preparation can proceed as described in the requirements.

Generate a published report from a clean committed state. The report identifies its generating commit and exact starting seed revision, links to saved GeoJSON, and states evidence cutoff, coverage, and financial-period limits. Manual review and drawing are retained inputs, not tasks to repeat when reproducing a report.

Use one release manifest for the release label, publication date, cutoff, seed references, generating commit, retained external inputs, reproduction command and environment, review, and output hashes. Archive the report, manifest, any required external evidence, and generating repository snapshot as immutable release assets or another durable archive. A repository link alone is not a backup. The completed manifest and report are generated after the source commit, so their hashes do not need to be embedded in that same commit.

Scripts and a runnable report command will be documented here when implemented. This README defines file conventions; it does not imply that the reporting system is already built.
