#!/bin/bash

satisfy_dependencies() {
	source `which virtualenvwrapper.sh`
	mkvirtualenv codincloud
	pip install -r ./CodinCloud/requirements.txt
}

if [ -z $VIRTUAL_ENV ]; then
	echo -e "Preparing your CodinCloud Environment...\n"
	satisfy_dependencies
fi

python wsgi.py $1