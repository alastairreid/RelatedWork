check:
	wget --spider -r -p -nd -nv -l 5 -o run1.log http://127.0.0.1:4000/
	grep -B1 'broken link!' run1.log

RelatedWork.md: _scripts/expand.py
	_scripts/expand.py _papers/*.md _notes/*.md > $@

RelatedWork.html: RelatedWork.md
	pandoc $< -s -o $@

RelatedWork.epub: RelatedWork.md
	pandoc $< -s -o $@

# End
