'''

Harshad Number
A Number that is divisible by the sum of it's digits is known as a Harshad number.
Let's try and understand it even better using an example,

Example
Input : 21
Output : Yes ' It's a Harshad Number.
Explanation : The sum of the digits of 21 is 3 i.e 2 + 1. As the number 21 is divisible by 3, It's a Harshad Number.


'''

number = int(input("Enter the number : "))
sum = 0
for i in str(number):
    sum = sum +int(i)
if number%sum ==0:
    print("Yes ' It's a Harshad Number.")
else:
    print("NO ' It's not a Harshad Number.")







































































