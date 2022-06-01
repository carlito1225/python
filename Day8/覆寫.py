#繼承之下的覆寫，覆寫一定要在繼承之下才有意義。
class Bird:
    def move(self):
        print("我會飛")
class Penguin(Bird):
    def move(self):
        print("我不會飛，但是我會游泳")

if __name__ == '__main__':
    bird = Bird();
    bird.move()
    penguin = Penguin();
    penguin.move()
