'''

Check Whether or Not the Number is a Perfect Number in Python
Given an integer input as a number, the objective is to check whether or not a number is a Perfect Number in Python Language. 
Therefore, we write a program to Check Whether or Not the Number is a Perfect Number in Python Language.


'''

'''

Example
Input : 28
Divisors : [1, 2, 4, 7, 14]
Sum = 1 + 2 + 4 + 7 + 14 = 28
Output : It's a Perfect Number

'''


number =int(input("Enter the Number: "))
sum =0
for i in range(1,number):
    
    if number%i==0:
        sum =sum+i
if sum ==number:
    print("perfect Number")
else:
    print("Not a perfect Number")



















































































