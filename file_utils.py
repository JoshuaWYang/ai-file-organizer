"""
Reusable file management functions.
"""

import os

def get_files(dir_name):
    file_paths = []

    for file in os.scandir(dir_name):
        if file.is_file():
            file_paths.append(file.path)

    return file_paths

def get_file_type(file):
    """
      Determines whether a file is an image, video,
      audio file, or unsupported.
    """

    if file.lower().endswith(".mp3"):
        return "audio"

    elif file.lower().endswith((".mp4", ".mov", ".avi", ".mkv")):
        return "video"

    elif file.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
        return "image"

    else:
        return "other"

def create_folder(file_path, folder_name):
    """
    Creates a folder if it does not already exist.

    Returns:
        The folder path.
    """

    folder_path = os.path.join(file_path, folder_name)

    #Don't overwrite an existing folder
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        print(f"{folder_name} created!")
    else:
        print(f"{folder_name} already exists!")

def rename_files(folder_path):
    """
    Allows the user to rename files individually.
    """

    for file in os.listdir(folder_path):
        old_path = os.path.join(folder_path, file)
        file_name, file_extension = os.path.splitext(file)
        new_name = input(f"Enter new file name for {file_name} (or type skip): ").strip()
        new_path = os.path.join(folder_path, new_name + file_extension)

        #Skip this file
        if new_name.lower() == "skip":
            print("Skipped!")
            continue

        #Don't overwrite an existing file
        if os.path.exists(new_path):
            print("That file already exists!")
            continue

        #Rename the file
        os.rename(old_path, new_path)
        print(f"{file_name} renamed to {new_name}")
