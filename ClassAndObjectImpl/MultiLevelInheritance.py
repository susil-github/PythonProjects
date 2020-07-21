class Animal:
    def speak(self):
        print("this is animal class speak method...")

class Dog(Animal):
    def eat(self):
        print("this is dog class eat method")

class DogChild(Dog):
    def walk(self):
        print("this is child class of Dog and walk method...")

d= DogChild()
d.eat()
d.speak()
d.walk()