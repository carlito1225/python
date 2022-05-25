import day5.Line as line

if __name__ == "__main__" :
    line.lineNotifyText("hello world")

    #測試sticker傳送
    line.lineNotifySticker(6325,10979923)

    #測試本地端圖片上傳
    line.lineNotifyLocalImage("bird.jpg")

    #測試雲端圖片上傳
    imageURI = "https://whitecherry2019.com/wp-content/uploads/2019/09/%E7%89%A0%E6%98%AF%E4%B8%96%E7%95%8C%E4%B8%8A%E6%9C%80%E5%8F%AF%E6%84%9B%E7%9A%84%E9%B3%A5%EF%BC%8C%E5%90%8D%E5%8F%AB%E3%80%8C%E7%B2%89%E7%B4%85%E7%BE%85%E8%B3%93%E3%80%8D%EF%BC%8C%E7%B4%85%E8%89%B2%E5%9C%93%E8%82%9A%E8%B6%85%E8%90%8C%E5%8F%88%E5%A4%A2%E5%B9%BB%EF%BC%81-1024x535.jpg"
    line.lineNotifyWebImage(imageURI)