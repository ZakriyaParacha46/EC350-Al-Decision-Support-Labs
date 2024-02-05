import random

count = int(input("Enter the number of passwords: "))
charlen = int(input("Enter the number of charecters: "))

for C in range(count):
    password= ''
    for i in range(charlen):
        rand_char = random.choice([str(random.randint(0,9)),
        chr(random.randint(ord('A'),ord('Z'))),
        chr(random.randint(ord('a'),ord('z')))])
        password+=rand_char
    print(password)