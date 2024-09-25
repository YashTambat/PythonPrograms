# Factorial of n (n!) = 1 * 2 * 3 * 4....n


# method 1: using recursion

'''
def factorial(num):
    if num==0:
        return 1
    
    return num * factorial(num-1)
num =int(input("Enter the number : "))
print("factorial of ",num,"is : ",factorial(num))

'''

#using iteration:

num =int(input("Enter the number: "))
fact = 1
if num<0:
    print("Not possible")
else:
    for i in range(1,num+1):
        fact = fact*i
        
print(f"Factorial of {num} : ",fact)
       
    