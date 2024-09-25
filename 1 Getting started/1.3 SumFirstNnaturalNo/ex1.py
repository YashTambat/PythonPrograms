'''
Example
Input : num = 8
Output : 36

Where first 8 number is 1, 2, 3, 4, 5, 6, 7, 8
Sum of numbers = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 = 36

'''

# Find the Sum of the First N Natural Numbers in Python
#  Method 1 : Using for Loop
'''
num = int(input("Enter the number :"))
sum = 0
for i in range(1,num+1):
    sum+=i
print(sum)  

'''

# Method 2 : Using Formula for the Sum of Nth Term
# Formula to Find the Sum of N terms
# Sum = ( Num * ( Num + 1 ) ) / 2

'''

Num=8
print(int(( Num * ( Num + 1 ) ) / 2))


'''

# Method 3 : Using Recursion

'''

def getSum(num):
    if num==1:
        return 1
    else:
        return num+getSum(num-1)
num =8
print(getSum(num))


'''

