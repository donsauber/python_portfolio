"""
01100010 01101001 01101110 01100001 
01110010 01111001 00100000 01110011 
01100101 01100001 01110010 01100011 
01101000
"""

from os import system

system('clear')

test_list = [3, 7, 10, 20, 29, 45, 77, 83, 98]
mid_point = int(len(test_list)/2)
low_point= 0
high_point=len(test_list)

print("This program does a binary search of a test list given a number to search for.")
given = int(input("Enter a positive whole number between 1 and 100:  "))

if given > test_list[-1]:
    print("Higher than the last element of the list")
elif given == test_list[-1]:
    print("Found at the last location")
elif given < test_list[0]:
    print("Lower than the first element of the list")
elif given == test_list[0]:
    print("Found at the beginning of the list")
else:
    while (low_point < high_point):
        if test_list[mid_point] == given:
            print(f"{given} is at position {mid_point}")
            break
        elif given < test_list[mid_point]:
            high_point = mid_point         
        else:
            low_point = mid_point
            
        mid_point = int((low_point + high_point)/2)
    