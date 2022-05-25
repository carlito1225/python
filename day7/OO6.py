class Stock:
    name = "" #股票名稱
    pe = 0 #本益比
    rate = 0 #殖利率
    pb = 0 #股價淨值比

    def __init__(self, name, pe, rate, pb):
        self.name = name  #股票名稱
        self.pe = pe      #本益比
        self.rate = rate  #殖利率
        self.pb = pb      #股價淨值比

    def __str__(self):
        return "股票名稱:%s 本益比:%f 殖利率:%f 股價淨值比:%f" % \
               (self.name, self.pe, self.rate, self.pb)



