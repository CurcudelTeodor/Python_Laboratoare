def count_words(text):
    words = text.split(" ")
    # for word in words:
    #     print(word)
    word_count = len(words)
    return word_count


def main():
    input_text = input("Enter a text: ")
    word_count = count_words(input_text)
    print(f"Number of words in the text: {word_count}")
    return 0


if __name__ == "__main__":
    main()