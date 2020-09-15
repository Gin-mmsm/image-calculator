from PIL import Image           # 画像処理ライブラリ
import numpy as np              # データ分析用ライブラリ
import pyocr                    # OCR ラッパーライブラリ 対応OCR:Tesseract, Cuneiform
import pyocr.builders           # OCR ラッパーライブラリ 対応OCR:Tesseract, Cuneiform


def ocr_image(filepath, threshold=100):
    # OCRが使用可能かをチェック
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("Cannot use pyocr")
        return None

    tool = tools[0]

    # OCR対応言語を表示
    langs = tool.get_available_languages()
    print("Available languages: %s" % ", ".join(langs))
    lang = 'eng'
    print("Will use lang '%s'" % lang)

    # 画像の前処理
    # とりあえず2値化
    img = Image.open(filepath)
    gray = img.convert('L')
    mono = gray.point(lambda x: 0 if x < threshold else 255)

    # 読み込んだ画像をOCRでテキスト抽出してみる。
    txt = tool.image_to_string(
        mono,
        lang=lang,
        builder=pyocr.builders.TextBuilder(tesseract_layout=7)
    )
    return txt


'''
----------以下テスト用----------
'''
# OCRが使用可能かをチェック
tools = pyocr.get_available_tools()

tool = tools[0]

# OCR対応言語を表示
langs = tool.get_available_languages()
print("Available languages: %s" % ", ".join(langs))
lang = 'eng+equ'
print("Will use lang '%s'" % lang)

filename = '../assets/sample.png'
# filename = '../assets/12345.png'
# filename = '../assets/67890.png'
# filename = '../assets/+-×.png'
# filename = '../assets/+-×÷.png'

# 画像の前処理
# とりあえず2値化
img = Image.open(filename)
gray = img.convert('L')
mono = gray.point(lambda x: 0 if x < 100 else 255)
mono.show()

# 読み込んだ画像をOCRでテキスト抽出してみる。
txt = tool.image_to_string(
    mono,
    lang=lang,
    builder=pyocr.builders.TextBuilder(tesseract_layout=7)
)
print(txt)
