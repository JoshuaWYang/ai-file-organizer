"""
Handles AI-based file organization.
"""

import os
import shutil
import cv2

from ai_analyzer import analyze_image
from file_utils import (
    create_folder,
    get_files,
    get_file_type
)

def organize_files(base_folder):
    """
    Uses AI image recognition to sort images and videos
    into user-created categories.
    """

    number_folders = int(input("How many folders would you like to create? "))

    folder_paths = create_folders(number_folders, base_folder)

    file_list = get_files(base_folder)

    for file in file_list:
        file_type = get_file_type(file)

        if file_type == "video":
            image_path = get_thumbnail(file)
        elif file_type == "image":
            image_path = file
        else:
            print("Not a video or image")
            continue

        category = analyze_image(image_path, folder_paths)
        if category in folder_paths:
            print(category)
            shutil.move(file, folder_paths[category])
            print(f"Moved to {category}")

def create_folders(num, dir_name):
    """
    Creates folders chosen by the user.

    Returns:
        Dictionary containing folder names and paths
    """

    folder_paths = {}

    # creates folder names
    for i in range(num):
        folder_name = input(f"Name of Folder {i + 1}: ")
        folder_path = os.path.join(dir_name, folder_name)
        create_folder(dir_name, folder_name)
        folder_paths[folder_name] = folder_path

    return folder_paths

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

def get_thumbnail(video_path):
    """
    Extracts a frame from the middle of a video
    to use for AI analysis.
    """

    video = cv2.VideoCapture(video_path)

    # get video length
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    # get middle of video
    middle_frame = int(total_frames/2)

    video.set(cv2.CAP_PROP_POS_FRAMES, middle_frame)

    success, frame = video.read()
    video.release()

    if success:
        thumbnail_path = "thumbnail.jpg"
        cv2.imwrite(thumbnail_path, frame)
        return thumbnail_path

    return None