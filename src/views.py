from flask import render_template, request, make_response, jsonify
from datetime import datetime
import werkzeug

from src import app
from src.calculator import ocr_image, txt_calculation


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'GET':
        return render_template('layout.html')

    if request.method == 'POST':
        # ファイルが設定されているか
        if 'uploadFile' not in request.files:
            make_response(jsonify({'result': 'upladFile is required.'}))
        file = request.files['uploadFile']
        if '' == file.filename:
            make_response(jsonify({'result': 'filename must not empty.'}))

        # アプロードされたファイルを保存する
        filepath = "assets/" + datetime.now().strftime("%Y%m%d%H%M%S") + ".png"
        file.save(filepath)
