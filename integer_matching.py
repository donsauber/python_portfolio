#How do you get the matching elements in an integer array?
from os import system

system('clear')

int_list = [1,2,3,3,4,5,6,6,6,7,8]

for i in int_list:
    if int_list.count(i) > 1:
        print(f'There are {int_list.count(i)} of {i}')