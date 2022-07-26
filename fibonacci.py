#Print a Fibonacci series using recursion?

from os import system

system('clear')

def fib(n):
    if (n <= 1):

        return n

    else:
        return fib(n - 1) + fib(n - 2)


fibonacci = []

print("This program will print out a Fibonacci series to a given number of places.")
places = int(input("Enter an integer: "))

for i in range(places):
    fibonacci.append(fib(i))

print(fibonacci)
