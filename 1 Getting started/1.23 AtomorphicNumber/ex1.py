'''

Example
Input : number = 5
Output : It's an Automorphic number.
Explanation : Number = 5
Square of number = 25
as the square of the number ends with the number itself, It's an Automorphic number.


5 = (5)^2= 25  end digit =5
6 = (6)^2 =36 end digit =6
76 = (76)^2 =  5776 end digit =76 
so it num = end digit then it is atomorphic number



'''

number = int(input("Enter the number : "))
a = number*number
if str(a).endswith(str(number)):
    print(f"{number} is Atomorphic")
else:
    print(f"{number} is not Atomorphic")