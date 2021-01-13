import random 
import tkinter as tk  
from PIL import Image,ImageTk

# 表示文字配列
result = ['ブリ','チーズ牛丼','牛丼','コロッケ','ローストビーフ','ピザ','サラダ','シューマイ','寿司','卵','トースト','鳥丼','うなぎ']

# 画像ファイル名配列
file = [
  './img/buri.jpg',
  './img/cheese-gyudon.jpg',
  './img/egg.jpg',
  './img/gyudon.jpg',
  './img/korokke.jpg',
  './img/pizza.jpg',
  './img/roast-beef.jpg',
  './img/salad.jpg',
  './img/shumai.jpg',
  './img/sushi.jpg',
  './img/toast.jpg',
  './img/tori.jpg',
  './img/unagi.jpg',
]

#ガチャを引くボタンの処理
def screenword():
    # ランダムで文字取得
    randomResult = random.choice(result)
    #ラベル変更
    label.configure(text=randomResult,font=('',80))
    # ボタン変更
    button.configure(text='タイトルへ',font=('',30),command=title)
    # 画像変更
    canvas.itemconfig(canvasImage,image=fileList[result.index(randomResult)])

# タイトルへ ボタンの処理
def title():
    # ラベル変更
    label.configure(text='今日何食べる？',font=('',30))
    # ボタン変更
    button.configure(text='ガチャを引く',font=('',30),command=screenword)
    # 画像変更 (初期画像に戻す)
    canvas.itemconfig(canvasImage,image=cooking)

# 画面作成
screen = tk.Tk()

# 画面タイトル名
screen.title('random lunch')

# 画面サイズ
screen.geometry('790x750')

# 画面領域
canvas = tk.Canvas(bg='white',width=780,height=516)
canvas.place(x=0,y=200)

# ラベル
label = tk.Label(text='今日何食べる？',font=('',30))

# ボタン
button = tk.Button(text='ガチャを引く',font=('',30),command=screenword)

# ラベル配置
label.pack()

# ボタンはいち
button.pack()

# 画像取得&リサイズ処理
def openAndResize(sozai):
    cheeseDogJpg = Image.open(sozai)
    cheeseDog = ImageTk.PhotoImage(cheeseDogJpg.resize(size=(768,512)))
    return cheeseDog

# 初期画像
cooking = openAndResize('./img/cooking.jpg')
canvasImage = canvas.create_image(10,0,image=cooking,anchor=tk.NW)

# 取得した画像ファイルのオブジェクト格納配列
fileList = []

# 画像ファイルを全て読み込み配列に格納
for name in file:
    obj = openAndResize(name)
    fileList.append(obj)

screen.mainloop()
