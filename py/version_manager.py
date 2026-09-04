"""
Handles duplicate file detection.
"""

import os
import shutil
import re

from file_utils import (
    get_files,
    create_folder
)

def remove_old_versions(folder_path):
    """
    Finds duplicate versions of files and moves older
    copies into an Old Versions folder.
    """

    file_groups = group_files(folder_path)
    old_versions_folder = create_folder(folder_path, "Old Versions")
    topaz_folder = create_folder(folder_path, "Topaz")
    mp3_folder = create_folder(folder_path, "Mp3")


    for file in file_groups["topaz"]:
        shutil.move(file, topaz_folder)

    for file in file_groups["mp3"]:
        shutil.move(file, mp3_folder)

    for name, files in file_groups.items():
        # Only deal with files that have multiple version
        if name == "mp3" or name == "topaz":
            continue

        if len(files) > 1:
            newest_file = max(files, key=os.path.getctime)
            for file in files:
                if file != newest_file:
                    shutil.move(file, old_versions_folder)


def group_files(folder_path):
    """
    Groups files that share the same original name.
    """

    files = get_files(folder_path)
    file_groups = {"mp3": [], "topaz": []}

    for file in files:
        if file.endswith(".MP3"):
            file_groups["mp3"].append(file)

        if file.endswith(".mp4"):
            original_name = get_original_name(file)

            if "_prob" in original_name:
                file_groups["topaz"].append(file)
                continue

            if original_name not in file_groups:
                file_groups[original_name] = []

            file_groups[original_name].append(file)

    return file_groups

def get_original_name(file_path):
    """
    Removes duplicate numbering from filenames.

    Example:
        video (1).mp4 → video.mp4
    """

    filename = os.path.basename(file_path)

    name, ext = os.path.splitext(filename)

    # removes " (1)", " (2)", etc.
    name = re.sub(r"\s*\(\d+\)$", "", name)

    return name + ext
