import os
import config
import logging
import time
from task_handler import CodeTask
import subprocess

from flask import Flask,request,render_template,url_for,jsonify

logging.basicConfig(level=logging.DEBUG)

app=Flask(__name__)

app.secret = config.KEY

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/compile')
def compile():
	filename = request.args.get('filename','',type=str)
	source_code = request.args.get('source_code','',type=str)
	stdin = request.args.get('stdin','',type=str)
	logging.debug('on app.py = '+str(len(stdin)))
	logging.debug('on app.py = '+stdin)
	new_task=CodeTask(1)
	if(len(stdin)==0):
		output_result = new_task.compile(filename,source_code)
	else:
		output_result = new_task.compile(filename,source_code,stdin)
	logging.debug(output_result)
	time.sleep(0.5)
	return jsonify(result=output_result.replace('\n','<br>'))

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/signup')
def signup():
	return render_template('signup.html')

@app.route('/login')
def login():
	return render_template('login.html')

if __name__=='__main__':
	app.run()
