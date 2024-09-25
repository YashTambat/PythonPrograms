
'''

Check for Perfect Square in Python
Here on this page, we will learn how to Check for Perfect Square in Python programming language. 
We are given an integer number and need to print “True” if it is, otherwise “False”.



'''


number =int(input("Enter the number : "))
x=False
for i in range(1 ,number):
    if i*i==number:
        x=True
print(x)
    