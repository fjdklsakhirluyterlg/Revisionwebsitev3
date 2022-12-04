test:
	pytest
serve:
	gunicorn app:app -b 127.0.0.1:5090
serve-dev:
	pytest
	python3 -u app.py