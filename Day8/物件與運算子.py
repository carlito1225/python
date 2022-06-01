# 物件與運算子
# 例如: + - * /
class Number:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __add__(self, x):
        self.value = self.value + x

    def __sub__(self, x):
        self.value = self.value - x

    def __pow__(self, x):
        self.value = self.value ** x


if __name__ == '__main__':
    one = Number(1)
    two = Number(2)
    five = Number(5)
    print(one, two, five)
    three = Number(3)
    three + 4  # 對應 __add__
    three - 3  # 對應 __sub__
    three ** 2  # 對應 __pow__
    print(three)
