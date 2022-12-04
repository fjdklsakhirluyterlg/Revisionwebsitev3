test:
	pytest
serve:
	gunicorn app:app -k gevent --worker-connections 1000
serve-dev:
	pytest
	python3 -u app.py