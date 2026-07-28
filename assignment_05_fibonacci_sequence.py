def generate_fibonacci(n):
    """Generates and prints the first N terms of the Fibonacci sequence."""
    if n <= 0:
        print("Error: Please enter a positive integer.")
        return

    sequence = []
    a, b = 0, 1
    
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    
    print("Fibonacci sequence:", " ".join(str(num) for num in sequence))


def is_fibonacci(num):
    """Checks whether a given non-negative integer is a Fibonacci number."""
    if num < 0:
        return False

    a, b = 0, 1
    while a < num:
        a, b = b, a + b

    return a == num


def main():
    print("=== PART A: Generate Fibonacci Sequence ===")
    n_terms = int(input("How many terms? "))
    generate_fibonacci(n_terms)

    print("\n" + "=" * 40)
    print("=== PART B: Check Fibonacci Number ===")
    check_num = int(input("Enter a number to check: "))

    if is_fibonacci(check_num):
        print(f"{check_num} is a Fibonacci number.")
    else:
        print(f"{check_num} is NOT a Fibonacci number.")


if __name__ == "__main__":
    main()
