from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Index!"

@app.route("/hello")
def hello():
    return "Hello World"

@app.route("/easy")
def easy():
    return "Easy"

@app.route("/easy/<string:game>")
def getGame(game: str):
    return game



if __name__ =="__main__":
    app.run()