from day7.OO2 import BMI

if __name__ == '__main__':
    b = BMI()
    b.h = 170
    b.w = 60
    print(b)
    b.calcBMI()
    print(b)
    print(b.getBMI())