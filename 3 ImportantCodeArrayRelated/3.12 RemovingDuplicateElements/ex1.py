'''
Removing Duplicates elements from an array
arr = [10, 20, 20, 30, 40, 40, 40, 50, 50]

output  10 20 30 40 50
'''

arr = [10, 20, 20, 30, 40, 40, 40, 50, 50]
for i in arr:
    if arr.count(i)!=1:
        arr.remove(i)
print(arr)  