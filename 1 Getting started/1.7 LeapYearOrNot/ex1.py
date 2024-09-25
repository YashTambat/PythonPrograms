# Check if a Year is a Leap Year or Not in Python
# Example
# Input : 2020
# Output : It's a Leap Year.

'''

Conditions for a Leap Year
Here are the two conditions that any year must satisfy to be called a leap year
1. The year must be perfectly divisible by 400.
2. The number must be divisible by 4 but not by 100.


'''
# method 1:

'''

year =int(input("Enter the year number: "))
if (year%400==0) or (year%4==0 and year%100!=0):
    print("Leap year")
else:
    print("Not a leap year")


'''

#2 method: by importing calender
'''

import calendar
n = int(input("Enter the year: "))

x =calendar.isleap(n)
print(x)

if x:
    print("Leap Year")
else:
    print("Not a leap year")

    
    '''