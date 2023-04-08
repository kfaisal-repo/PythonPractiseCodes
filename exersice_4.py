class Print_area_of_circle:

    def __init__(self):
        self.first_name = input("Enter first name: ")
        self.last_name = input("Enter last name: ")

    def print_reverse_names(self):
        return self.last_name[::-1] + self.first_name[::-1]

##########################################################################################################

obj_version=Print_area_of_circle()
print(obj_version.print_reverse_names())

