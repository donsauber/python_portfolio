#How would you find the second largest number in an array?

from os import system

system('clear')

test_list = [98, 45, 20, 77, 10, 29, 83, 7, 3 ]

sorted_list = sorted(test_list)
print(f"The second largest number in {test_list} is {sorted_list[-2]}")