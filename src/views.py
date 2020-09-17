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
            make_response(jsonify({'result': 'uploadFile is required.'}))
        file = request.files['uploadFile']
        if '' == file.filename:
            make_response(jsonify({'result': 'filename must not empty.'}))

        # アプロードされたファイルを保存する
        filepath = "assets/" + datetime.now().strftime("%Y%m%d%H%M%S") + ".png"
        file.save(filepath)

        # モデルを使って判定する
        txt, frame_img = ocr_image(filepath=filepath)
        filepath_frame = "assets/" + datetime.now().strftime("%Y%m%d%H%M%S") + "_frame.png"
        frame_img.save(filepath_frame)
        txt_for_print, ans = txt_calculation(txt=txt)
        calc_error = not is_num(ans)

        return render_template('layout.html', filepath=filepath, filepathframe=filepath_frame, txt=txt_for_print, ans=ans, calc_error=calc_error)


@app.errorhandler(werkzeug.exceptions.RequestEntityTooLarge)
def handle_over_max_file_size(error):
    print('werkzeug.exceptions.RequestEntityTooLarge')
    return 'result: file size is overed.'


def is_num(string):
    return string.replace('.', '').isnumeric()
