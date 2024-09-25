# Find the Prime Numbers in a Given Range in Python

'''

Given two integer as Limits, low and high, the objective is to write a code to in Python Find Prime Numbers in a Given Range in Python Language. To do so we’ll use nested loops to check for the Prime while Iterating through the range.
Example
Input : low = 2 , high = 10
Output : 2 3 5 7

'''

# numbers= [int(i) for i in input("Enter the number with space: ").split()]
# print(numbers[0] , numbers[-1])

'''

low, high = 2, 10
primes = []

for i in range(low, high + 1):
    flag = 0

    if i < 2:
        continue
    if i == 2:
        primes.append(2)
        continue

    for x in range(2, i):
        if i % x == 0:
            flag = 1
            break

    if flag == 0:
        primes.append(i)
        
print(primes)

'''

# method 2 by taking input
'''
numbers  = [int(i) for i in input("Enter the number with space : ").split()]
low, high =numbers
print(low , high)
primes = []

for i in range(low, high + 1):
    flag = 0

    if i < 2:
        continue
    if i == 2:
        primes.append(2)
        continue

    for x in range(2, i):
        if i % x == 0:
            flag = 1
            break

    if flag == 0:
        primes.append(i)
        
print(primes)


'''

# method 3: by using these formula to decide prime or not:
#  n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))


number=[int(i) for i in input("Enter the number with space : ").split()]
print(number[0],number[-1])
for num in range(number[0] , number[-1]+1):
    if num>1 and all(num%j for j in range(2,int(num**0.5)+1)):
        print(num,end="")