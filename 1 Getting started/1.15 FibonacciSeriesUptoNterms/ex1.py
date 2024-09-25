'''

Example
Input : 4
Output : 0 1 1 2

The series Looks like : 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 …

Its a unique sequence where the next number is the sum of previous two numbers.

Where the first two terms are always 0 and 1
In mathematical terms :
Fn = Fn-1 + Fn-2

Where,
F0 : 0
F1 : 1

'''
# Method 1: Using Simple Iteration
'''

num = 4
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")

print()

'''


def fibonacciSeries(i):
    if i <= 1:
        return i
    else:
        return (fibonacciSeries(i - 1) + fibonacciSeries(i - 2))

num=int(input("Enter the number : "))
if num <=0:
    print("Please enter a Positive Number")
else:
    print("Fibonacci Series:", end=" ")
for i in range(num):
    print(fibonacciSeries(i), end=" ")