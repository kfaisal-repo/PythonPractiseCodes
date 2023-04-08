class Print_triple_quotes:
    def __init__(self,message):
        self.message=message
    def print_my_messg(self):
        print(self.message)

m="""Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are"""

obj=Print_triple_quotes(m)
print(obj.print_my_messg())