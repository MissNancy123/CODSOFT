def add(x, y):
    return x+y
def Subtract(x, y):
    return x-y
def Multiply(x, y):
    return x*y
def Divide(x, y):
    return x/y
print("Select Operation: ")
print("1: Add")
print("2: Subtract")
print("3: Multiply")
print("4: Divide")
choice = int(input("Enter choice(1/2/3/4): "))
num1 = int(input("Enter First num1: "))
num2 = int(input("Enter Second num2: "))
if choice == 21:
    print("Result: ", add(num1, num2))
elif choice == 2:
    print("Result: ", Subtract(num1, num2))
elif choice == 3:
    print("Result: ", Multiply(num1, num2))
elif choice == 4:
    print("Result: ", Divide(num1, num2))
else:
    print("Invalid Choice")
