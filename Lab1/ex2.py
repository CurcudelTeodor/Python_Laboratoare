def number_of_vowels(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0

    for character in text:
        if character in vowels:
            vowel_count = vowel_count + 1

    return vowel_count


def main():
    input_string = input("Enter a string: ")
    vowel_count = number_of_vowels(input_string)
    print(f"Number of vowels in {input_string}: {vowel_count}")
    return 0


if __name__ == "__main__":
    main()