# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

class sum_n_nn_nnn:

    def __init__(self):
        self.numb=int(input("Enter number: "))

    def print_sum_n_nn_nnn(self):
        return (self.numb + (self.numb+(10*self.numb))+(self.numb+(10*self.numb)+(100*self.numb)))

##############################################################
obj_version=sum_n_nn_nnn()
print(obj_version.print_sum_n_nn_nnn())