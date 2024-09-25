
'''

Input : arr[8] = [10, 20, 40, 30, 50, 20, 10, 20]
Output : 5
Explanation : 10, 20, 30, 40, 50 are the distinct elements.


'''

array= [10, 20, 40, 30, 50, 20, 10, 20]
arr2 =set(array)
print(list(arr2)) # op: [40, 10, 50, 20, 30]
count =0
for i in arr2:
    count = count+1
print(count) # op: 5