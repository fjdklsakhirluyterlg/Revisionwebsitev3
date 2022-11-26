test:
	pytest
serve:
	python3 -u app.py
serve-dev:
	pytest
	python3 -u app.py