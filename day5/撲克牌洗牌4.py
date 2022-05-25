import random as r
poker = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]*4

def shuffle(count):
    for i in range(count):
        lens=len(poker)
        p1= r.randint(0,lens-1)
        p2 = r.randint(0, lens - 1)
        #直接對調法
        poker[p1], poker[p2] = poker[p2], poker[p1]

if __name__ == "__main__":
    print(len(poker),poker)
    shuffle(100)
    print(len(poker),poker)
