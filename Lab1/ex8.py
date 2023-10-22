def count_one_bits(number):
    binary = bin(number)
    print(binary)
    count = binary.count('1')
    return count


def main():
    number = int(input("Enter a number:"))
    result = count_one_bits(number)
    print(f"Number of bits with value '1': {result}")
    return 0


if __name__ == "__main__":
    main()