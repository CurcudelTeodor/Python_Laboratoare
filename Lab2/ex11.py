def custom_sort(tuples_list):
    # custom sorting function based on the 3rd character of the 2nd element in the tuple
    def sort_key(tuple_item):
        return tuple_item[1][2] if len(tuple_item[1]) > 2 else None

    # sort the list of tuples using the custom sorting function
    sorted_tuples = sorted(tuples_list, key=sort_key)

    return sorted_tuples


def main():
    tuples_list = [('abc', 'bcd'), ('abc', 'zza'), ('abc', 'zzb')]
    sorted_list = custom_sort(tuples_list)
    print(sorted_list)


if __name__ == "__main__":
    main()
