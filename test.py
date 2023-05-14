import re
import os
import shutil
from datetime import date

today = date.today()
folder_name = today.strftime("%Y-%m-%d")

# Function to extract numbers from the link
def extract_numbers_from_link(link):
    match = re.search(r',(-?\d+),(-?\d+)', link)
    if match:
        number1 = int(match.group(1))
        number2 = int(match.group(2))
        return number1, number2
    else:
        return None

# Function to find matching files in the download folder
def find_matching_files(download_folder, number1, number2):
    matching_files = []
    for filename in os.listdir(download_folder):
        match = re.search(fr'^pixelplanet-{number1}-{number2}', filename)
        if match:
            matching_files.append(filename)
    return matching_files

# Prompt for the link input
link = input("Link for the location you want recorded: ")

# Extract numbers from the link
numbers = extract_numbers_from_link(link)
if numbers:
    number1, number2 = numbers
    print("Extracted numbers:", number1, number2)

    # Specify the path to the download folder
    download_folder = "path to where the downloaded files go normally."

    # Find matching files in the download folder
    matching_files = find_matching_files(download_folder, number1, number2)

    if matching_files:
        # Create a folder with the current date in the root directory

        folder_path = os.path.join(os.getcwd(), folder_name)
        os.makedirs(folder_path, exist_ok=True)

        print("Created folder:", folder_name)

        # Move matching files to the new folder
        for filename in matching_files:
            src_path = os.path.join(download_folder, filename)
            dst_path = os.path.join(folder_path, filename)
            shutil.move(src_path, dst_path)

            print("Moved file:", filename)
    else:
        print("No matching files found.")
else:
    print("No numbers found in the link.")
