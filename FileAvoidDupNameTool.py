import os
from time import time

"""
When we need to merge data from Directory A to Directory B, there might already be files in Directory B that cause naming confilict.
This tool appends "__avoid_dup" to the end of file name (before file extension) to avoid naming conflicts.
Name change will be in place. 
"""

def main() -> None:
    directory = input("Enter source directory path (files will be renamed in place): ")
    start_time = time()

    for file in os.listdir(directory):
        source_file_name, extension = os.path.splitext(file)
        destination_file_name = f"{source_file_name}__avoid_dup{extension}"

        source_file = os.path.join(directory, file)
        destination_file = os.path.join(directory, destination_file_name)
        os.rename(source_file, destination_file)

    print(f"Name change completed. Time taken: {time() - start_time} seconds.")


if __name__ == "__main__":
    main()