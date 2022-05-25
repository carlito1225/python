# if - elif - else
#判定 score 的分數是否及格
import random as r
score = r.randint(-100,200)
print("score:",score)

if score >= 60 and score <=100:
    print("及格")

elif score >= 0 and score <59:
    print("不及格")

else:
    print("分數錯誤")