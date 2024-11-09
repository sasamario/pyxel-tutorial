# pyxelとは
公式Github：https://github.com/kitao/pyxel/blob/main/docs/README.ja.md  
作者さんのQiita記事：[【公式】レトロゲームエンジンPyxelを使わない理由が見つからない](https://qiita.com/kitao/items/eae53dd47c663b497352)

> Pyxel (ピクセル) は、 Python 向けのレトロゲームエンジンです。
使える色は 16 色のみ、同時に再生できる音は 4 音までなど、レトロゲーム機を意識したシンプルな仕様で、Python を使ってドット絵スタイルのゲームづくりが気軽に楽しめます。

# インストール方法
1. Homebrewをインストール　`brew -v`で確認
2. 以下コマンドを実行
```bash
brew install pipx
pipx ensurepath
pipx install pyxel
```
pipx：システムにインストール済みの他パッケージとの間に依存関係の衝突を起こすことなくPythonのコマンドラインアプリケーションをインストールし動作させるためのツール  

3. 任意のディレクトリに移動し、サンプルをコピーする。copy_examplesというディレクトリができる `pyxel copy_examples`
4. サンプルは.gitignoreで追跡対象外としておく

## サンプルの実行
```bash
cd pyxel_examples
pyxel run 01_hello_pyxel.py
pyxel play 30sec_of_daylight.pyxapp
```

終了する場合エスケープキーを押せば良い