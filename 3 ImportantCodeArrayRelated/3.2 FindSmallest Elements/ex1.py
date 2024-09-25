'''
Find Smallest elements in the array

'''


arr = [45 ,20, 50, 15, 10]

mini = arr[0]
for i in range(len(arr)):
    if  arr[i]<mini:
        mini=arr[i]
print(mini)
print(min(arr))