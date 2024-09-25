'''

Example
Input : 123
Output : 321

'''

#1 method:

'''
number = input("Enter the number: ")
arr = []
for i in number:
    arr.append(int(i))
x=arr[::-1]
for j in x:
    print(j ,end="")

    
'''

num =1234
temp = num
reverse = 0
while num>0:
    reminder =num%10
    print("reminder = ",reminder)
    reverse = (reverse * 10) + reminder 
    print("reverse = ",reverse)
    num = num // 10
    print("num = ",num)

print(reverse)
