import random

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_+-=/.,';][\`"

use = lowercase + uppercase + numbers + symbols
length_of_password = 8

password = "".join(random.sample(use, length_of_password))

print("Your generated password: " + password)