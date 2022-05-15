from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello_sprout():
    return "<h1>Hello, Sprout! My name is 超級貓貓男</h1>"


if __name__ == "__main__":
    app.run()
