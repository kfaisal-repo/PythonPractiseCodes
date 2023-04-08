# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

class doc_string:

    def __init__(self):
        self.func_name=input("Enter function name: ")
        print(self.func_name)

    def print_doc_string(self):
        print((self.func_name).__doc__)

##############################################################
obj_version=doc_string()
print(obj_version.print_doc_string())