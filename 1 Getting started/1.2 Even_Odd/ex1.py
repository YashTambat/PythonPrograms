# Check Whether a Number is Even or Odd in Python

# Method 1 : Using Brute Force
'''
num = int(input("Enter kr num :"))
if num%2==0:
    print("Even")
else:
    print("Odd")

'''

# Method 2 : Using Ternary Operator
'''
num =int(input("Enter kr num :"))
# print("Even" if num%2==0 else "odd")
print("Even") if num%2 == 0  else print("Odd")

'''

# Method 3 : Using Bitwise Operator
# num=11 # odd
# print(num & 1) # op: 1 1 means 0dd
# num = int(input("Enter the number :"))
# if num &1==1:
#     print("odd")
# else:
#     print("Even")

def isEven(num):
  return not num&1


num = int(input("Enter the number :"))
if isEven(num):
    print('Even')
else:
    print('Odd')