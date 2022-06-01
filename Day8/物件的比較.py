'''
物件的比較
>   __gt__
>=  __ge__
<   __lt__
<=  __le__
==  __eq__
<>  __neq__
'''

class Drink:
    def __init__(self, name, amount, total_price):
        self.name = name
        self.amount = amount
        self.total_price = total_price

    def __gt__(self, other):
        return (self.total_price/self.amount) > (other.total_price/other.amount)


if __name__ == '__main__':
    milk = Drink("牛奶", 3, 80) #牛奶3杯80元
    coffee = Drink("咖啡", 2, 55) #咖啡2杯55元
    #試問哪一個單價高?
    print(milk > coffee)
    print(milk < coffee)
    #便宜的飲料
    name =  milk.name if milk < coffee else + coffee.name
    print("便宜的是:", name)

    #便宜的飲料
    name =  milk.name if milk > coffee else + coffee.name
    print("較貴的是:", name)