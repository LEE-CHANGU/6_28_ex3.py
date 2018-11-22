num1 = int(input())
num2 = int(input())

num3 = num1 & num2
num4 = num1 | num2

num3 = bin(num3)
num4 = bin(num4)

print(num3.count('1'))
print(num4.count('1'))
