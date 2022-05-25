'''
min-    max
0-100之間猜一個數字
-------------------
20-100
20-65
30-65
30-47
30-41
36-41
38 bingo
'''
import random as r
min=0
max=100
ans=r.randint(min+1,max-1)


while True:
    user_guess=int(input("使用者在 %d - %d 之間猜一數字:"%(min,max)))
    # 判斷USER所猜是否是合法資料範圍
    if user_guess <= min or user_guess >= max:
        print("數字範圍錯誤")
        continue #重跑迴圈


    #判斷是否有猜對
    if user_guess < ans:
        min=user_guess

    elif user_guess > ans:
        max=user_guess

    else:
        print("恭喜 user 答對")
        break

    #----------------------------------------------------------------------------
    # PC猜數字
    # min max ==> min+1 max-1
    # 20-65 ==> 21-64
    pc_guess = r.randint(min+1,max-1)
    print("PC猜:",pc_guess)
    if pc_guess < ans:
        min = pc_guess
    elif pc_guess > ans:
        max = pc_guess
    else:
        print("恭喜PC答對")
        break