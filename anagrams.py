# Figure out if two strings are anagrams
from os import system

system('clear')


print("This program figures out if two strings are anagrams")

first_string = input("Enter the first string: ")
second_string = input("Enter the second string: ")

first_list = sorted(list(first_string))
second_list = sorted(list(second_string))

if first_list == second_list:
    print("These are anagrams!")
else:
    print("Sorry, these are unrelated")