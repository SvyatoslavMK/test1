import random

class Student:
    def __init__(self, name):
        self.name = name
        self.happiness = 50
        self.progress = 0
        self.money = 0
        self.alive = True

    def study(self):
        self.progress += random.randint(10, 20)
        self.money -= 10

    def rest(self):
        self.happiness += random.randint(5, 10)
        self.money -= random.randint(10, 20)

    def work(self):
        self.money += random.randint(30, 50)
        self.happiness -= random.randint(5, 10)

    def is_alive(self):
        return self.alive

    def live(self, day):
        self.happiness -= random.randint(1, 5)
        self.money -= random.randint(1, 10)

        if self.money < 0:
            self.work()

        if self.happiness < 30:
            self.rest()

        if day % 30 == 0:
            self.study()

        if day == 365:
            self.alive = False
        print("")
        print("Day:", day)
        print("Money:", self.money)
        print("Happiness:", self.happiness)
        print("Progress:", self.progress)

nick = Student(name="Slavic")

for day in range(1, 366):
    if not nick.is_alive():
        break
    nick.live(day)

print("=================")
if nick.progress >= 100:
    print(nick.name, "successfuly completed the year with progress", nick.progress)
else:
    print(nick.name, "didn't complete the year and made progress only", nick.progress)
#hi im Svyatoslav my discord "masvkir"