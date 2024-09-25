'''

For Instance,
Input : 150 160
Output : 153

'''

numbers = [int(i) for i in input("Enter the range of number: ").split()]
low ,high = numbers
print(low  , high)
l1 = len(str(low))
armstrong_Arr= []
for i in range(low , high+1):
    sum = 0
    for j in str(i):
        sum = sum+(int(j)**l1)
    # print("sum : ",sum)
    if sum==int(i):
        armstrong_Arr.append(sum)
# print(armstrong_Arr)
for i in armstrong_Arr:
    print(i ,end="")

    