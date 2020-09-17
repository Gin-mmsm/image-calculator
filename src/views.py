from flask import render_template, request, make_response, jsonify
from datetime import datetime
import werkzeug

from src import app
from src.calculator import ocr_image, txt_calculation


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'GET':
        return render_template('layout.html')
