'''
Input : arr[8] = [10, 20, 40, 30, 50, 20, 10, 20]
Output : 10 20
Explanation : 40, 30 and 50 are occur 1 time in the given array, 10 occurs 2 times and 20 occurs 3 times.

'''

array = [10, 20, 40, 30, 50, 20, 10, 20]
count =1
arr2 =[]
for i in array:
    if array.count(i) >count:
        arr2.append(i)
x=set(arr2)
for i in list(x):
    print(i,end=" ")