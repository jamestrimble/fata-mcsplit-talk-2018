all : tables graphs scripts/clique_encoding.tex
	latexmk -pdf -pdflatex='pdflatex -interaction=nonstopmode %O %S' talk

TABLES =

GRAPHS = gen-graph-plain-cumulative.tex \
	 gen-graph-33ved-cumulative.tex gen-graph-sip-cumulative.tex \
		 gen-graph-plain-james-versus-cp-fc-nodes-scatter.tex \
		 gen-graph-plain-james-versus-cp-fc-runtimes-scatter.tex \
		 gen-graph-sip-james-versus-kdown-nodes-scatter.tex

tables : $(TABLES)

graphs : $(GRAPHS)

gen-graph-%.tex : graph-%.gnuplot
	gnuplot $<

scripts/clique_encoding.tex: scripts/make_clique_encoding.py
	python scripts/make_clique_encoding.py > scripts/clique_encoding.tex

clean :
	rm *.aux *.bbl *.blg *.fdb_latexmk *.fls *.log gen-graph* talk.pdf scripts/clique_encoding.tex
