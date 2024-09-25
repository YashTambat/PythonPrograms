'''
Explanation :
We are given with pairs, some symmetric pairs are exists in the given set of pairs. The problem statement says that we have to find all symmetric pairs that exist
Example,
Input : arr[5][2] = {{10,20}, {30,40}, {50,60}, {20,10}, {40,30}, {90, 100}, {1, 9}, {100, 90}}
Output : (10,20) (30,40) (90, 100)

ex-2
pairs = [(3, 4), (1, 2), (5, 2), (7, 10), (4, 3), (2, 5)]
op: 
(4, 3)
(2, 5)


'''

pairs = [(3, 4), (1, 2), (5, 2), (7, 10), (4, 3), (2, 5)]
arr1 =[]
for i in pairs:
    if i and i[::-1] in pairs:
        arr1.append(i[::-1])
        pairs.remove(i)
for i in arr1:
    print(i ,end=" ")
        



