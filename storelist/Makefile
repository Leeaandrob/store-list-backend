clean:
	find . -name "*.pyc" -exec rm -rf {} \;

user: clean
	python manage.py createsuperuser --settings=storelist.settings_local

run: clean
	python manage.py runserver --settings=storelist.settings_local

shell: clean
	python manage.py shell --settings=storelist.settings_local

migrations: clean
	python manage.py makemigrations --settings=storelist.settings_local

migrate: clean
	python manage.py migrate --settings=storelist.settings_local

test: clean
	python manage.py test --settings=storelist.settings_tests
