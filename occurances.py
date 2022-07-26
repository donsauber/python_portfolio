#Find the number of occurances of a character in a string
from os import system

system('clear')

print("This program finds the number of times a character is in a string")
rune = input("Enter the character to count: ")
test_string = input("Enter the string to check: ")

count = 0 
for i in test_string:
    if i == rune:
        count += 1

print(f"There are {count} '{rune}'s in {test_string}")