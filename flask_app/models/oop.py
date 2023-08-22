class CoffeeM:
    def __init__(self,name, temp):
        self.name = name
        self.water_temp = temp
    def brew_now(self,beans):
        print(f"Using {beans}!")
        print("Brew now brown cow!")
    def clean(self):
        print("Cleaning!")

class CappuccinoM( CoffeeM ):
    def __init__(self,name, temp):
        super().__init__(name, temp)
        self.milk = "whole"
    def make_cappuccino(self,beans):
        super().brew_now(beans)
        print("Frothy!!!")

class Barista:
    def __init__(self,name):
        self.name = name
        self.cafe = CoffeeM("Cafe")
    def make_coffee(self):
        self.cafe.brew_now()
        

coffee = CoffeeM("Cofee Name", "60")
cappuccino = CappuccinoM("Cappuccino", "80")
print(cappuccino.water_temp)