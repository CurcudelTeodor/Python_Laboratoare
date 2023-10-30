def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def get_primes(numbers):
    prime_numbers = []
    for num in numbers:
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers


def main():
    input_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #list(range(1, 101))
    prime_numbers = get_primes(input_numbers)
    print(prime_numbers)


if __name__ == "__main__":
    main()