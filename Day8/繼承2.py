# 繼承 __init__, __str__
class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self):
        return 'name: %s age: %d sex: %s ' % (self.name, self.age, self.sex)

class Student(Person):
    def __init__(self, name, age, sex, grade):
        # super() 在此指的就是 Person 物件
        #super().__init__(name, age, sex)  # 調用 Person 的 __init__ 方法
        Person.__init__(self, name, age, sex)
        self.grade = grade

    def __str__(self):
        return super().__str__() + 'grade: %d' % self.grade

if __name__ == '__main__':
    student = Student('Vincent', 18, 'M', 8)
    print(student)