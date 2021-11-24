import random
import time

Password = ""

Upper_count = int(input("How many upper case letters do you want in your password: "))
Lower_count = int(input("How many lower case letters do you want in your password: "))
Num_count = int(input("How many Numbers do you want in your password: "))
Symbol_count = int(input("How many symbols do you want in your password: "))

for i in range(Upper_count):
    Password += chr(random.randint(ord('A'),ord('Z')))
    
for j in range(Lower_count):
    Password += chr(random.randint(ord('a'),ord('z')))
    
for i in range(Num_count):
    Password += str(random.randint(0,9))

for i in range(Upper_count):
    Password += chr(random.randint(ord('a'),ord('z')))

for i in range(Symbol_count):
    Password += chr(random.randint(33,47))
    
print("Making password.......")
time.sleep(3)
print('your password is')
time.sleep(1)
pwd =list(Password)
random.shuffle(pwd)
print(''.join(pwd))

