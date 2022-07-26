#How would you implement the bubble sort algorithm?

from os import system

system('clear')

test_list = [98, 45, 20, 77, 10, 29, 83, 7, 3 ]

n = len(test_list)
  
for i in range(n):
    for j in range(0, n-i-1):
        if test_list[j] > test_list[j+1]:
            test_list[j], test_list[j+1] = test_list[j+1], test_list[j]
  

print(f"Sorted list is: {test_list}")
