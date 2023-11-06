def count_characters(input_string):
    char_count = {}  # empty dictionary

    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        # If the character is not in the dictionary, add it with count 1
        else:
            char_count[char] = 1

        # char_count[char] = char_count.get(char, 0) + 1
    return char_count


def main():
    input_string = "Ana has apples."
    result_dict = count_characters(input_string)
    print(result_dict)


if __name__ == "__main__":
    main()
