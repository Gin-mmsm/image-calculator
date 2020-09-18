# image-calculator

## 環境

- python 3.7

## アプリの構成

1. 写真をあげる(数式1行のみ、式の長さは可変、イコールなしの数式) (うまくいったら複数行でもチャレンジ)
2. 読み込んだ結果＋計算結果を表示

## ファイル構成

```
flask_app
├ src
│ ├ static --- 静的ファイル置き場所
│ │ ├ index.css
│ │ ├ index.js
│ │ └ assets
│ │   ├ sample.png
│ │   └ etc...
│ ├ templates　--- テンプレート
│ │ └ layout.html
│ ├ __init__.py
│ ├ views.py
│ ├ calculator.py --- 機械学習用
│ └ test.py --- テスト用
├ fonts
│ └ Apple Symbols.ttf
├ Procfile --- Heroku
├ Aptfile --- Heroku
├ README.md
├ .gitignore
├ run.py --- アプリ実行用スクリプト（アプリの入り口）
└ requirements.py --- ライブラリ一覧
```
