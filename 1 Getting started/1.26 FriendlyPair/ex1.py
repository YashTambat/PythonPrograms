'''
Friendly Pair Numbers
The numbers whose ( sum of divisors ) / number ratio is same are known as Friendly Pair Numbers.
Let's try and understand it better using an example

Example
Input : 6 28
Output : Yes, they are a friendly pair
Explanation : The factors of 6 and 28 except the numbers themselves are 1, 2, 3 and 1, 2, 4, 7, 14 respectively.
Now the sum of factors of both the numbers are 6 and 28 respectively. 
When we divide the sums with the numbers we get 1 and 1 respectively. 
As the ratio of both the number match, they are considered as a friendly pair.


'''
# Input numbers
m = int(input("Enter the number 1: "))
n = int(input("Enter the number 2: "))

# Calculate the sum of divisors for n
sum_div_n = 0
for i in range(1, n + 1):
    if n % i == 0:
        sum_div_n += i

# Calculate the sum of divisors for m
sum_div_m = 0
for i in range(1, m + 1):
    if m % i == 0:
        sum_div_m += i

# Calculate the abundancy indices
abundancy_n = sum_div_n / n
abundancy_m = sum_div_m / m

# Check if the abundancy indices are equal
if abundancy_n == abundancy_m:
    print("Yes, they are a friendly pair.")
else:
    print("No, they are not a friendly pair.")
