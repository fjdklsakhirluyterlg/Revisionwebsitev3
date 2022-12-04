test:
	pytest
serve:
	gunicorn -w 4 'backends:create_app()' -b 0.0.0.0:5090
serve-dev:
	pytest
	python3 -u app.py