import math

class Print_area_of_circle:

    def __init__(self):
        self.radius=float(input("Enter radius: "))

    def print_area(self):
        return math.pi*math.pow(self.radius,2)

##########################################################################################################
obj_version=Print_area_of_circle()

print(obj_version.print_area())
