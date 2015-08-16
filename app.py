import os
import config
import logging
from task_handler import CodeTask

from flask import Flask,request,render_template,url_for,jsonify

logging.basicConfig(level=logging.DEBUG)

app=Flask(__name__)

app.secret = config.KEY

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/compile',methods=['POST'])
def compile():
	valu=request.form["edit"]

	logging.debug(valu)
	
	if valu == '':
		return render_template('error.html')
	new_task=CodeTask(2)
	output_result = new_task.compile(request.form['filename_field'],valu)
	
	logging.debug('Code ran successfully with output: '+output_result)
	logging.debug(request.form['filename_field'])
	
	return render_template('output.html',output=output_result)
	

@app.route('/about_page')
def about_page():
	return "PyJudge is an Online compiler made by the Flask MicroFramework"

#--------NEED TO WORK ON--------------------------------------------------
@app.route('/login')
def login():
	return render_template('login.html')

if __name__=='__main__':
	port = int(os.environ.get("PORT", 3000))
	app.run(host='0.0.0.0', port=port,debug=True)
	