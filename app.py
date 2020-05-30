from flask import Flask, jsonify, request
from mobilenetpeople import getPredictions


app = Flask(__name__)

@app.route("/predict", methods=["POST"])

def predict():
    predictions = getPredictions(request)
    return jsonify(predictions)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)