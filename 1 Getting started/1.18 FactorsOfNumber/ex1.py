'''
Example
Input : 10
Output : 2 5

'''
# method 1: Iteration
num = int(input())
for i in range(2,num):
    if num%i==0:
        print(i ,end=" ")
