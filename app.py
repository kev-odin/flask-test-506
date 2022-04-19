from flask import Flask
import datetime

app = Flask(__name__)


@app.route("/")
def hello_world():
    return f"Hello World!"


@app.route("/owner")
def owner():
    return "Hello world to Kevin C!"


@app.route("/datetime")
def current_time():
    return f"Current time: {datetime.datetime.now()}"


if __name__ == "__main__":
    app.run(debug=True)
