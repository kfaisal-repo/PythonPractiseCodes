
import datetime as dt
class Print_no_of_days_between_two_days:

    def __init__(self):
        self.start_date = list(map(int,input("Enter start date: ").strip("(").strip(")").split(",")))
        self.end_date = list(map(int,input("Enter end date: ").strip("(").strip(")").split(",")))

    def no_of_days_between_2_dates(self):
        return dt.date(*self.start_date) - dt.date(*self.end_date)
##############################################################

obj_version=Print_no_of_days_between_two_days()
print(obj_version.no_of_days_between_2_dates())

