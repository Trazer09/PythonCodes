def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        print("This operation cannot be performed")
        return None
    return x / y

print("Select operation:")
print("add")
print("subtract")
print("multiply")
print("divide")

choice = input("Enter choice (1/2/3/4): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))

if choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))

if choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))

if choice == '4':
    result = divide(num1, num2)
    if result is not None:
        print(num1, "/", num2, "=", result)
