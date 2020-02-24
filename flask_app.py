from flask import Flask, render_template, request
from analysis_twitter_api import create_web_map_from_user_friends_location
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
    if os.path.exists('templates/web_map.html'):
        os.remove('templates/web_map.html')
    screen_name = request.form.get("screen_name")
    create_web_map_from_user_friends_location(screen_name,
                                              'templates/web_map.html')
    return render_template("web_map.html")


if __name__ == "__main__":
    app.run(debug=True)