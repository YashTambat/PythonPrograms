'''
arr[] = [11, 20, 35, 40, 53]
op: 
Even Elements count = 2 (20, 40)
Odd Elements count = 3 (11, 35, 53)



'''


arr1 = [11, 20, 35, 40, 53]
even = []
odd = []
for i in arr1:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
e = tuple(even)
o = tuple(odd)
print(f"{len(e)} ",e)
print(f"{len(o)} ",o)