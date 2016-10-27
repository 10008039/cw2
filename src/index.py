from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route('/gtr/')
def gtr():
  return render_template('gtr.html')

@app.route("/p1")
def p1():
  start = '<img src="'
  url = url_for('static', filename='image/p1.jpg')
  end = '">'
  return start+url+end, 200

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
def veyron():
  return render_template('bugatti.html')

@app.route("/p918/")
def p918():
  return render_template('p918.html')


@app.errorhandler(404)
def page_not_found(error):
  return "couldnt find the page you requested.", 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
