import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def i():
    return "hi!"


@app.route("/home")
def home():
    return "ENGLISH mEn"


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
