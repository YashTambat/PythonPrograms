# Check Whether a Number is a Prime or Not in Python
# method 1: 
'''

while True:
    num = int(input("Enter the number: "))
    if num ==0:
        print("Enter number with positive and not equal to")
    flag = 0
    
    for i in range(2,num):
        if num%i==0:
            flag = 1
            break
    if flag == 1:
        print('Not Prime')
    
    else:
        print("Prime")
        break


        '''
# method 2:

def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))
n=int(input("Enter the number : "))
if is_prime(n):
    print("Prime")
else:
    print("Not a prime")