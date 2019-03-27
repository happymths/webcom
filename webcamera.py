from PIL import Image, ImageDraw, ImageFont
import cv2
import subprocess


###############################################
###############################################
#webカメラで画像とって保存.cv2を使ってるのはここのみ

cap = cv2.VideoCapture(-1)

if cap.isOpened() is False:
    print("can not open camera")
    sys.exit()

#cv2.namedWindow("webcam", cv2.WINDOW_AUTOSIZE)
ret, frame = cap.read()
cv2.imwrite("capturedImage.jpg",frame)
###################################################
################################################





###subprocessで快不快判定を動かして返ってきた文字列取得########

cmd = "sh run2.sh"
#cmd ="ls"
subprocess.call(cmd.split())

try:
    res = subprocess.check_output(cmd.split())
except:
    print("Error.")

response=res.decode('utf-8')


if "class_1_images" in response:#みたいなの
    judge="不快"
elif "class_2_images" in response:#みたいなの
    judge="快"

else:
    print(response)
    judge=response




############################画像の読み込み#######
############################################

img = Image.open("capturedImage.jpg")
#drawインスタンスを生成
draw = ImageDraw.Draw(img)
#フォントの設定(フォントファイルのパスと文字の大きさ)
font = ImageFont.truetype("kokoro/Kokoro.otf", 27)










#文字を書く
draw.text((10, 10), judge, fill=(255, 0, 0),font=font)
#改行できる
#draw.text((10, 10), u'\n名前はまだ無い。', fill=(0, 0, 255), font=font)
img.save("judge-result.jpg")

cmd ="fbi judge-result.jpg"
subprocess.call(cmd.split())

