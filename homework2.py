import random

class Dog:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.sleep = 5
        self.alive = True
    def to_HaveFun(self):
        print("Time to have fun")
        self.sleep -= 0.1
        self.gladness -= 2.5
    def to_sleep(self):
        print("Time to Sleep")
        self.gladness += 1.5
        self.sleep += 0.25
    def to_chill(self):
        print("Rest Time")
        self.gladness += 2.5
    def is_alive(self):
        if self.sleep < -0.5:
            print("Didnt had enough sleep and died :(")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression")
            self.alive = False
        elif self.gladness > 200:
            print("Overhapines")
            self.alive = False
    def end_of_day(self):
        print(f"Gladdnes = {self.gladness}")
        print(f"Sleep = {self.sleep}")
    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1,3)
        if live_cube == 1:
            self.to_HaveFun()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
            self.end_of_day()
            self.is_alive()
Buddy = Dog(name="Buddy")
for day in range(365):
    if Buddy.alive == False:
        break
    Buddy.live(day)