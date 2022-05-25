#迴圈 for-loop 步進迴圈
#印出1-9的數字
for i in range(1,10):
    print(i,end=" ")

print()

for i in range(1,10,3):
    print(i,end=" ")

print()

#數組(陣列)的符號 : [ ]

scores=[100,90,80,85,75,40,35]
#index  0,1,2,3,4,5,6
for score in scores:
    if score >= 60:
        print(score,end=" ")
print()
print(scores[0],scores[1]) #抓取index =0,index =1的資料
print(scores[3]) #抓取index =3 的資料
print(len(scores)) #取得資料元素個數