def count_occurrences(substring, main_string):
    count = 0
    start = 0

    while True:
        start = main_string.find(substring, start)
        if start == -1:  # didn't find the substring in the main string
            break
        else:
            count = count + 1
            start = start + 1

    return count


def main():
    main_string = input("Enter the main string: ")
    substring = input("Enter the substring: ")

    number_of_occurrences = count_occurrences(substring, main_string)

    print(f"Number of occurrences of '{substring}' in the main string: {number_of_occurrences}")
    return 0


if __name__ == "__main__":
    main()
