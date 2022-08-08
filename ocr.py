from flask import Flask, jsonify
from paddleocr import PaddleOCR
from flask_cors import CORS


app = Flask(__name__)
img_path = './mbob-test.jpeg'
ocr = PaddleOCR(use_angle_cls=True, lang='en')
CORS(app, origins="*")


@app.route("/")
def hello():
    result = ocr.ocr(img_path,cls=True)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=False, port=8081, host='0.0.0.0')
