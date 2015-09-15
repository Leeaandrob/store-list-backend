#!/bin/bash
NAME="storelist" #Name app
DJANGODIR=/home/webapps/storelist/current/storelist/
SOCKFILE=/home/webapps/storelist/run/gunicorn.sock  # we will communicte using
NUM_WORKERS=3                                     # how many worker processes
DJANGO_SETTINGS_MODULE=storelist.settings_production             # which settings file should
DJANGO_WSGI_MODULE=storelist.wsgi                     # WSGI module name

# Activate the virtual environment
cd $DJANGODIR
source ../../../bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

TIMEOUT=120
# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do
# not use --daemon)
exec ../../../bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
	--name $NAME \
	--workers $NUM_WORKERS \
	--bind=unix:$SOCKFILE \
	--log-level=debug \
	--log-file=- \
	--timeout $TIMEOUT
