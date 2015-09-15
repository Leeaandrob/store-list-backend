#!/bin/bash
NAME="storelist" #Name app
DJANGODIR=/home/webapps/storelist/current/storelist/
SOCKFILE=/home/webapps/storelist/run/gunicorn.sock  # we will communicte using
DJANGO_SETTINGS_MODULE=storelist.settings_production             # which settings file should
DJANGO_WSGI_MODULE=storelist.wsgi                     # WSGI module name

cd $DJANGODIR
source ../../../bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

uwsgi --socket :8000 --module ${DJANGO_WSGI_MODULE}
exit $?
