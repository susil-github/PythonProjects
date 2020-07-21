class Animal:
    def doSpeak(self):
        print("animal speaks...")

class Dog(Animal):
    def doEat(self):
        print("Dog eats...")

d= Dog()
d.doEat()
d.doSpeak()