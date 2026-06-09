all: primitives_of_action.pdf fundamental_constants.pdf universal_discovery_engine.pdf

primitives_of_action.pdf: primitives_of_action.tex references.bib
	pdflatex primitives_of_action.tex
	bibtex primitives_of_action
	pdflatex primitives_of_action.tex
	pdflatex primitives_of_action.tex

fundamental_constants.pdf: fundamental_constants.tex references.bib
	pdflatex fundamental_constants.tex
	bibtex fundamental_constants
	pdflatex fundamental_constants.tex
	pdflatex fundamental_constants.tex

universal_discovery_engine.pdf: universal_discovery_engine.tex references.bib
	pdflatex universal_discovery_engine.tex
	bibtex universal_discovery_engine
	pdflatex universal_discovery_engine.tex
	pdflatex universal_discovery_engine.tex

clean:
	rm -f *.aux *.log *.out *.bbl *.blg *.toc *.pdf

.PHONY: all clean
