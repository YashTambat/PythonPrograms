'''

Finding the frequency of element Frequency of elements in an array using Python
poi
'''

arr = [10, 30, 10, 20, 10, 20, 30, 10]
arr2 = set(arr)
for i in arr2:
    print(f"{i} count : {arr.count(i)} ")
