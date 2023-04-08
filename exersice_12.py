# How many leap years between 1923 to 2023
# 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968,
# 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020

import calendar
class Print_calendar:

    def __init__(self):
        self.input_params=input("Enter start year(yyyy) and end year(yyyy) separated by space: ")
        self.start,self.end=self.input_params.split(" ")

    # Print specific month calendar, please set input parameters again. This code is modified
    def print_specific_month_calendar(self):
        mm,yyyy=self.func_name.split(" ")
        return calendar.month(int(yyyy),int(mm))

    # Print all leap years between given start and end year
    def print_all_leap_years_between_given_years(self):
        list_of_leap_year=[]
        for i in range(int(self.start),int(self.end)):
            if calendar.isleap(i):
                list_of_leap_year.append(i)
        return list_of_leap_year

##############################################################
obj_version=Print_calendar()
print(obj_version.print_all_leap_years_between_given_years())

