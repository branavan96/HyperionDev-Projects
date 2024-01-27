'''
User is requested to enter three different integers.
'''

# this is where the three different integers are inputted
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# the three different outputs of the integers
print("num1: ",num1)
print("num2: ",num2)
print("num3: ",num3)

# addition of integers
sum = num1 + num2 + num3
print("sum of all 3 numbers is : ",sum)

# subtraction of num1 minus num2
subtraction = num1 - num2
print("subtraction of num2 from num1 = ",subtraction)

# multiplication of num3 bu num1
multiplication = num3*num1
print("multiplication of num3 by num1 = ",multiplication)

# division of sum of all three numbers by num3
division = sum/num3
print("division of sum by num3 = ",division)