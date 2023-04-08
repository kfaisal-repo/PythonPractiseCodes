class first_n_last_from_list:

    color_list = ["Red", "Green", "White", "Black"]

    def __init__(self):
        pass

    def print_first_n_last_from_list(self):
        return (self.color_list[0],self.color_list[-1])

##########################################################################################################

obj_version=first_n_last_from_list()

print(obj_version.print_first_n_last_from_list())
