import random

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
from random import randint
my_file = open("test.json", "w")
y = 1
while y < 100:
    a = random.randint(1, 100)
    a = int(a)
    password =''
    for i in range(a):
        password += random.choice(chars)
        my_file.write(password + '\n')        
    y = y + 1    
    print(password)   
my_file.close()
