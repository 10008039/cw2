import ConfigParser
from flask import Flask, render_template, url_for, request, redirect, flash, session
app = Flask(__name__)


@app.route("/account/", methods=['POST','GET'])
def account():
	if request.method == 'POST':
		print request.form
		name = request.form['name']
		return "Welcome %s" % name
	else:
		page ='''
		<html><body>
		 <form action="" method="post" name="form">
			<label for="name">Name:</label>
			<input type="text" name="name" id"name"/>
			<input type="submit" name="submit" id="submit"/>
		</form>
		</body><html>'''
		
		return page

@app.route("/")
def index():
  return render_template("index.html")

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
