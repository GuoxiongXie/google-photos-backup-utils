import os
import shutil

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
    source_dir = input("Enter source directory path: ")
    destination_dir = input("Enter destination directory path: ")

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    for file in os.listdir(source_dir):
        base_name, extension = os.path.splitext(file)
        source_path = os.path.join(source_dir, file)

        if file in FILES_TO_CHANGE:
            new_file_name = f"{base_name}.{TARGET_EXTENSION}"
            destination_path = os.path.join(destination_dir, new_file_name)
            shutil.move(source_path, destination_path)
        elif extension == ".json" and base_name in FILES_TO_CHANGE:
            dot_separated_base_name = base_name.split(".")
            dot_separated_base_name[-1] = TARGET_EXTENSION
            new_base_name = ".".join(dot_separated_base_name)
            new_file_name = f"{new_base_name}{extension}"
            destination_path = os.path.join(destination_dir, new_file_name)
            shutil.move(source_path, destination_path)

    print(f"Name change completed.")


if __name__ == "__main__":
    main()