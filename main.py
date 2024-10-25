from flask import Flask
from flask import send_file

app = Flask(__name__)

@app.route("/")

def index():
    return "Hello world!"

@app.route("/calciatori")

def calciatori():
    return send_file('calciatori.json')

if __name__ == "__main__":

    app.run()
