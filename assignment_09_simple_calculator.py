def add(a, b):
    """Returns the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Returns the difference of two numbers."""
    return a - b


def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b


def divide(a, b):
    """Returns the quotient rounded to 2 decimal places, or None if division by zero."""
    if b == 0:
        return None
    return round(a / b, 2)


def modulus(a, b):
    """Returns the remainder of division, or None if modulus by zero."""
    if b == 0:
        return None
    return a % b


def exponentiate(a, b):
    """Returns a raised to the power of b."""
    return a ** b


def display_menu():
    """Displays the calculator menu."""
    print("\n============================")
    print("     SIMPLE CALCULATOR     ")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def get_numbers():
    """Helper function to prompt and return two float/int inputs."""
    a = float(input("Enter first number : "))
    b = float(input("Enter second number: "))
    
    
    if a.is_integer():
        a = int(a)
    if b.is_integer():
        b = int(b)
        
    return a, b


def main():
    while True:
        display_menu()
        choice = input("Select an operation (1-7): ").strip()

        if choice == "7":
            print("Goodbye!")
            break

        if choice in ["1", "2", "3", "4", "5", "6"]:
            num1, num2 = get_numbers()

            if choice == "1":
                res = add(num1, num2)
                print(f"Result: {num1} + {num2} = {res}")

            elif choice == "2":
                res = subtract(num1, num2)
                print(f"Result: {num1} - {num2} = {res}")

            elif choice == "3":
                res = multiply(num1, num2)
                print(f"Result: {num1} * {num2} = {res}")

            elif choice == "4":
                res = divide(num1, num2)
                if res is None:
                    print("Error: Cannot divide by zero.")
                else:
                    print(f"Result: {num1} / {num2} = {res:.2f}" if isinstance(res, float) else f"Result: {num1} / {num2} = {res}")

            elif choice == "5":
                res = modulus(num1, num2)
                if res is None:
                    print("Error: Cannot perform modulus by zero.")
                else:
                    print(f"Result: {num1} % {num2} = {res}")

            elif choice == "6":
                res = exponentiate(num1, num2)
                print(f"Result: {num1} ** {num2} = {res}")

        else:
            print("Error: Invalid choice. Please select a number from 1 to 7.")


if __name__ == "__main__":
    main()

