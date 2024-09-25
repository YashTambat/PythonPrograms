
'''
Example
Input : 1221
Output : Palindrome


'''
# method 1:
'''


number = int(input("Enter here: "))
x= str(number)
y =x[::-1]
if x==y:
    print("palindrome")
else:
    print("Not a palindrome")

    '''
# method 2:

number =123321
temp = number
reverse = 0
while number>0:
    reminder =number%10
    reverse = (reverse * 10) + reminder 
    number = number // 10
if reverse==temp:
    print("palindrome")
else:
    print("Not a palindrome")