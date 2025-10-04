#!/usr/bin/env python3

import os
import shutil
import sys

def organize_files(directory_path):
    """
    Organizes files in the given directory into subdirectories based on their file extension.
    """
    if not os.path.isdir(directory_path):
        print(f"Error: Directory not found at {directory_path}")
        sys.exit(1)

    print(f"Organizing files in: {directory_path}")

    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()
            if not file_extension:
                target_dir = os.path.join(directory_path, "No_Extension")
            else:
                target_dir = os.path.join(directory_path, file_extension[1:].capitalize())

            os.makedirs(target_dir, exist_ok=True)
            shutil.move(file_path, target_dir)
            print(f"Moved [32m{filename}[0m to [34m{target_dir}[0m")

    print("File organization complete.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python file_organizer.py <directory_path>")
        sys.exit(1)
    
    target_directory = sys.argv[1]
    organize_files(target_directory)

