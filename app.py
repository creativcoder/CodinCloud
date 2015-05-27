import os
import config
from task_handler import CodeTask

from flask import Flask,request,render_template,url_for,jsonify

app=Flask(__name__)

app.secret = config.KEY

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/compile',methods=['POST'])
def compile():
	valu=request.form["edit"]
	print valu
	if valu == '':
		return render_template('error.html')
	new_task=CodeTask(2)
	output = new_task.compile(request.form['filename_field'],valu)
	return render_template('output.html',output=output)
	#return request.form['filename_field']

@app.route('/about_page')
def about_page():
	return "PyJudge is an Online compiler made by the Flask MicroFramework"

#--------NEED TO WORK ON--------------------------------------------------
@app.route('/login')
def login():
	return render_template('login.html')
	#return "Your have successfully logged in"

if __name__=='__main__':
	port = int(os.environ.get("PORT", 3000))
	app.run(host='0.0.0.0', port=port,debug=True)
	