test:
	pytest
serve:
	gunicorn app:app -w 4
serve-dev:
	pytest
	python3 -u app.py