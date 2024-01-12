from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/")
def hello_world():
    response = jsonify({'data': 'this home route'})
    return response


@app.route("/classify", methods=["POST"], strict_slashes=False)
def classify():
    if request.method == "POST":
        if 'img' in request.files:
            img_file = request.files['img']
            return "File berhasil diunggah"
        else:
            return "Kunci 'img' tidak ditemukan di dalam request.files", 400
    return "Metode yang diizinkan adalah POST", 405


app.run()
