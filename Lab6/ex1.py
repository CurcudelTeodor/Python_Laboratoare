import os
import sys


def read_and_print_files(directory, file_extension):
    try:
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Directory '{directory}' not found.")

        # iterate through files in the directory
        for filename in os.listdir(directory):
            # use os.path.splitext to get the file extension
            _, ext = os.path.splitext(filename)

            # check if the file has the specified extension
            if ext == file_extension:
                file_path = os.path.join(directory, filename)

                try:
                    # read and print the contents of each file
                    with open(file_path, 'r') as file:
                        contents = file.read()
                        print(f"Contents of {filename}:\n{contents}\n")

                except Exception as e:
                    print(f"Error reading file {filename}: {str(e)}")

    except Exception as e:
        print(f"Error: {str(e)}")


def main():
    if len(sys.argv) != 3:
        print(sys.argv[0])
        print(sys.argv[1])
        print(sys.argv[2])

        print("Usage: python ex1.py <directory> <file_extension>")
        sys.exit(1)

    # usage: python .\ex1.py "E:\Facultate\Anul 3 Sem 1\Python\exemplu_director" .txt

    directory = sys.argv[1]
    file_extension = sys.argv[2]

    read_and_print_files(directory, file_extension)


if __name__ == "__main__":
    main()
