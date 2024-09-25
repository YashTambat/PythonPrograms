
'''

Example
Input : number = 5
Output : 15
Explanation : 1 + 2 + 3 + 4 + 5 = 15


'''


# Method 1: Using for Loop
'''

number,sum = 6,0
for i in range(number+1):
  sum+=i
print(sum) # op: 21

'''

# Method 2: Using the Formula
'''

number = 6
sum  = int((number *(number+1))/2)
print(sum) # op: 21


'''

# Method 3: Using Recursion

def sumofN(num):
    if num==1:
        return 1
    else:
        return num + sumofN(num-1)
num =6
print(sumofN(num)) # op: 21