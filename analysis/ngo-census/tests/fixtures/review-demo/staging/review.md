# Demo independent review

SYNTHETIC TEST FIXTURE. Not reviewed census data.

<!-- census-record -->
```json
{
  "schema_version": 1,
  "assignment": "Demo review — one synthetic assignment",
  "reviewer_id": "fixture-reviewer",
  "reviewer_type": "agent",
  "execution_notes": [
    {
      "role": "reviewer",
      "model_actual": "synthetic/not run",
      "reasoning_effort_actual": "not run"
    }
  ],
  "items": [
    {
      "change_id": "change-01",
      "proposal_hash": "af4ca75d8fc2d3723915ee598c7fac94ce920dd8156aaa0c3f85a884721dd44f",
      "disposition": "accepted",
      "scope": "listed proposal only",
      "reviewed_date": "2026-11-11",
      "rationale": "Source identity and bytes checked for this synthetic fixture.",
      "review_id": "fixture-review-01"
    },
    {
      "change_id": "change-02",
      "proposal_hash": "9598be1696305122aaf16e22119c75b86a934dd41fac8edd6f7ebfe854c6aae9",
      "disposition": "accepted",
      "scope": "listed proposal only",
      "reviewed_date": "2026-11-11",
      "rationale": "Revenue agrees with synthetic line 4; period and currency preserved.",
      "review_id": "fixture-review-02"
    },
    {
      "change_id": "change-03",
      "proposal_hash": "8fc068e6196a2f1855ad7f85375f6ae4c5a28639d218dded6720daf967eacb9d",
      "disposition": "correction requested",
      "scope": "listed proposal only",
      "reviewed_date": "2026-11-11",
      "rationale": "State the specific program geography rather than broad river language.",
      "review_id": "fixture-review-03"
    },
    {
      "change_id": "change-04",
      "proposal_hash": "87dd8ee1b871c757cac24e46659ce7ee1a6924589f05740cba15b1a9ad96a055",
      "disposition": "deferred",
      "scope": "listed proposal only",
      "reviewed_date": "2026-11-11",
      "rationale": "Source does not support this exact extent; preserve as a deferred question.",
      "review_id": "fixture-review-04"
    },
    {
      "change_id": "change-05",
      "proposal_hash": "147dbb42cc2c90268b7951334ec95633ebd5b95d49b29957b27a9f11762d122d",
      "disposition": "accepted",
      "scope": "lead only",
      "reviewed_date": "2026-11-11",
      "rationale": "Retain as an unverified follow-up lead only.",
      "review_id": "fixture-review-05"
    },
    {
      "change_id": "change-06",
      "proposal_hash": "2897479214cfc49ef7791446ded38ec7b98fdd2a925fa8e9ade5449c2e6438b5",
      "disposition": "rejected",
      "scope": "listed proposal only",
      "reviewed_date": "2026-11-11",
      "rationale": "Revenue is not evidence of attributable steelhead expenditure.",
      "review_id": "fixture-review-06"
    }
  ]
}
```
