import ConfigParser
import sqlite3
import bcrypt
from functools import wraps
from flask import Flask, render_template, url_for, request, redirect, flash, session, g
app = Flask(__name__)
db_location = 'var/test.db'
app.secret_key =  'supersecret'
		
valid_email = 'person@napier.ac.uk'
valid_pwhash = bcrypt.hashpw('secretpass', bcrypt.gensalt())

def check_auth(email, password):
	if(email == valid_email and
		valid_pwhash == bcrypt.hashpw(password.encode('utf-8'),
	valid_pwhash)):
		return True
	return False

def requires_login(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		status = session.get('logged_in', False)
		if not status:
			return redirect(url_for('.root'))
		return f(*args, **kwargs)
	return decorated

@app.route('/logout/')
def logout():
	session['logged_in'] = False
	return redirect(url_for('.root'))

@app.route("/secret/")
@requires_login
def secret():
	return render_template('login.html')

@app.route("/", methods=['GET', 'POST'])
def root():
	if request.method == 'POST':
		user = request.form['email']
		pw = request.form['password']

		if check_auth(request.form['email'], request.form['password']):
			session['logged_in'] = True
			return redirect(url_for('.secret'))
	return render_template('index.html')


@app.route("/")
def index():
  return render_template("index.html")
  

@app.route('/session/write/<name>/')
def write(name=None):
	session ['name'] = name
	return "Wrote %s into 'name' key of session" % name

@app.route('/session/read/')
def read():
	try:
		if(session['name']):
			return str(session['name'])
	except KeyError:
		pass
	return "No session variable set for 'name' key"


@app.route('/session/remove/')
def remove():
	session.pop('name', None)
	return "Removed key 'name' from session"
  
  
@app.route('/gtr/')
def gtr():
  return render_template('gtr.html')

@app.route("/p1")
def p1():
  return render_template('p1.html')

@app.route("/ferrari/", methods=['GET', 'POST'])
def ferrari():
  if request.method == 'POST':
    print request.form
    name = request.form['name']
    return 'Hello %s' % name
  else:
    return render_template('ferrari.html')

@app.route("/lambo/")
def lambo():
  return render_template('lambo.html')

@app.route("/bugatti/")
def buggati():
  return render_template('buggati.html')

@app.route("/p918/")
def p918():
  return render_template('p918.html')


@app.errorhandler(404)
def page_not_found(error):
  return "couldnt find the page you requested.", 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

	
@app.route('/config/')
def config():
	str = []
	str.append('debug:'+app.config['DEBUG'])
	str.append('port:'+app.config['port'])
	str.append('url:'+app.config['url'])
	str.append('ip_adress:'+app.config['ip_address'])
	return '\t'.join(str)
	
def init(app):
	config = ConfigParser.ConfigParser()
	try:
		config_location = "etc/defaults.cfg"
		config.read(config_location)

		app.config['DEBUG'] = config.get("config", "debug")
		app.config['ip_address'] = config.get("config", "ip_address")
		
		app.config['port'] = config.get("config", "port")
		app.config['url'] = config.get("config", "url")
	except:
		print "Could not read configs from: ", config_location

if __name__ == '__main__':
	init(app)
	app.run(
	host=app.config['ip_address'],
	port=int(app.config['port']))

