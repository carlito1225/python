# 物件導向
# 建立一個 Human 的類別
class Human:
    name = " " #屬性/欄位/變數
    age = 0
    sex = " "
    #將物件內容以自訂字串格式輸出
    def __str__(self) -> str:
        return self.name + "," + str(self.age) + "," + self.sex

if __name__ == '__main__':
    #建立一個物件
    h1 = Human()
    h1.name ="Vincent";h1.age = 18;h1.sex = "男"
    #再建立一個物件
    h2 = Human()
    h2.name="Anita";h2.age=19;h2.sex="女"

    #print(h1, h1.name, h1.age, h1.sex)
    #print(h2, h2.name, h2.age, h2.sex)
    print(h1)
    print(h2)