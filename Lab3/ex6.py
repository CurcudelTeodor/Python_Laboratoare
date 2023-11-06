def count_unique_and_duplicates(input_list):
    element_count = {}  # Dictionary to store the count of each element

    for num in input_list:
        if num in element_count:
            element_count[num] += 1
        else:
            element_count[num] = 1

    print(element_count)
    num_unique = len([count for count in element_count.values() if count == 1])

    num_duplicates = len([count for count in element_count.values() if count > 1])

    list_unique = list(filter(lambda count: count == 1, element_count.values()))
    list_multiple = list(filter(lambda count: count > 1, element_count.values()))

    print(list_unique)
    print(list_multiple)

    print(len(list_unique))
    print(len(list_multiple))

    return num_unique, num_duplicates


def main():
    input_list = [1, 2, 2, 3, 4, 4, 5, 2]
    result = count_unique_and_duplicates(input_list)
    print("Number of unique elements:", result[0])  # output: 3 (unique elements: 1, 3, 5)
    print("Number of duplicates:", result[1])       # output: 2 (duplicates: 2, 4)


if __name__ == "__main__":
    main()
