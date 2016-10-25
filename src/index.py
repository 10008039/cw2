from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
  return "<strong>this is my website</strong>"

@app.route("/hp/")
def hp():
  return "THIS IS PAGE TWooooooooooooO"





if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
 
