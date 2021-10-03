##############################################################################################
##                         Password Generator made by 💸#8658                              ##
##############################################################################################

import string
from random import sample

characters=string.ascii_letters+string.digits+string.punctuation

length=input("How many characters long would you like your password to be?\n > ")
password="".join(sample(characters,int(length)))

print(password)
