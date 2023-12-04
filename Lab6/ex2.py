import os
import sys


def rename_files(directory):
    try:
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Directory '{directory}' not found.")

        # get a list of files in the directory
        files = os.listdir(directory)

        # rename files with sequential number prefix
        for index, filename in enumerate(files, start=1):
            file_path = os.path.join(directory, filename)

            # use os.path.splitext to get the filename and extension separately
            filename_without_extension, file_extension = os.path.splitext(filename)
            new_filename = f"{filename_without_extension}{index}{file_extension}"

            try:
                # rename the file
                os.rename(file_path, os.path.join(directory, new_filename))
                print(f"Renamed: {filename} -> {new_filename}")

            except Exception as e:
                print(f"Error renaming {filename}: {str(e)}")

    except Exception as e:
        print(f"Error: {str(e)}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python ex2.py <directory>")
        sys.exit(1)

    # usage: python .\ex2.py "E:\Facultate\Anul 3 Sem 1\Python\exemplu_director\Lab6_ex2"

    directory = sys.argv[1]

    rename_files(directory)


if __name__ == "__main__":
    main()
