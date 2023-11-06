def validate_dict(rules, dictionary):

    for key, prefix, middle, suffix in rules:
        if key in dictionary:
            value = dictionary[key]
            if not value.startswith(prefix) or not value.endswith(suffix):
                return False
            if middle not in value:
                return False
        else:
            continue  # skip to the next rule if key is not in the dictionary

    # check if all keys in the dictionary are specified in the rules
    keys_in_rules = {key for key, _, _, _ in rules}
    for key in dictionary.keys():
        if key not in keys_in_rules:
            return False

    return True


def main():
    rules = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
    dictionary = {
        "key1": "come inside, it's too cold out",
        "key2": "starting winter, middle of the year winter",
        "key3": "this is not valid"
    }
    result = validate_dict(rules, dictionary)
    print(result)  # Output: False


if __name__ == "__main__":
    main()
