import random

class dog:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.saturation = 40
        self.weight = 20
        self.alive = True
    def to_eat(self):
        print("Time to eat")
        self.saturation += 2
        self.weight += 0.10
        self.gladness += 1
    def to_sleep(self):
        print("I will sleep")
        self.gladness += 2
        self.weight += 0.1
    def to_chill(self):
        print("Rest time")
        self.gladness += 1
        self.saturation -= 2
        self.weight += 0.1
    def to_walk(self):
        print("I will walk")
        self.gladness += 1
        self.saturation -= 5
        self.weight -= 0.50
    def is_alive(self):
        if self.weight < 10:
            print("Death from starvation")
            self.alive = False
        elif self.saturation == 0:
            print("Death from starvation")
            self.alive = False
        elif self.gladness == 0:
            print("Depression…")
            self.alive = False
        elif self.weight >= 30:
            print("Death from overeating")
            self.alive = False
        elif self.weight <= 20:
            print("Normal weight…")
            self.alive = False
        elif self.gladness >= 500:
            print("Normal gladness")
            self.alive = False
    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"saturation = {round(self.saturation, 2)}")
        print(f"Weight = {round(self.weight, 2)}")
    def end_of_year(self):
        if day == "364":
            print(f"Gladness = {self.gladness}")
            print(f"saturation = {round(self.saturation, 2)}")
            print(f"Weight = {round(self.weight, 2)}")
        breakpoint()
    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_eat()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
            self.end_of_day()
            self.is_alive()
snikers = dog(name="snikers")
for day in range(365):
 if snikers.alive == False:
    break
 snikers.live(day)
 e = input("7")

 if e == ("BELUGA,RICK,???"):
     print("https://www.youtube.com/watch?v=o16TyBbAUAg")
     print("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
     print("https://www.google.com/search?sca_esv=27dc6454a5630b7b&rlz=1C1GCEA_enUA1007UA1007&sxsrf=ADLYWIK578zrb9qP4yoT1XtMrfKzt-fxzQ:1731521171207&q=%D1%82%D0%B0%D0%BA%D1%81%D0%B0&udm=2&fbs=AEQNm0AsxJe8lWY5tkJ-SCURVqqlDljY9ZJaR7wpbIwisgKxwj7MQyCC4RC5PV2YJRUv2nZQNX219hgYquJA2LgtJ_FIvNy9VIiK0udTVWrrOeAwzAYKWrb2qmPEWswZqBWtKibBZGm5ZXBbS_kmw0Fr0F4clgsLMq_xS_zW2GMtcwT9jAO8mb1LWgO1SGm7UYDgeCUDBggtkA0Q1g8Y-PgHhY_PQ6NnAKDpHCfmVHKZjDHgNHmIfSKRjH4Pf2xOFa0UmpTvXHIV&sa=X&ved=2ahUKEwj0tNKC89mJAxUFS_EDHRjcLyQQtKgLegQIDhAB&biw=1178&bih=564&dpr=1.63")
     break
 else:
     print("no")




