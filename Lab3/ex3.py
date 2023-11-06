# true -> equal dictionaries (same key: value pairs)
# false -> not equal dictionaries
def equal_dicts(dict1, dict2):
    if isinstance(dict1, dict) and isinstance(dict2, dict):
        # compare the keys
        if set(dict1.keys()) != set(dict2.keys()):
            return False

        # recursively compare the values in the dictionaries
        for key in dict1:
            if not equal_dicts(dict1[key], dict2[key]):
                return False

        # dictionaries are equal
        return True

    # if objects are not dictionaries, directly compare them (ex: lists, tuples, sets...)
    else:
        return dict1 == dict2


def main():
    dict1 = {
        'a': 1,
        'b': [1, 2, 3],
        'c': {
            'd': 4,
            'e': [5, 6]
        }
    }

    dict2 = {
        'c': {
                'd': 4,
                'e': [5, 6]
            },
        'a': 1,
        'b': [1, 2, 3],
    }

    dict3 = {
        'a': 1,
        'b': [1, 2, 3],
        'c': {
            'd': 4,
            'e': [5, 7]  # [5,7] != [5,6] -> false
        }
    }

    print(equal_dicts(dict1, dict2))  # true
    print(equal_dicts(dict1, dict3))  # false


if __name__ == "__main__":
    main()
    