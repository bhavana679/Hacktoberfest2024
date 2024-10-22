def is_prime(number):
    """Returns True if the number is prime, else False."""
    if number <= 1:
        return False  # Corrected: 1 is not prime!
    for i in range(2, int(number**0.5) + 1):  # Corrected: Check up to the square root of the number
        if number % i == 0:
            return False
    return True

def sum_of_primes(limit):
    """Returns the sum of all prime numbers up to the given limit."""
    total = 0
    for num in range(2, limit):  # Corrected: Start from 2, since 1 is not prime
        if is_prime(num):
            total += num
    return total

def main():
    """Main function to demonstrate the prime number functions."""
    while True:
        try:
            number = int(input("Enter a number to check if it's prime: "))  # Added input validation
            break
        except ValueError:
            print("Invalid input! Please enter an integer.")

    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
    
    while True:
        try:
            limit = int(input("Enter the upper limit for the sum of primes: "))  # Added input validation
            if limit < 2:
                print("Limit should be at least 2.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter an integer.")

    print(f"The sum of primes up to {limit} is: {sum_of_primes(limit)}")

if __name__ == "__main__":
    main()
