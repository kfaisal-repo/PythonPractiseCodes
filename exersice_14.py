
class Print_begins_with_is:

    def __init__(self):
        self.sample_string=input("Enter a string: ")
        self.numb=int(input("How many times: "))

    def check_begins_with_is(self):
        if self.sample_string.startswith("Is"):
            return self.sample_string
        else:
            return "Is " + self.sample_string

    def generate_n_copies_of_string(self):
        return self.numb *self.sample_string
##############################################################

obj_version=Print_begins_with_is()
#print(obj_version.check_begins_with_is())
print(obj_version.generate_n_copies_of_string())

