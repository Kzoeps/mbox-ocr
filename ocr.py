from flask import Flask, request, jsonify
from paddleocr import PaddleOCR
from flask_cors import CORS
import os
from tempfile import mkdtemp
from io import BytesIO
from PIL import Image
from numpy import asarray
from werkzeug.utils import secure_filename


app = Flask(__name__)
img_path = './mbob-test.jpeg'
ocr = PaddleOCR(use_angle_cls=True, lang='en')
CORS(app, origins="*")
UPLOAD_FOLDER = './temp/images'


@app.route("/", methods=["POST", "GET"])
def hello():
    if request.method == "POST":
        uploadFile = request.files['file']
        fileName = secure_filename(uploadFile.filename)
        filePath = os.path.join(mkdtemp(), fileName)
        print(filePath)
        uploadFile.save(filePath)
        result = ocr.ocr(filePath)
        return jsonify(result)

def convert_to_array(file):
    # bites = BytesIO(file)
    image = Image.open(file)
    data = asarray(image)
    return data
if __name__ == "__main__":
    app.run(debug=False, port=8081, host='0.0.0.0')
