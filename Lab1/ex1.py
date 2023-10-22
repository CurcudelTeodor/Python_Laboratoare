def myprint(x):
    print(x, type(x))


def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def main():
    numbers = input("Enter numbers separated by space: ").split()  # list of strings
    numbers = [int(num) for num in numbers]  # list of ints

    result = numbers[0]
    for num in numbers[1:]:
        result = gcd(result, num)

    print("Greatest common divisor:", result)


if __name__ == "__main__":
    main()
