scores=[89,95,90,83,43,62,57]
#請試算總分,平均,最高分
if __name__ == "__main__":
    print(scores)
#請用for迴圈試算總分,平均,最高分
    sum = 0
    for score in scores:
        print(scores) #印出每一筆分數
        sum = sum + score #每一筆分數與sum進行累加
    print("總分=",sum)
    print("平均=",sum/len(scores))
