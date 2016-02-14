#!/bin/bash

satisfy_dependencies() {
	source `which virtualenvwrapper.sh`
	mkvirtualenv codincloud
	pip install -r ./CodinCloud/requirements.txt
}

if [ -z $VIRTUAL_ENV ]; then
	satisfy_dependencies
fi

python wsgi.py $1