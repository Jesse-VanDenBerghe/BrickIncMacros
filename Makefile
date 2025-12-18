PYTHON := .venv/bin/python

dive:
	$(PYTHON) ./brickinc/dive.py

dive_hard:
	$(PYTHON) ./brickinc/dive_hard.py

test:
	$(PYTHON) ./test.py

.PHONY: dive dive_hard test