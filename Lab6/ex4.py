import os
import sys


def count_files_by_extension(directory):
    try:
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Directory '{directory}' not found.")

        # check if the directory is empty
        if not os.listdir(directory):
            raise ValueError(f"Directory '{directory}' is empty.")

        # initialize a dictionary to store counts for each extension
        extension_counts = {}

        # iterate through all files in the directory
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)

            try:
                # check if it is a file (not a directory)
                if os.path.isfile(file_path):
                    _, file_extension = os.path.splitext(filename)

                    # Increment the count for the file extension
                    extension_counts[file_extension] = extension_counts.get(file_extension, 0) + 1
                    # if 0 is not provided as a default value -> Error accessing file E:...\Lab6_ex4\a.txt:
                    # unsupported operand type(s) for +: 'NoneType' and 'int'; NoneType -> because the key (.txt in
                    # this case) doesn't exist at first. If you put 0 ->  if file_extension is not already a key in
                    # extension_counts, the get() method returns the default value, which is 0 in this case
                    # (adds the key-value pair to the dictionary)

            except Exception as e:
                print(f"Error accessing file {file_path}: {str(e)}")

        print("File counts by extension:")
        for extension, count in extension_counts.items():
            print(f"{extension}: {count} files")

    except Exception as e:
        print(f"Error: {str(e)}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory>")
        sys.exit(1)

    # usage: python .\ex4.py "E:\Facultate\Anul 3 Sem 1\Python\exemplu_director\Lab6_ex4"

    directory = sys.argv[1]

    count_files_by_extension(directory)


if __name__ == "__main__":
    main()
