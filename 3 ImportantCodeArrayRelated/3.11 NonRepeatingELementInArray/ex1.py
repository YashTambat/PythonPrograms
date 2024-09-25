'''

Input : arr[8] = [10, 20, 70, 90, 80, 20, 10, 20]
Output : 70 90 80
Explanation : 70, 90 and 80 are occur 1 time in the given array, 10 occurs 2 times and 20 occurs 3 times.



'''

array=  [10, 20, 70, 90, 80, 20, 10, 20]
count =1
arr2 =[]
for i in array:
    if array.count(i)==count:
        arr2.append(i)
for i in arr2:
    print(i,end=" ") # op: 70 90 80 

