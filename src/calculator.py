from PIL import Image           # 画像処理ライブラリ
import numpy as np              # データ分析用ライブラリ
import pyocr                    # OCR ラッパーライブラリ 対応OCR:Tesseract, Cuneiform
import pyocr.builders           # OCR ラッパーライブラリ 対応OCR:Tesseract, Cuneiform

# OCRが使用可能かをチェック
tools = pyocr.get_available_tools()

tool = tools[0]

# OCR対応言語を表示
langs = tool.get_available_languages()
print("Available languages: %s" % ", ".join(langs))
lang = 'eng'
print("Will use lang '%s'" % lang)

filename = '../assets/sample.png'
# filename = '../assets/12345.png'
# filename = '../assets/67890.png'
# filename = '../assets/+-×.png'
# filename = '../assets/+-×÷.png'

# 読み込んだ画像をOCRでテキスト抽出してみる。
txt = tool.image_to_string(
    Image.open(filename),
    lang=lang,
    builder=pyocr.builders.TextBuilder(tesseract_layout=7)
)
print(txt)
