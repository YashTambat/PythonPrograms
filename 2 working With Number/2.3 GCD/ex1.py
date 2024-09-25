

'''

GCD of Two numbers in Python
Here, in this section, we will discuss the GCD of two numbers in python. 
Basically, the GCD (Greatest Common Divisor) or HCF (highest common factor ) of two numbers is the largest positive integer 
that divides each of the integers where the user entered number should not be zero

'''



num1 = 36
num2 = 60
gcd = 1

for i in range(1, min(num1, num2)):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i
print("GCD of", num1, "and", num2, "is", gcd)