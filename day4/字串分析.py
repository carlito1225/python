str = "she sell sea shell on the sea shore"
print(str)
print("有幾個字?", len(str))
print("有幾個單字?", len(str.split(" ")))
print("2-10範圍的字串內容", str[2:10])
print("有幾個 s ?", str.count("s"))
print("最近的sea在哪個位置?", str.find("sea"))
print("最近的tea在哪個位置?", str.find("tea")) #結果為-1表示沒有找到資料

str="    母親節 快樂 !        "
print(str)
str=str.lstrip() #去除左側空白
print(str)
str=str.rstrip() #去除右側空白
#str=str.strip() #去除左右空白
print(str)
path =r"c:\temp\nba.txt"
print("路徑:",path)