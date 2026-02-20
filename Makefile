.PHONY: install run lint test clean

PYTHON ?= python3

install:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt

run:
	$(PYTHON) src/text_analytics_and_tree_structures.py

lint:
	$(PYTHON) -m ruff check src tests

test:
	$(PYTHON) -m unittest discover -s tests -v

clean:
	rm -rf report/generated
	rm -f figures/*.png
