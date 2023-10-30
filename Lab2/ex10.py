def ex10(*lists):
    max_length = max(len(lst) for lst in lists)
    result_lists = []

    for i in range(max_length):
        tuplu_de_adaugat = tuple(lst[i] if i < len(lst) else None for lst in lists)
        result_lists.append(tuplu_de_adaugat)

    return result_lists


def main():
    list1 = [1, 2, 3]
    list2 = [5, 6, 7]
    list3 = ["a", "b", "c"]

    result = ex10(list1, list2, list3)
    print(result)


if __name__ == "__main__":
    main()
