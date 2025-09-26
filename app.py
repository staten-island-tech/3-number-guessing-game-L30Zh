import random

y = random.randint (1, 10)

print (y)

while True:
   
    y = int(y)
    x = input ("Okay, pick a number 1-10")
    while x == y:
        input ("YEAHHAHHAHAHAHHH")
    if int(x) > y:
        input("Too high!")
    elif int(x) < y:
        input("Too low!")
    elif int(x) == y:
        print ("YEAHHAHHAHAHAHHH")
    
    

