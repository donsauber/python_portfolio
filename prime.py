'''
How do you check if the given number is prime?
Use if statements to check for each condition separately:
If the number is 0 or 1, it cannot be prime.
If the number is 2, it is prime number.
If the number is indivisible by other numbers, it is prime.'''

from os import system

system('clear')

def prime(given):
    if given == 1 or given ==0:
        return False
    if given == 2:
        return True 
    
    for i in range(2,given):
        if given % i == 0:
            return False
  
    return True



print("This program checks to see if a given number is prime")

given = int(input("Enter the number: "))

print(prime(given))
