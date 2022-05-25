# if - elif - else
#判定 score 的分數是否及格
import random as r
score = r.randint(-100,200)
print("score:",score)

#先判斷 score 是否在合法的範圍之內
if score > 100 or score < 0:
    print("分數錯誤")
    exit() #離開程式

#才判斷 score 的分數是否及格
if score >= 60:
    print("及格")
else:
    print("不及格")
