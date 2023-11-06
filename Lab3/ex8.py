def loop(mapping):
    visited = set()  # to keep track of visited keys and detect loops
    result = []
    current_value = mapping.get('start')

    # check for not None because the current_value might not appear as a key in dictionary
    while current_value is not None and current_value not in visited:
        result.append(current_value)
        visited.add(current_value)
        current_value = mapping.get(current_value)  # Update the current key

    return result


def main():
    mapping = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
    result = loop(mapping)
    print(result)  # Output: ['a', '6', 'z', '2']


if __name__ == "__main__":
    main()
