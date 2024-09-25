num1 = 12
num2 = 14

# Calculating HCF here
for i in range(1, max(num1, num2)):
    if num1 % i == num2 % i == 0:
        hcf = i
# LCM formula
lcm = (num1*num2)//hcf
print("LCM of", num1, "and", num2, "is", lcm)