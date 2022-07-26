#How do you reverse an array?

from os import system

system('clear')

test_list = [98, 45, 20, 77, 10, 29, 83, 7, 3 ]
second_list = []

for i in range(1,len(test_list)+1):
    second_list.append(test_list[-i])

print(second_list)