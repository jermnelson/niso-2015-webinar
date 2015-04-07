__author__ = "Jeremy Nelson"
__license__ = "GPLv3"

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<path:page>")
def slide(page):
    return render_template("{}.html".format(page))

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run('0.0.0.0', 20152, debug=True)
