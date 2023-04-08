class Print_area_of_circle:

    def __init__(self):
        self.lov = input("Enter comma sep values here: ")

    def generate_py_list(self):
        return list(self.lov.split(","))

    def generate_py_tuple(self):
        return tuple(self.lov.split(","))

##############################################################

obj_version=Print_area_of_circle()

#check the type
print(type(obj_version.generate_py_list()))
#check the value
print(obj_version.generate_py_list())


#check the type
print(type(obj_version.generate_py_tuple()))
#check the value
print(obj_version.generate_py_tuple())