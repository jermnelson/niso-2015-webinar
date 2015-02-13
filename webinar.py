__author__ = "Jeremy Nelson"
__license__ = "GPLv3"

from flask import Flask, render_template

webinar = Flask(__name__)

@webinar.route("/<path:page>")
def slide(page):
    return render_template("{}.html".format(page))

@webinar.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    webinar.run('0.0.0.0', 20152, debug=True)
