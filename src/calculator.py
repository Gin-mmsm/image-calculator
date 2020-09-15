from PIL import Image, ImageDraw    # 画像処理ライブラリ
import numpy as numpy   # データ分析用ライブラリ
import pyocr    # OCR ラッパーライブラリ 対応OCR:Tesseract, Cuneiform
import pyocr.builders   # OCR ラッパーライブラリ 対応OCR:Tesseract, Cuneiform


def ocr_image(filepath, threshold=100):
    # OCRが使用可能かをチェック
    tools = pyocr.get_available_tools()
    if not tools:
        print("Cannot use pyocr")
        return

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
# 標準ビューワーが開きます
mono.show()

# 読み込んだ画像をOCRでテキスト抽出してみる。
# txt = tool.image_to_string(
#     mono,
#     lang=lang,
#     builder=pyocr.builders.TextBuilder(tesseract_layout=7)
# )
# print(txt)

# 画像出力
res = tool.image_to_string(
    mono,
    lang=lang,
    builder=pyocr.builders.WordBoxBuilder(tesseract_layout=7)
)

res_im = mono.convert('RGB')
res_draw = ImageDraw.Draw(res_im)
txt_lis = []
for w in res:
    print(w.content)
    txt_lis.append(w.content)
    print(w.position)
    res_draw.rectangle(
        (w.position[0], w.position[1]), None, (255, 0, 0), 2)
# 標準ビューワーが開きます
res_im.show()
txt = ''.join(txt_lis)
print(txt)
