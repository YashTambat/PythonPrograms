'''

Example
Input : Number = 12
Output : Yes, It's an Abundant Number
Explanation : The Factors for the number 12 are, 1, 2, 3, 4 and 6.
 We don't want to include the number itself.
Now the sum of the factors except the number itself is :
1 + 2 + 3 + 4 + 6 = 16
as the number 16>12 , the number itself.
It's an abundant number.


'''


number = int(input("Enter the number: "))
sum =0
for i in range(1,number):
    if number%i ==0:
        sum=sum+i
if sum>number:
    print("It's an abundant number.")
else:
    print("It's not an abundant number.")
        
































