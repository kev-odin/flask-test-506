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
    now = datetime.datetime.now()
    return f'Current: {now.strftime("%m/%d/%Y, %H:%M:%S")}'


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
