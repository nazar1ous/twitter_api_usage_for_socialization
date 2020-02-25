from flask import Flask, render_template, request
from analysis_twitter_api import get_web_map_from_user_friends_location
import os

app = Flask(__name__)


@app.route("/")
def index():
    """
    If user goes to the main route, opens index.html
    :return:
    """
    return render_template("index.html")


@app.route("/web_map", methods=["POST"])
def web_map():
    """
    Creates the web map of twitter friends
    :return: object of rendered template
    """
    screen_name = request.form.get("screen_name")
    html_doc = get_web_map_from_user_friends_location(screen_name)
    return html_doc


if __name__ == "__main__":
    app.run(debug=True)