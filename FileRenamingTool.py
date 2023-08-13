import os
from time import time
from random import random
from math import floor

"""
Some photo service has character limits in file name and rejects long names.
The purpose of this util is to use a random int generator 
that's > # of files in directory to avoid dup and generate a relatively short name. 
File names will be changed in place.
Note that it doesn't take multiple dots in the filename in account. 
i.e. file.name.extension will be renamed to randomNumber.extension

If there's duplicate with the randomly generated name, append __{count} to the end of file name (before extension)
"""

DIR_SIZE = 10_000 # better use a number >>> # of files in directory

def main() -> None:
    directory = input("Enter source directory path (files will be renamed in place): ")
    start_time = time()
    seen_before = set()

    for file in os.listdir(directory):
        source_file_name, extension = os.path.splitext(file)
        randomized_file_name = floor(random() * DIR_SIZE)
        while randomized_file_name in seen_before:  # keep generating random name until it hasn't seen before
            randomized_file_name = floor(random() * DIR_SIZE)
        seen_before.add(randomized_file_name)
        destination_file_name = f"{randomized_file_name}{extension}"

        source_file = os.path.join(directory, file)
        destination_file = os.path.join(directory, destination_file_name)
        os.rename(source_file, destination_file)

    print(f"Name change completed. Time taken: {time() - start_time} seconds.")


if __name__ == "__main__":
    main()