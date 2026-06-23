num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("the addition is", num1+num2)
elif op == "-":
    print("the subtraction is", num1-num2)
elif op == "*":
    print("the multiplication is", num1*num2)
elif op == "/":
    print("the division is", num1/num2)