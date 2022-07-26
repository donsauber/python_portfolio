from os import system

system('clear')


def factorial (number):
    if (number == 1):
        return 1
    else:
        return (number * factorial(number - 1))

print("Given a number, this program gives the factorial of that number.")
number=int(input("Enter a number: "))
print(f"{number}! = {factorial(number)}")