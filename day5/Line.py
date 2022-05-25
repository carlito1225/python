#撰寫一個LineNotify推播工具
#推播文字,內建小圖,自訂小圖
import requests
token="3IcEkexGbXqblVqBndaSnOBnbYmBnPUUsCqH5k8QG0o" #授權碼
lineNotifyURL = "https://notify-api.line.me/api/notify"

#推播文字
def lineNotifyText(msg):
    # 建立HTTP的標頭(Header)資訊
    # Authorization 授權
    headers = {"Authorization": "Bearer " + token, "Content-type": "application/x-www-form-urlencoded"}

    # payload 傳送內容
    payload = {"message": msg}
    response = requests.post(lineNotifyURL,
                             headers=headers, params=payload)
    print("回應碼:", response.status_code)

#推播內建小圖
def lineNotifySticker(PackageId, id):
    headers = {"Authorization": "Bearer " + token, "Content-type": "application/x-www-form-urlencoded"}

    # payload 傳送內容
    payload = {"message":" ",
               "stickerPackageId": PackageId,
               "stickerId": id}

    response = requests.post(lineNotifyURL,
                             headers=headers, params=payload)
    print("回應碼:", response.status_code)

#推播地端自訂小圖
def lineNotifyLocalImage(imageURI):
    headers = {"Authorization": "Bearer " + token}

    # payload 傳送內容
    payload = {"message": " "}
    imgFile = {"imageFile": open(imageURI,"rb")} #r讀取b二進位資料
    response = requests.post(lineNotifyURL,
                             headers=headers, params=payload, files=imgFile)
    print("回應碼:", response.status_code)

#推播雲端圖片
def lineNotifyWebImage(imageURI):
    headers = {"Authorization": "Bearer " + token}

    # payload 傳送內容
    payload = {"message": " ",
               "imageThumbnail" : imageURI,
               "imageFullsize" : imageURI,
               } #message 一定要放

    response = requests.post(lineNotifyURL,headers=headers, params=payload)
    print("回應碼:", response.status_code)