SHELL := /bin/bash

setup:
	python -m venv .venv
	( \
       		 source .venv/bin/activate; \
		 pip install requests; \
	         pip install -r requirements.txt; \
	)
