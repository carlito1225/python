#物件的__get__與__set__

class USD:
    def __get__(self, instance, owner):
        money= instance.money
        return money / 30

class JPY:
    def __get__(self, instance, owner):
        money= instance.money
        return money / 0.22

class Exchange:
    usd = USD()
    jpy = JPY()
    def __init__(self, money):
        self.money = money

if __name__ == "__main__":
    twd=10000
    exchange = Exchange(twd)
    print("TWD: %d" % twd)
    print("USD: %d" % exchange.usd)
    print("JPY: %d" % exchange.jpy)
