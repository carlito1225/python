#自訂函式
#h代表身高, w代表體重
#return bmiValue, result
def calcBMIAndResult(h,w):
    bmiValue= w / ((h/100)**2)

    result="過重" if bmiValue >23 else "過輕" if bmiValue <=18 else "正常"

    return bmiValue,result

#---------------------------------
#主程式
#---------------------------------
if __name__ == "__main__":
    h=170
    w=60
    bmi, res=calcBMIAndResult(h,w)
    print(bmi)
    print(res)