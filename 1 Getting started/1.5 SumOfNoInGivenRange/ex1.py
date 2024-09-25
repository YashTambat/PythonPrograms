# Find the Sum of the Numbers in a Given Range
# Given two integer inputs as the range [ low , high ], the objective is to find the sum of the numbers that lay in the intervals given by the integer inputs.
#  Therefore we’ll write a code to Find the Sum of the Numbers in a Given Range in Python Language

# Example
# Input : 2 5
# Output : 14  , explaination : 2+3+4+5 =14


num = [int(i) for i in input().split()]
# print(num) # op: [2, 5]
print(num[0] , num[-1]) # op: 2 5

sum =0
for i in range(num[0] ,num[-1]+1):  # op: 2 6
    sum = sum+i
print(sum) # op: 14

