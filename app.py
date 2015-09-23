import os
import config
import logging
from task_handler import CodeTask
import subprocess


from flask import Flask,request,render_template,url_for,jsonify

logging.basicConfig(level=logging.DEBUG)

app=Flask(__name__)

app.secret = config.KEY

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/compile',methods=['GET','POST'])
def compile():
	source_code=request.form["edit"]
	std_input = request.form["std-input"]
	logging.debug("This is the source code :: "+source_code)
	
	if source_code == '':
		return render_template('error.html')
	
	new_task=CodeTask(1)
	output_result = new_task.compile(request.form['filename_field'],source_code,std_input)
	logging.debug(request.form['std-input'])
	logging.debug('Code ran successfully with output: '+output_result)
	logging.debug('Filename field is  :'+request.form['filename_field'])
	
	return render_template('output.html',output=output_result)
	

@app.route('/test')
def test():
	subprocess.Popen(['gcc',os.path.abspath('temp.c')])
	output = subprocess.Popen([os.path.abspath('a.out')],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	#logging.debug(output.stdout.read())
	return render_template('error.html',output=output.stdout.read())

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
	