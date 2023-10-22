import re

def convert_to_lowercase_with_underscores(text):

    result = re.sub('([a-z0-9])([A-Z])', r'\1_\2', text)
    result = result.lower()
    return result


def main():
    upper_camel_case = input("Enter a string in UpperCammelCase: ")
    converted_string = convert_to_lowercase_with_underscores(upper_camel_case)
    print("String in lowercase_with_underscores: ", converted_string)
    return 0


if __name__ == "__main__":
    main()