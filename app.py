import sys

from flask import Flask, render_template, request, jsonify
import backend.bot as bot

app = Flask(__name__)


@app.get("/")
def index_get():
    return render_template("./base.html")


@app.post("/predict")
def predict():
    user_input = request.get_json().get("message")
    response = bot.get_response(user_input)
    message = {"answer": response}
    return jsonify(message)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        if sys.argv[1] == '--train':
            bot.train_bot()
            exit(1)
    app.run(debug=True)
