def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: division by zero"
    return a / b


def show_menu():
    print("\n--- Calculator Menu ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")


while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "5":
        print("Goodbye")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice, try again.")
        continue

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == "1":
        result = add(a, b)
    elif choice == "2":
        result = subtract(a, b)
    elif choice == "3":
        result = multiply(a, b)
    elif choice == "4":
        result = divide(a, b)

    print("Result:", result)