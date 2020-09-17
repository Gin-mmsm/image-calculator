from flask import render_template, request, make_response, jsonify
from datetime import datetime
import werkzeug

from src import app
from src.calculator import ocr_image, txt_calculation


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'GET':
        return render_template('layout.html', request=request.method)

    if request.method == 'POST':
        # ファイルが設定されているか
        if 'uploadFile' not in request.files:
            make_response(jsonify({'result': 'uploadFile is required.'}))
        file = request.files['uploadFile']

        # ファイルが存在しないとき
        if '' == file.filename:
            return render_template('layout.html', request=request.method)

        # アプロードされたファイルを保存する
        filepath = "assets/" + datetime.now().strftime("%Y%m%d%H%M%S") + ".png"
        file.save(filepath)

        # モデルを使って判定する
        txt = ocr_image(filepath=filepath)
        txt_for_print, ans = txt_calculation(txt=txt)
        calc_error = not is_num(ans)

        render = render_template('layout.html', filepath=filepath,
                                 txt=txt_for_print, ans=ans, calc_error=calc_error,
                                 request=request.method,
                                 )
        return render


@app.errorhandler(werkzeug.exceptions.RequestEntityTooLarge)
def handle_over_max_file_size(error):
    print('werkzeug.exceptions.RequestEntityTooLarge')
    return 'result: file size is overed.'


def is_num(string):
    # 整数だった場合
    return str(string).replace('.', '').isnumeric()
