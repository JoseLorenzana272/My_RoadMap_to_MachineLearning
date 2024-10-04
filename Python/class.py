class Point:

    def move(self):
        print('move')

    def draw(self):
        print('draw')


point1 = Point()
point1.move()
point1.draw()

# Little exercise

class Person:

    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi I'm {self.name}, and I'm a human.")


name = input("Write your name: ")

try:
    person1 = Person(name)
    person1.talk()
except ValueError:
    print("Name must be a string")

