def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1

    while len(fib_sequence) < n:
        fib_sequence.append(a)
        a, b = b, a + b

    return fib_sequence


def main():
    n = 2
    result = fibonacci(n)
    print(result)


if __name__ == "__main__":
    main()