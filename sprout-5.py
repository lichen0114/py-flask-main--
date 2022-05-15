from flask import Flask
app = Flask(__name__) #Flask = class , app = instance

visitor = 0

@app.route("/")
def hello_sprout():
    global visitor
    visitor += 1
    return f"<h1>造訪人數：{visitor}</h1>"

if __name__ == "__main__":
    visitor = 0
    app.run()