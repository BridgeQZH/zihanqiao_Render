from datetime import datetime

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/time")
def current_time():
    formatted_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template("time.html", current_time=formatted_time)


if __name__ == "__main__":
    app.run(debug=True)
