
#  Method 1: Using Brute Force
'''
n  = int(input("Enter krr bhai number :"))
if n>0:
    print("Positive")
elif n<0:
    print("Negative")
else:
    print("zero")

'''

# Method 2: Using Nested if-else Statements
'''

num  = int(input("Enter krr bhai number :"))
if num>=0:
    if num==0:
        print("zero")
    else:
        print("Positive")
else:
    print("Negative")

'''
#Method 3: Using ternary operator
num  = int(input("Enter krr bhai number :"))
print("Positive" if num>=0 else "negative") 