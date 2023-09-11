# Tool to help convert a folder to a .apworld file for use with the Archipelago randomizer.

import shutil
import os

def zip_folder(folder_path: str, zip_file_name: str) -> None:
    shutil.make_archive(zip_file_name, 'zip', folder_path)

def rename_extension(file_path: str, new_extension: str) -> None:
    base_path = os.path.splitext(file_path)[0]
    new_file_path = f"{base_path}.{new_extension}"
    os.rename(file_path, new_file_path)

def main():
    folder_path = input("Enter the folder path: ")
    zip_file_name = input("Enter the zip file name (without extension): ")

    # Zip the folder
    zip_folder(folder_path, zip_file_name)

    # Rename the zip file with the custom extension
    zip_file_path = f"{zip_file_name}.zip"
    rename_extension(zip_file_path, "apworld")

if __name__ == "__main__":
    main()