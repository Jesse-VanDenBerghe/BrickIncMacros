PYTHON := .venv/bin/python

dive:
	$(PYTHON) ./brickinc/dive.py

dive_hard:
	$(PYTHON) ./brickinc/dive_hard.py

path_of_truth:
	${PYTHON} ./brickinc/path_of_truth.py

test:
	$(PYTHON) ./test.py

.PHONY: dive dive_hard path_of_truth test

