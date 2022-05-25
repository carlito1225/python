class BMI:
    h = 0  # 公有變數
    w = 0  # 公有變數
    __bmi = 0 # 私有

    #初始建構時所要執行的程序
    def __init__(self,h,w):
        self.h = h
        self.w = w
        self.calcBMI()

    # 計算 bmi 值
    def calcBMI(self):
        self.__bmi = self.w / (self.h/100)**2

    # 取得 bmi 值
    def getBMI(self):
        return self.__bmi

    def __str__(self):
        return str(self.h) + ', ' + str(self.w) + ', ' + str(self.__bmi)