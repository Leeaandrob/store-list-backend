clean:
	find . -name "*.pyc" -exec rm -rf {} \;

run: clean
	pyhton manage.py runserver --settings=storelist.settings_local

shell: clean
	python manage.py shell --settings=storelist.settings_local

migrations: clean
	python manage.py makemigrations --settings=storelist.settings_local

migrate: clean
	python manage.py migrate --settings=storelist.settings_local

test: clean
	python manage.py test --settings=storelist.settings_tests
