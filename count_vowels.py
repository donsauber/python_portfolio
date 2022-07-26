# Count the number of vowels and the number of consonents in a given string
from os import system

system('clear')


print("This program counts vowels and consonents in a string")
test_string = input("Enter a string: ")

vowels = {'a', 'e', 'i', 'o', 'u'}
vowel_count = 0
consonent_count = 0

for i in test_string:
    if i in vowels:
        vowel_count += 1
    else:
        consonent_count += 1

print(f"The string '{test_string}' has {vowel_count} vowels and {consonent_count} consonants, spaces, or punctuation.")