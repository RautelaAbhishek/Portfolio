import random

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

letters = []
for i in alphabet:
    letters.append(i)

numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ["!","@","#","$",'%','&','*','(',')']

length = int(input("How many letters would you like in your password?\n"))
num = int(input("How many numbers would you like in your password?\n"))
special = int(input("How many special characters would you like in your password?\n"))
password = []

for i in range(length):
    char = random.randint(0,51)
    password.append(letters[char])
for i in range(num):
    char = random.randint(0,9)
    password.append(numbers[char])
for i in range(special):
    char = random.randint(0,8)
    password.append(symbols[char])

random.shuffle(password)
combine = "".join(password)
        
print("Your password is : " + combine)
    
    
        
        
