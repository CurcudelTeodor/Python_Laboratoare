def most_common_letter(text):

    cleaned_string = ''.join(c for c in text if c.isalpha()).lower()

    letter_counts = {}
    for char in cleaned_string:
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1

    most_common_character = max(letter_counts, key=letter_counts.get)
    count = letter_counts[most_common_character]
    return most_common_character, count


def main():

    input_string = input("Enter a string: ")
    letter, count = most_common_letter(input_string)

    print(f"The most common letter is '{letter}' with {count} occurrences.")

    return 0


if __name__ == "__main__":
    main()