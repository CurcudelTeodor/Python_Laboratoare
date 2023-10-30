def list_operations(a, b):
    # Intersection of a and b
    intersection = [value for value in a if value in b]

    # a U b
    union = a + [value for value in b if value not in a]

    # a - b
    a_minus_b = [value for value in a if value not in b]

    # b - a
    b_minus_a = [value for value in b if value not in a]

    return intersection, union, a_minus_b, b_minus_a


def main():
    a = [1, 2, 3, 4, 5]
    b = [3, 4, 5, 6, 7]

    intersection, union, difference_a, difference_b = list_operations(a, b)
    print("Intersection:", intersection)
    print("Union:", union)
    print("Difference A - B:", difference_a)
    print("Difference B - A:", difference_b)


if __name__ == "__main__":
    main()