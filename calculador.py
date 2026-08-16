def add(p, q):
    return p + q

def subtract(p, q):
    return p - q

def multiply(p, q):
    return p * q

def divide(p, q):
    return p / q

print("Select operation:")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")

choice = input("Enter choice (a/b/c/d): ")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == 'a':
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == 'b':
    print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == 'c':
    print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == 'd':
    print(num1, "/", num2, "=", divide(num1, num2))

else:
    print("Invalid input")