x = input("Enter first number: ")
y = input("Enter second number: ")

x = float(x)
y = float(y)

# 在这里补四行 print，用 f-string
print(f"{x} + {y} = {x + y}") 
print(f"{x} - {y} = {x - y}")
print(f"{x} * {y} = {x * y}")
if y != 0:
    print(f"{x} / {y} = {x / y}")
else:
    print("Error: Division by zero is not allowed.")
