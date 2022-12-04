test:
	pytest
serve:
	gunicorn app:app -w 4 -bind:5090
serve-dev:
	pytest
	python3 -u app.py