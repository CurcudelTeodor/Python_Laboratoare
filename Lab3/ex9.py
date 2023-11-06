def my_function(*args, **keyword_args):
    values_set = set(keyword_args.values())  # create a set of keyword argument values
    count = 0

    for arg in args:
        if arg in values_set:
            count += 1

    return count


def main():
    result = my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5)
    print(result)  # Output: 3


if __name__ == "__main__":
    main()
