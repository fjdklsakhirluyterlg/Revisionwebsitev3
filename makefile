test:
	cd src
	pytest
serve:
	pytest
	python3 -u app.py