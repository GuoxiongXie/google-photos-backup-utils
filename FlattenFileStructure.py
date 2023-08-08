import os
import shutil
from collections import defaultdict


def flatten_directory(current_dir: str, destination_dir: str, file_count: defaultdict) -> None:
    """
    Recursively flatten file structure.
    When there's a file with duplicate name (take file extension into account),
    rename file to <originalName>__<dupCount>.<fileExtension>

    current_dir: reflect the recursive tree path
    destination_dir: stays the same as the destination
    """
    for file in os.listdir(current_dir):
        item_path = os.path.join(current_dir, file)
        if os.path.isdir(item_path):  # found dir, keep going down recursion tree
            flatten_directory(item_path, destination_dir, file_count)
        else:  # leaf node
            new_file_name = handle_duplicate_file_name(file, file_count)
            destination_path = os.path.join(destination_dir, new_file_name)
            shutil.copy(item_path, destination_path)
            # print(f"Copied {item_path} to {destination_path}")  # TODO: comment out this line after debug


def handle_duplicate_file_name(file, file_count) -> str:
    """
    Checks for duplicate file name and
    when there's a file with duplicate name (take file extension into account),
    rename file to <originalName>__<dupCount>.<fileExtension>

    :param file: the file which we check for duplicate
    :param file_count: map that maintains count of file name occurrences
    :return: a new name <originalName>__<dupCount>.<fileExtension> to avoid duplicates.
    """
    new_file_name = file
    # if os.path.exists(os.path.join(destination_dir, new_file_name)):  # duplicate name found
    if file in file_count:  # duplicate name found
        updated_count = file_count.get(file, 0) + 1
        file_count[file] = updated_count
        base_name, extension = os.path.splitext(file)
        new_file_name = f"{base_name}__{updated_count}{extension}"
        print(f"MINOR: found duplicate file --- {file}, renamed to {new_file_name}")
    else:
        file_count[file] = 0  # count starts from 0, first duplicate will have __1.ext
    return new_file_name


def main() -> None:
    source_dir = input("Enter source directory path: ")
    destination_dir = input("Enter destination directory path: ")

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    file_count = defaultdict(int)  # keeps track of count of <fileName>.<fileExt> occurrences to rename duplicates
    flatten_directory(source_dir, destination_dir, file_count)
    print("Flattening and copying complete.")


if __name__ == "__main__":
    main()
