import os
from time import time

"""
When overlaying datetime metadata to photos, I received a lot of errors like:
Error: Not a valid HEIC (looks more like a JPEG) - ./IMG_0944.HEIC
These can be fixed by changing the file extension to .JPEG, and the corresponding metadata file
to .JPEG.json.
These two files will need to be moved to a different directory to perform the re-overlay
so that we don't need to overlay the original directory all over again (which might contains a lot of photos).
"""

TARGET_EXTENSION = "JPEG"
FILES_TO_CHANGE = {}

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