import sys
import os


def calculate_total_size(directory):
    try:
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Directory '{directory}' not found.")

        total_size = 0

        # dirpath: a string that contains the path to the current directory being traversed.
        # dirnames: a list of strings representing the names of subdirectories in the current directory.
        # filenames: a list of strings representing the names of files in the current directory.
        # walk through the directory and its subdirectories
        for dirpath, dirnames, filenames in os.walk(directory):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)

                try:
                    # get the size of each file and add to the total
                    file_size = os.path.getsize(file_path)
                    total_size += file_size

                except Exception as e:
                    print(f"Error accessing file {file_path}: {str(e)}")

        print(f"Total size of all files in {directory}: {total_size} bytes")

    except Exception as e:
        print(f"Error: {str(e)}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python ex3.py <directory>")
        sys.exit(1)

    # usage: python .\ex3.py "E:\Facultate\Anul 3 Sem 1\Python\exemplu_director"

    directory = sys.argv[1]

    calculate_total_size(directory)


if __name__ == "__main__":
    main()
