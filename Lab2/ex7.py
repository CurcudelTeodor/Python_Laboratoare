def is_palindrome(number):
    return str(number) == str(number)[::-1]


def find_palindromes(numbers):
    palindromes = [num for num in numbers if is_palindrome(num)]

    if palindromes:
        max_palindrome = max(palindromes)
    else:
        max_palindrome = None

    return len(palindromes), max_palindrome


def main():
    numbers = [121, 123, 420024, 1331, 454, 67876, 987]
    palindrome_count, greatest_palindrome = find_palindromes(numbers)
    print("Number of palindromes found:", palindrome_count)
    print("Greatest palindrome number:", greatest_palindrome)


if __name__ == "__main__":
    main()
