def print_single_table(num):
    """Prints the multiplication table for a given number from 1 to 12."""
    print(f"\nMultiplication Table for {num}:")
    for i in range(1, 13):
        print(f"{num}  x  {i:<2} =  {num * i}")


def generate_tables_up_to_n(n):
    """Prints multiplication tables for every number from 1 to N."""
    for i in range(1, n + 1):
        print_single_table(i)
        if i < n:
            print("-" * 27)


def main():
    print("=== PART A: Single Table ===")
    user_num = int(input("Enter a number: "))
    
    if user_num <= 0:
        print("Error: Please enter a positive integer.")
        return

    print_single_table(user_num)

    print("\n" + "=" * 40)
    print("=== PART B: Tables from 1 to N ===")
    n = int(input("Enter a number N: "))

    if n <= 0:
        print("Error: Please enter a positive integer.")
        return

    generate_tables_up_to_n(n)


if __name__ == "__main__":
    main()

