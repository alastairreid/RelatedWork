check:
	wget --spider -r -p -nd -nv -l 5 -o run1.log http://127.0.0.1:4000/
	grep -B1 'broken link!' run1.log

# show papers that don't refer to a note
unnoted:
	grep -A1 '^notes:' _papers/*.md | grep 'md----'

RelatedWork.md: _scripts/expand.py
	_scripts/expand.py _papers/*.md _notes/*.md > $@

RelatedWork.html: RelatedWork.md
	pandoc $< -s -o $@

RelatedWork.epub: RelatedWork.md
	pandoc $< -s -o $@

RelatedWork.bib:
	_scripts/md2bib.py RelatedWork.bib _papers/*.md

showbib.pdf: RelatedWork.bib
	pdflatex showbib
	bibtex showbib
	pdflatex showbib

clean::
	$(RM) showbib.{aux,blg,bbl,dvi,log,out,pdf}
	${RM} RelatedWork.{bib,epub,html,md}
	${RM} _data/authors.yaml
	${RM} _data/backrefs.yaml


# End
