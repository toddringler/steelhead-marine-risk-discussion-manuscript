# Steelhead marine risk discussion manuscript

*Are We Adequately Accounting for Marine Risk in Steelhead Conservation?*

A modular scientific discussion paper examining whether conservation adequately accounts for marine risk. This is an open hypothesis: the scaffold contains no scientific findings or references.

## Repository structure

```text
main.tex                 Manuscript entry point
preamble.tex             Shared packages and formatting
references.bib           Verified bibliography (initially empty)
.latexmkrc               pdfLaTeX/Biber build configuration
platexmkrc               TeXShop override for its pdflatexmk engine
AGENTS.md                Scientific and editing guidance
sections/                Twelve numbered manuscript sections
figures/
  lifecycle/
  risk/
  conservation/
  framework/
tables/
  life_stage_crosswalk.tex
  risk_taxonomy.tex
  conservation_effort.tex
appendices/
  risk_definitions.tex
  coding_methodology.tex
  supporting_evidence.tex
research/
  literature/
  working_notes/
  source_documents/
  coding_protocols/
data/
  raw/
  processed/
  metadata/
analysis/
  scripts/
  notebooks/
output/                  Generated PDF and auxiliary files (ignored)
test.tex                 Existing standalone build test, preserved
```

## Build

Install a TeX distribution such as TeX Live or MacTeX with pdfLaTeX, latexmk, Biber, and the packages listed in `preamble.tex` (including BibLaTeX, Latin Modern, booktabs, tabularx, longtable, hyperref, and cleveref).

Run from the repository root:

```sh
latexmk -pdf main.tex
```

The result is `output/main.pdf`. Latexmk manages repeat LaTeX passes and invokes Biber when bibliography processing is needed. The initially empty bibliography may produce an empty-bibliography warning; no references should be invented to suppress it. Add verified entries to `references.bib` and cite them with `\textcite{key}` or `\parencite{key}`.

To remove auxiliary files while retaining the PDF:

```sh
latexmk -c main.tex
```

To remove all build products, including the PDF:

```sh
latexmk -C main.tex
```

## VS Code / LaTeX Workshop

Open this repository folder in VS Code. The workspace settings in `.vscode/settings.json` select latexmk with pdfLaTeX and Biber, enable SyncTeX, and tell the PDF viewer to use `output/`. With `main.tex` or a section file active, run **LaTeX Workshop: Build LaTeX project** (Option-Command-B on macOS).

The settings force the configured recipe because Workshop otherwise interprets the TeXShop `TS-program = pdflatexmk` comment as an executable and fails with `spawn pdflatexmk ENOENT`. The comment remains available for TeXShop.

## TeXShop

Open `main.tex` in TeXShop and choose **Typeset** (Command-T). Its magic comment selects the bundled `pdflatexmk` engine, which runs latexmk and Biber as needed. If that engine is unavailable, activate `pdflatexmk.engine` from `~/Library/TeXShop/Engines/Inactive/Latexmk/` into `~/Library/TeXShop/Engines/` and restart TeXShop.

TeXShop's engine loads the project-specific `platexmkrc` after its bundled settings. This restores `.latexmkrc` so the PDF, log, auxiliary files, and SyncTeX file all go into `output/`. No change to global TeXShop preferences is needed. Root comments in the preamble, sections, appendices, and table files direct typesetting to `main.tex`.

TeXShop normally looks for its automatic PDF preview beside the source file ([TeXShop documentation](https://pages.uoregon.edu/koch/texshop/changes_3.html)). Open `output/main.pdf` explicitly in TeXShop to view the result; this configuration does not create a PDF copy in the repository root.

## Writing and research

Edit the numbered section files and appendices; `main.tex` includes each in order. Table files are comment-only placeholders until evidence-backed content is available; include them with, for example, `\input{tables/life_stage_crosswalk}` when ready. Store figures in the appropriate topical directory and include them with `\includegraphics`.

Keep raw data unchanged and document sources and transformations in `data/metadata/`. Keep research notes and coding protocols separate from manuscript prose. See `AGENTS.md` for citation standards and the requirement to examine counterevidence and alternative explanations.

Empty directories are tracked with `.gitkeep`. Build products, PDFs, Python caches, and temporary files are ignored; intentionally versioned source PDFs require an explicit exception to `.gitignore` and a permissions review.
