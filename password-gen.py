import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
special = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

n_letters = int(input("Enter the number of letters: "))
n_numbers=(int(input("enter no.of numbers: ")))
n_special=(int(input("enter no.of special: ")))


password_list = []

for i in range(n_letters):
    char = random.choice(letters)
    password_list+=char            #password_list.append(char)

for i in range(n_numbers):
    char= random.choice(numbers)
    password_list+=char            #password_list.append(char)

for i in range(n_special):
    char= random.choice(special)
    password_list+=char            #password_list.append(char)

random.shuffle(password_list)

password="" 


for i in password_list:
    char=i
    password+=char

print(password)