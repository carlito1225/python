# 例外處理
# 取得使用者輸入的整數數值
def input_int():
    try:
        y = int(input("請輸入分母"))
    except ValueError as e:
        print("請輸入數字，錯誤內容", e)
    else:
        return y

#計算除法
def div(y):
    x = 100
    try:
        result = x / y  # ZeroDivisionError 分母不可為0
    except ZeroDivisionError as e:
        print("分母不可為 0,錯誤內容", e)
    else:
        return x, y, result

#印出結果
def print(x,y )


if __name__ == "__main__":
    div()