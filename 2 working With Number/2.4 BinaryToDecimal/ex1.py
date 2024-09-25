# Input: binary number as a string
binary_number = "1011"  #                                 2^3+ 2^2+ 2^1+ 2^0

# Convert binary to decimal
decimal_number = 0
power = 0

for digit in reversed(binary_number):
    decimal_number += int(digit) * (2 ** power)
    power += 1

# Output the decimal number
print(f"The decimal equivalent of binary {binary_number} is {decimal_number}")



n1 =input("enter the number: ")
pow =0
dec =0
for i in reversed(n1):
    dec = dec+int(i)*(2**pow)
    pow+=1

print("dec : ",dec)

