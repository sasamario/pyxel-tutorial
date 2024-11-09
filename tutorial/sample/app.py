import pyxel

# ini()で、ウィンドウサイズを指定し初期化
pyxel.init(160, 120)

def update():
  # btnpはフレームに引数で指定したkeyが押されたらtrue、押されなければfalse
  # ここでは、pyxel.KEY_Qを指定しているので、Qを押下したらtrue
  if pyxel.btnp(pyxel.KEY_Q):
    # Pyxelアプリケーションを終了
    pyxel.quit()

def draw():
    pyxel.cls(0)
    pyxel.rect(10, 10, 20, 20, 11)

pyxel.run(update, draw)