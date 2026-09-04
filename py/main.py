"""
File Organizer

A file management tool that can:
1. Automatically organize images/videos using an AI vision model.
2. Remove older versions of duplicate files.
3. Rename files manually.

Uses:
- Ollama (Qwen Vision model) for image classification
- OpenCV for video thumbnails
- Python standard libraries for file management
"""

import os

from organizer import organize_files
from version_manager import remove_old_versions
from file_utils import rename_files

# -----------------------------
# Main Program
# -----------------------------

def start():
    """
    Displays the main menu and runs the selected tool
    """
    while True:

        print("\n=== File Organizer ===")

        print("What folder would you like to organize?")

        base_folder = input("Enter folder path: ").strip('"')

        if not os.path.exists(base_folder):
            print("Folder does not exist.")
            start()

        print("Which tool would you like to use?")
        print("1: Organization")
        print("2: Old Versions")
        print("3: Rename Files")

        option = int(input("> "))
        if option == 1:
            organize_files(base_folder)
            print("Organized!")
        elif option == 2:
            remove_old_versions(base_folder)
            print("Removed old versions!")
        elif option == 3:
            rename_files(base_folder)
            print("Renamed all Files!")
        else:
            print("Invalid option")
            start()

        again = input("Run another tool? (y/n): ").lower()

        if again != "y":
            print("Goodbye!")
            break

# Run program
start()
