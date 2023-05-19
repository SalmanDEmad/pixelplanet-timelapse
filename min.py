import os
import shutil
from PIL import Image

from movie import timelapse

def fix_image(source_folder):
    destination_folder = source_folder + '_fixed'  # Set destination folder based on source folder name
    os.makedirs(destination_folder, exist_ok=True)  # Create destination folder if it doesn't exist
    target_width = 1036
    target_height = 610

    # Get a list of all image files in the source folder
    image_files = [file for file in os.listdir(source_folder) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

    # Sort the image files based on their modification time
    sorted_files = sorted(image_files, key=lambda x: os.path.getmtime(os.path.join(source_folder, x)))

    # Rename and move the files to the destination folder
    for index, filename in enumerate(sorted_files):
        new_filename = str(index + 1) + os.path.splitext(filename)[1]
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, new_filename)
        shutil.move(source_path, destination_path)

        # Open the image file
        image = Image.open(destination_path)

        # Resize the image while maintaining the aspect ratio and cropping the excess pixels
        width, height = image.size
        aspect_ratio = width / height

        if aspect_ratio > target_width / target_height:
            new_width = int(height * (target_width / target_height))
            resized_image = image.resize((new_width, target_height))
            left = (new_width - target_width) / 2
            top = 0
            right = (new_width + target_width) / 2
            bottom = target_height
        else:
            new_height = int(width * (target_height / target_width))
            resized_image = image.resize((target_width, new_height))
            left = 0
            top = (new_height - target_height) / 2
            right = target_width
            bottom = (new_height + target_height) / 2

        cropped_image = resized_image.crop((left, top, right, bottom))

        # Save the resized and cropped image
        cropped_image.save(destination_path)

    # Sort the contents of the source folder by date
    sorted_files = sorted(os.listdir(source_folder), key=lambda x: os.path.getmtime(os.path.join(source_folder, x)))

    # Print the sorted list of files in the source folder
    print("Sorted files in the source folder:")
    for filename in sorted_files:
        print(filename)

    timelapse(destination_folder)