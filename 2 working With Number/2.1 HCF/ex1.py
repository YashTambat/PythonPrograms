

'''

HCF of Two Numbers
Here, in this section we will discuss how to find HCF of two numbers in python. 
HCF means (Highest Common Factor) also known as GCD (Greatest Common Divisor).

x is called HCF of a & b two conditions :

x can completely divide both a & b leaving remainder 0
No, other number greater than x can completely divide both a & b



'''

num1 = 36
num2 = 60
hcf = 1

for i in range(1, min(num1, num2)):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i
print("Hcf of", num1, "and", num2, "is", hcf)