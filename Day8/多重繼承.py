# 多重繼承
class Employee:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "employee name: %s" % self.name

class Computer:
    def __init__(self, cpu_speed):
        self.cpu_speed = cpu_speed
    def __str__(self):
        return "Computer cpu_speed: %d" % self.cpu_speed

class Robot(Employee, Computer):
    def __init__(self, name, cpu_speed, nickname):
        Employee.__init__(self, name)
        Computer.__init__(self, cpu_speed)
        self.nickname = nickname
    def __str__(self):
        return Employee.__str__(self) + Computer.__str__(self) + "nickname: %s" % self.nickname

if __name__ == '__main__':
    robot = Robot("春麗", 3.0, "保全")
    print(robot)