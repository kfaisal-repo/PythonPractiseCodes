class Print_extension_of_file:

    def __init__(self):
        self.filename=input("Enter filename: ")

    def print_filename_extension(self):
        return self.filename.split(".")[1]

##########################################################################################################

obj_version=Print_extension_of_file()

print(obj_version.print_filename_extension())
