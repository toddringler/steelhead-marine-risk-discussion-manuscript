# Build with pdfLaTeX; latexmk invokes Biber for BibLaTeX as needed.
$pdf_mode = 1;
$out_dir = 'output';
$aux_dir = 'output';
@default_files = ('main.tex');
$pdflatex = 'pdflatex -interaction=nonstopmode -halt-on-error -file-line-error %O %S';
$biber = 'biber %O %B';
