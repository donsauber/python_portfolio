# Reverse a string
from os import system

system('clear')

print("This program reverses a given string")
first_string = input("Enter a string: ")
second_string = ""

for i in range(1,len(first_string)+1):
    second_string+=first_string[-i]

print(second_string)