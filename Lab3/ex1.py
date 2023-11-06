def operate_on_lists(a, b):
    intersection = set(a) & set(b)
    union = set(a) | set(b)  # or set(a+b)
    a_minus_b = set(a) - set(b)
    b_minus_a = set(b) - set(a)

    result = [intersection, union, a_minus_b, b_minus_a]
    return result


def main():
    # Note: my_set = set -> output : set()
    #       my_set = {}  -> output : {}
    list_a = [1, 2, 3, 4, 5]
    list_b = [3, 4, 5, 6, 7]
    result_sets = operate_on_lists(list_a, list_b)
    print("Intersection:", result_sets[0])
    print("Union:", result_sets[1])
    print("A - B:", result_sets[2])
    print("B - A:", result_sets[3])


if __name__ == "__main__":
    main()
