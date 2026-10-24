print("Welcome to the random password generator")

import random
import string

len = 8
random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=len))
print("This is your password: ",random_string)