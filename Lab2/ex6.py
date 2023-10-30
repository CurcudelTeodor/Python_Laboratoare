def find_items_appearing_x_times(x, *lists):
    all_items = []
    for lst in lists:
        all_items.extend(lst) # A list with all the lists concatenated

    result = []
    for item in set(all_items):
        if all_items.count(item) == x: # We search in the list with all the elements
            result.append(item)

    return result


def main():
    list1 = [1, 2, 3]
    list2 = [2, 3]
    list3 = [4, 5, 6]
    list4 = [4, 1, "test"]
    x = 2

    result = find_items_appearing_x_times(x, list1, list2, list3, list4)
    print(result)  # -> [1, 2, 3, 4]


if __name__ == "__main__":
    main()
    