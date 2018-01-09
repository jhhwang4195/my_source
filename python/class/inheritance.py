# -*- coding: utf-8 -*-
#!/usr/bin/python


class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        print("move")

    def speak(self):
        pass


class Dog (Animal):
    def speak(self):
        print("bark")


class Duck (Animal):
    def speak(self):
        print("quack")

if __name__ == '__main__':
    # Inheritance
    dog = Dog("doggy")
    print "\n>>>> vars(dog)"
    print vars(dog)
    print "\n>>>> dog.__dict__"
    print dog.__dict__
    print "\n>>>> dir(dog)"
    print dir(dog)

    n = dog.name
    dog.move()
    dog.speak()

    # Polymorphism
    animals = [Dog('doggy'), Duck('duck')]

    for a in animals:
        a.speak()


"""
########################################
# Result
########################################
>>>> vars(dog)
{'name': 'doggy'}

>>>> dog.__dict__
{'name': 'doggy'}

>>>> dir(dog)
['__doc__', '__init__', '__module__', 'move', 'name', 'speak']
move
bark
bark
quack
"""
