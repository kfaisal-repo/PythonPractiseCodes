# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
import calendar
class Print_calendar:

    def __init__(self):
        self.func_name=input("Enter month(mm) and year(yyyy) separated by space: ")

    def print_specific_month_calendar(self):
        mm,yyyy=self.func_name.split(" ")
        return calendar.month(int(yyyy),int(mm))

##############################################################
obj_version=Print_calendar()
print(obj_version.print_specific_month_calendar())