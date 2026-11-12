# Scientific purpose

This repository supports the discussion paper *Are We Adequately Accounting for Marine Risk in Steelhead Conservation?*

Treat inadequate accounting of marine risk as a hypothesis to examine, not a predetermined conclusion. Evaluate alternative explanations, counterevidence, uncertainty, and the limits of inference. Distinguish biological importance from management controllability and conservation effort from conservation outcomes. Do not invent findings, data, references, or quantitative estimates.

# Manuscript organization

`main.tex` assembles the twelve numbered files in `sections/`, the bibliography, and three appendices. Shared packages and formatting belong in `preamble.tex`; references belong in `references.bib`. Reusable table fragments belong in `tables/` and are included from the relevant section when ready. Organize figures by topic under `figures/`.

Keep literature, working notes, source documents, and coding protocols under `research/`. Preserve original data in `data/raw/`; document provenance, units, definitions, transformations, and uncertainty in `data/metadata/`. Put derived data in `data/processed/` and reproducible code in `analysis/`. Do not redistribute restricted source documents or sensitive data without authorization.

# Citation and evidence standards

Use BibLaTeX with Biber and author-year citations (`\textcite{key}` or `\parencite{key}`). Verify bibliographic metadata and that each source supports the associated claim; prefer original research and authoritative primary documents. Identify interpretation and hypotheses explicitly. Record population, geography, life stage, time period, and methodological limits where relevant. Mark missing evidence with a clear TODO comment rather than a fabricated citation. Keep `references.bib` empty until verified sources are added.

# Editing and validation

Review existing files before editing. Preserve modular organization and use descriptive labels for figures and tables. Build from the repository root with `latexmk -pdf main.tex`; generated files belong in `output/` and must remain untracked. An empty bibliography warning is expected until sources and citations are added. Report compilation failures and unresolved citations. Do not commit changes unless the user authorizes a commit.

# NGO census output exception
All NGO census work stays under `analysis/ngo-census/`. Its generated previews, reports, assets and coordinator journals belong in ignored `analysis/ngo-census/output/`, not the repository-root manuscript `output/` directory.
