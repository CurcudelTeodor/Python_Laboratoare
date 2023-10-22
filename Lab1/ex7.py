import re


def extract_number(text):
    pattern = r'\d+'

    match = re.search(pattern, text)

    return int(match.group()) if match else None

def main():
    text1 = "An apple is 123 USD"
    text2 = "hj3478 asl 90 123 as"

    number1 = extract_number(text1)
    number2 = extract_number(text2)

    print("Number from text 1:", number1)
    print("Number from text 2:", number2)

    return 0


if __name__ == "__main__":
    main()