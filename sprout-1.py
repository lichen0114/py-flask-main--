from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello_sprout():
    return "<h1>Hello, Sprout! My name is lichen</h1>"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
