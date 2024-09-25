'''

Example
Input : 145
Output : It's a Strong Number.
Explanation : Number = 145
145 = 1! + 4! + 5!
145 = 1 + 24 + 120

'''

'''
def factorial(num):
    if num==0:
        return 1
    return num * factorial(num-1)
num = int(input("Enter the number: "))
sum =factorial(num)
print(sum)
        
'''


def factorial(num):
    if num==0:
        return 1
    return num * factorial(num-1)
number =145
sum =0
for i in str(number):
    # print(int(i) , end=" ")
    x =factorial(int(i))
    sum = sum+x
if sum ==number:
    print("Strong number ")
else:
    print("Not a strong number")






   




