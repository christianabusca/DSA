num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))
num3 = float(input("Enter a number: "))

if num1 >= num2 and num1 >= num3:
    highest = num1
elif num2 >= num1 and num2 >= num3:
    highest = num2
else:
    highest = num3
print(f"The highest value among the three input values is {highest}")