import cv2

#定義臉部偵測檔
face_cascade = cv2.CascadeClassifier("./xml/haarcascade_frontalcatface.xml")


# 設定攝像鏡頭(0,1,2, ...)
cap = cv2.VideoCapture(0)

# 判斷 camera 是否有啟動
if not cap.isOpened():
    cap.open() #啟動

print(cap.isOpened())
# 設定捕捉區域
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

while True:
    #捕捉FRAME
    ret, frame = cap.read()
    #print(frame)

    #偵測人臉
    faces =face_cascade.detectMultiScale(
        frame, #待檢測圖片
        scaleFactor=1.1, #檢測粒度 越小越精準但越慢 (1.1可算最小)pixel
        minNeighbors=5, #每個目標至少要檢測幾次以上才認定
        minSize=(30,30), #搜尋最小尺寸
        flags=cv2.CASCADE_SCALE_IMAGE #正常比例檢測
    )

    #找到人臉個數
    amount = len(faces)
    if(amount > 0):
        print("找到 %d 個人臉" % amount)
        print(faces)

    #在臉部周圍畫上矩形
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,100,100), 3) #末兩項(B, G, R)顏色, 線寬。

    #將frame資料顯示
    cv2.imshow("new camera", frame)

    #按下 q 離開
    if cv2.waitKey(1) & 0XFF == ord("q"):
        break;

#釋放資源
cap.release()
cv2.destroyAllWindows()
