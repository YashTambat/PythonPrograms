'''

Example
Input : 371
Output : It's an Armstrong Number


explaintion :  3^3+ 7^3 +1^3 = 371
where is depend on len of number given

'''

num = int(input("Enter the number: " ))
l=len(str(num))
sum =0
for i in str(num):
    if i.isdigit:
        sum= sum+(int(i)**int(l))

# print(sum)
if sum ==num:
    print("Armstrong")
else:
    print("Not a Armstrong")

