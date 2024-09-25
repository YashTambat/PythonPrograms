
'''
Given an integer input as the number, the objective is to Find all the Prime Factors of a the given integer input number. Therefore, we’ll write a program to Find the Prime Factors of a Number in Python Language.

Example
n = 210
output: [ 2 , 3 , 5 , 7 ] only prime number is printed here
'''


num = int(input())
arr= []
for i in range(2,num):
    if num%i==0  and all(i % j for j in range(2, int(i**0.5) + 1)):

        arr.append(i)
print(arr)
