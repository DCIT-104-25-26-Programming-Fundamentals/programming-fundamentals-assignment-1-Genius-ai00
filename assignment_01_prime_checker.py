def is_prime(number):
  
    if number < 2:
        return False
    
    
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
            
    return True

def main():
    user_input = int(input("Enter a number: "))
    
    if is_prime(user_input):
        print(f"{user_input} is a prime number.")
    else:
        print(f"{user_input} is NOT a prime number.")

if __name__ == "__main__":
    main()
