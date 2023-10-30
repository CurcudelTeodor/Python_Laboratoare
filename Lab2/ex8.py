def generate_char_lists(x=1, strings=[], flag=True):
    def is_divisible(char_code):
        return char_code % x == 0 if flag else char_code % x != 0

    result_lists = []
    for string in strings:
        char_list = [char for char in string if is_divisible(ord(char))]
        result_lists.append(char_list)
    return result_lists


def main():
    x = 2
    strings = ["test", "hello", "lab002"]
    flag = False

    result = generate_char_lists(x, strings, flag)
    print(result)


if __name__ == "__main__":
    main()
