test:
	pytest
serve:
	flask run --host=0.0.0.0 --port=5090
serve-dev:
	pytest
	python3 -u app.py