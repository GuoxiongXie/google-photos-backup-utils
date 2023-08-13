import os
from time import time
from random import random

"""
Some photo service has character limits in file name and rejects long names.
The purpose of this util is to use a random int generator 
that's > # of files in directory to avoid dup and generate a relatively short name. 
File names will be changed in place.
Note that it doesn't take multiple dots in the filename in account. 
i.e. file.name.extension will be renamed to randomNumber.extension
"""

DIR_SIZE = 10_000 # better use a number >>> # of files in directory

def main() -> None:
    directory = input("Enter source directory path (files will be renamed in place): ")
    start_time = time()

    for file in os.listdir(directory):
        source_file_name, extension = os.path.splitext(file)
        source_file_name = random() * DIR_SIZE
        destination_file_name = f"{source_file_name}{extension}"

        source_file = os.path.join(directory, file)
        destination_file = os.path.join(directory, destination_file_name)
        os.rename(source_file, destination_file)

    print(f"Name change completed. Time taken: {time() - start_time} seconds.")


if __name__ == "__main__":
    main()