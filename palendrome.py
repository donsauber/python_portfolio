#Test if a string is a palendrome
from os import system

system('clear')

print("This program tests to see if a given string is a palendrome")
first_string = input("Enter a string: ")
second_string = ""

for i in range(1,len(first_string)+1):
    second_string+=first_string[-i]

if first_string == second_string:
    print("This is a palendrome!")
else:
    print("Sorry, not a palendrome")