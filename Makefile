check:
	wget --spider -r -p -nd -nv -l 5 -o run1.log http://127.0.0.1:4000/
	grep -B1 'broken link!' run1.log
