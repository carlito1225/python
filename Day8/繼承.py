# 繼承
class Person:
    name = ''
    age = 0
    sex = ''

class Student(Person):
    grade = 0

class Teacher(Person):
    salary = 0

if __name__ == '__main__':
    student = Student()
    student.name = 'Vincent'
    student.age = 18
    student.sex = 'M'
    student.grade = 8
    print(student.name, student.age, student.sex, student.grade)