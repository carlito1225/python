scores=[89,95,90,83,43,62,57]
#請用for迴圈試算最高分
if __name__ == "__main__":
    print(scores)
#透過替換法來求得最高分
    max_score=0
    for score in scores:
        if score>max_score:
            max_score=score
    print("最高分=",max_score)

#直接利用內建函式
    print("最高分=",max(scores))
