def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def calculate_average(numbers):
    total = calculate_sum(numbers)
    return total / len(numbers)

def find_maximum(numbers):
    max_val = numbers[0]
    for num in numbers[1:]:
        if num > max_val:
            max_val = num
    return max_val

def find_minimum(numbers):
    min_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
    return min_val

def main():
    n = int(input("How many numbers? "))
    
    
    if n <= 0:
        print("Error: Please enter a positive integer.")
        return

    numbers = []
    for i in range(1, n + 1):
        num = float(input(f"Enter number {i}: "))
        
        if num.is_integer():
            num = int(num)
        numbers.append(num)

    print("\nResults:")
    print(f"Sum:     {calculate_sum(numbers)}")
    print(f"Average: {calculate_average(numbers)}")
    print(f"Maximum: {find_maximum(numbers)}")
    print(f"Minimum: {find_minimum(numbers)}")

if __name__ == "__main__":
    main()

