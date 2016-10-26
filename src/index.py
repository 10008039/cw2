from flask import Flask, render_template
app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(error):
  return "couldnt find the page you requested.", 404

if __name__ == "__main__":
    app.run(host='0.0.0.0' debug=True)
