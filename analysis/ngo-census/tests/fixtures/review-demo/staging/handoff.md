# Demo handoff

SYNTHETIC TEST FIXTURE. Not reviewed census data.

<!-- census-record -->
```json
{
  "schema_version": 1,
  "synthetic": true,
  "assignment": "Demo review — one synthetic assignment",
  "objective": "Exercise document, row, text and geometry inspection without changing real research.",
  "base_commit": "synthetic-fixture-not-a-git-commit",
  "researcher_id": "fixture-researcher",
  "organizations": [
    {
      "org_id": "org-demo",
      "name": "Demo Watershed Association"
    },
    {
      "org_id": "org-next",
      "name": "Demo Estuary Initiative"
    }
  ],
  "current_role": "steward",
  "view_stage": "reviewed",
  "from_role": "reviewer",
  "to_role": "steward",
  "sources": [
    {
      "source_id": "src-demo-2023",
      "title": "Fictional 2023 filing",
      "publisher": "Synthetic fixture publisher",
      "period": "2023",
      "path": "staging/proposed-changes/sources/org-demo/990/2023-demo.txt",
      "sha256": "f9728138ff4c0ea5e12736b02f02146b95cb0f17205aef8fb2ebd24484683cbb",
      "url": "https://example.invalid/synthetic-filing",
      "locator": "synthetic lines 2–6",
      "origin_check": "Synthetic check only; not an authentic public filing"
    }
  ],
  "changes": [
    {
      "change_id": "change-01",
      "org_id": "org-demo",
      "kind": "document",
      "target": "sources/org-demo/990/2023-demo.txt",
      "before": null,
      "after_file": "staging/proposed-changes/sources/org-demo/990/2023-demo.txt",
      "submission_type": "finding",
      "summary": "Retain one synthetic filing",
      "source_ids": [
        "src-demo-2023"
      ]
    },
    {
      "change_id": "change-02",
      "org_id": "org-demo",
      "kind": "csv-row",
      "target": "sources/org-demo/financial-history.csv",
      "key": {
        "org_id": "org-demo",
        "metric": "revenue",
        "fiscal_period": "2023"
      },
      "before": null,
      "after": {
        "org_id": "org-demo",
        "metric": "revenue",
        "fiscal_period": "2023",
        "amount": "1200",
        "currency": "USD",
        "source_id": "src-demo-2023",
        "locator": "synthetic line 4"
      },
      "submission_type": "finding",
      "summary": "Add source-backed 2023 revenue observation (synthetic)",
      "source_ids": [
        "src-demo-2023"
      ],
      "depends_on": [
        "change-01"
      ]
    },
    {
      "change_id": "change-03",
      "org_id": "org-demo",
      "kind": "text",
      "target": "sources/org-demo/activities.md",
      "before": "# Demo program\n\nPreviously reviewed synthetic activity description.\n",
      "after_file": "staging/proposed-changes/sources/org-demo/activities.md",
      "submission_type": "finding",
      "summary": "Clarify program geography before acceptance",
      "source_ids": [
        "src-demo-2023"
      ]
    },
    {
      "change_id": "change-04",
      "org_id": "org-demo",
      "kind": "geojson",
      "target": "sources/org-demo/footprint.geojson",
      "before": null,
      "after_file": "staging/proposed-changes/sources/org-demo/footprint.geojson",
      "submission_type": "finding",
      "summary": "Defer unsubstantiated synthetic footprint",
      "source_ids": [
        "src-demo-2023"
      ]
    },
    {
      "change_id": "change-05",
      "org_id": "org-next",
      "kind": "csv-row",
      "target": "sources/entities.csv",
      "key": {
        "org_id": "org-next"
      },
      "before": null,
      "after": {
        "org_id": "org-next",
        "name": "Demo Estuary Initiative",
        "status": "pending"
      },
      "submission_type": "lead",
      "summary": "Keep a possible partner as a follow-up lead, not a verified finding",
      "source_ids": [
        "src-demo-2023"
      ]
    },
    {
      "change_id": "change-06",
      "org_id": "org-demo",
      "kind": "csv-row",
      "target": "sources/org-demo/financial-history.csv",
      "key": {
        "org_id": "org-demo",
        "metric": "attributed-expenditure",
        "fiscal_period": "2023"
      },
      "before": null,
      "after": {
        "org_id": "org-demo",
        "metric": "attributed-expenditure",
        "fiscal_period": "2023",
        "amount": "1200",
        "currency": "USD",
        "source_id": "src-demo-2023",
        "locator": "unsupported allocation — deliberate test error"
      },
      "submission_type": "finding",
      "summary": "Reject unsupported allocation of all revenue to steelhead work",
      "source_ids": [
        "src-demo-2023"
      ]
    }
  ],
  "integration_ids": [
    "change-01",
    "change-02",
    "change-05"
  ],
  "execution_notes": [
    {
      "role": "researcher",
      "session_id": "fixture-researcher",
      "model_requested": "synthetic/no actual agent",
      "model_actual": "not run",
      "reasoning_effort_requested": "medium",
      "reasoning_effort_actual": "not run"
    }
  ],
  "reused_count": 1,
  "gaps": [
    "No real filings or source checks were performed.",
    "Program geography and the footprint remain unresolved."
  ],
  "owner_questions": [
    "Approve only the independently accepted synthetic subset for testing; this is not an actual authorization request."
  ]
}
```
