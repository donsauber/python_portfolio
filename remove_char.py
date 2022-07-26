#How do you remove all occurrences of a given character from the input string?
from os import system

system('clear')


print("This program removes all occurrences of a given character from the input string")

given_string = input("Enter the string: ")
given_char = input("Enter a character:  ")

result = given_string.replace(given_char, "")

print(f"The result is {result}")