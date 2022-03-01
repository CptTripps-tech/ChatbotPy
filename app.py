from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import backend.bot as bot
import sys

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)

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
