#自訂函數篇
#加法函式
def add(x,y):
    sum = x+y
    return sum

def div(x,y):
    sum = x/y
    return sum

def max(x,y):
    maxValue= x if x>y else y
    return maxValue

#---------------------------------
#主程式
#---------------------------------
a,b=10,20
result =add(a,b)
print(result)

result = div(a,b)
print(result)

result = max(a,b)
print(result)