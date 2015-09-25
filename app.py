import os
import time
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
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_user import login_required, UserManager, UserMixin, SQLAlchemyAdapter

class ConfigClass(object):
	# Flask Settings
	SECRET_KEY = os.getenv('FLASK_DEV_KEY','SAMPLE_INSECURE_KEY')
	SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI','sqlite:///basic.sqlite')
	# Flask-Mail Settings
	MAIL_USERNAME = os.getenv('MAIL_USERNAME','rsconceptx@gmail.com')
	MAIL_PASSWORD = os.getenv('MAIL_PASSWORD','Devilzz9688$')
	MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER','rsconceptx@gmail.com')
	MAIL_SERVER = os.getenv('MAIL_SERVER','smtp.gmail.com')
	MAIL_PORT = int(os.getenv('MAIL_PORT','465'))
	MAIL_USE_SSL = int(os.getenv('MAIL_USE_SSL',True))

	# Flask-User settings
	USER_APP_NAME = "AppName"

logging.basicConfig(level=logging.DEBUG)

app=Flask(__name__)
app.config.from_object(__name__+'.ConfigClass')

db = SQLAlchemy(app)
mail = Mail(app)

class User(db.Model,UserMixin):
	id = db.Column(db.Integer,primary_key=True)

	# User Authentication Information
	username = db.Column(db.String(50), nullable=False, unique=True)
	password = db.Column(db.String(255),nullable=False,server_default='')
	reset_password_token = db.Column(db.String(100),nullable=False,server_default='')

	#User email information
	email = db.Column(db.String(255),nullable=False,unique=True)
	confirmed_at = db.Column(db.DateTime())

	# User Information
	active = db.Column('is_active',db.Boolean(),nullable=False,server_default='0')

db.create_all()

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
	time.sleep(0.5)
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
	