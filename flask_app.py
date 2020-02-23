from flask import Flask, render_template, request
from analysis_twitter_api import create_web_map_from_user_friends_location


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")
    # return '<h1>Hello</h1>'


@app.route("/web_map", methods=["POST"])
def create_web_map():
    screen_name = request.form.get("name")
    create_web_map_from_user_friends_location(screen_name,
                                              'templates/web_map.html')
    return render_template("web_map.html")


if __name__ == "__main__":
    app.run()
