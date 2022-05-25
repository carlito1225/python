# if - elif - else
# bmi 判定要件
#過輕:bmi <= 18
#正常:18 < bmi <= 23
#過重: bmi >23
import random as r
bmi = r.randint(10,35)
print("bmi:",bmi)
#請判斷bmi是"過輕"、"正常"還是"過重"
#第一種寫法

if bmi <= 18:
    print("過輕")
elif bmi >18 and bmi <= 23:
    print("正常")
else:
    print("過重")

#第二種寫法

if 18 <= bmi <= 23:
    print("正常")
elif bmi>23:
    print("過重")
else:
    print("過輕")
