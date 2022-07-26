#How would you implement the insertion sort algorithm?
"""We assume the first element in the test_listay to be sorted. The second element is stored 
separately in the key. This sorts the first two elements. You can then take the third element 
and do a comparison with the ones on the left of it. This process will go on until a point 
where we sort the test_listay."""

from os import system

system('clear')

test_list = [98, 45, 20, 77, 10, 29, 83, 7, 3 ]

for i in range(1, len(test_list)):
  
    key = test_list[i]
    j = i-1
    while j >= 0 and key < test_list[j] :
        test_list[j + 1] = test_list[j]
        j -= 1
    test_list[j + 1] = key
  
  
print(f"Sorted list is: {test_list}")
  
