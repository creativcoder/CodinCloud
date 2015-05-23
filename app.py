import os
import config

from flask import Flask,request,render_template,url_for,jsonify

app=Flask(__name__)

app.secret = config.KEY

@app.route('/')
def index():
	return render_template('index.html')

if __name__=='__main__':
	port = int(os.environ.get("PORT", 3000))
	app.run(host='0.0.0.0', port=port,debug=True)
	