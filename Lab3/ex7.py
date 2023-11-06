import pprint


def perform_set_operations(*sets):
    operations_result = {}

    for i, set_a in enumerate(sets):
        for j, set_b in enumerate(sets):
            if i != j:
                key = f"{set_a} | {set_b}"
                operations_result[key] = set_a | set_b

                key = f"{set_a} & {set_b}"
                operations_result[key] = set_a & set_b

                key = f"{set_a} - {set_b}"
                operations_result[key] = set_a - set_b

                key = f"{set_b} - {set_a}"
                operations_result[key] = set_b - set_a

    return operations_result


def main():
    result = perform_set_operations({1, 2}, {2, 3}, {3, 4}, {4, 5})
    pprint.pprint(result)


if __name__ == "__main__":
    main()
