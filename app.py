import os
import config
import logging
from task_handler import CodeTask
import subprocess

# import re

# from jinja2 import evalcontextfilter, Markup, escape

# _paragraph_re = re.compile(r'(?:\r\n|\r|\n){2,}')

# app = Flask(__name__)

# @app.template_filter()
# @evalcontextfilter
# def nl2br(eval_ctx, value):
#     result = u'\n\n'.join(u'<p>%s</p>' % p.replace('\n', '<br>\n') \
#         for p in _paragraph_re.split(escape(value)))
#     if eval_ctx.autoescape:
#         result = Markup(result)
#     return result



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
	
	return render_template('output.html',output=output_result.split('\n'))
	

@app.route('/test')
def test():
	
	#logging.debug(output.stdout.read())
	return render_template('output.html',output="jhg")

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
	port = int(os.environ.get("PORT", 3000))
	app.run(host='0.0.0.0', port=port,debug=True)
	