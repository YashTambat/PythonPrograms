
'''

Input : arr[6] = [1, 90, 34, 89, 7, 9]
Output : 1 7 9 90 89 34

'''

array = [1, 90, 34, 89, 7, 9]
array.sort()
print(array) # op: [1, 7, 9, 34, 89, 90]
x=len(array)//2
Firsthalf =[]
Secondhalf =[]
for i in range(x):
    Firsthalf.append(array[i])
Firsthalf.sort()
for j in range(x,len(array)):
    Secondhalf.append(array[j])
Secondhalf.sort(reverse=True)
print(Firsthalf+Secondhalf)


I

