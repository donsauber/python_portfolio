#How would you swap two numbers without using a third variable?

from os import system

system('clear')

a = 5
b = 6
print(f"a= {a}, b= {b}")

b=b+a 
print(f"a= {a}, b= {b}")

a=b-a 
print(f"a= {a}, b= {b}")

b=b-a 
print(f"a= {a}, b= {b}")

