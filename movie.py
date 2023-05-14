from moviepy.editor import ImageSequenceClip
import os
from natsort import natsorted

# Set the folder path
folder_path = "image2"

# Get the list of image file names in the folder and sort them by name
image_files = natsorted([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])

# Create a list to hold the image paths
image_paths = []

# Iterate over the image files and generate the full path
for image_file in image_files:
    image_path = os.path.join(folder_path, image_file)
    image_paths.append(image_path)

# Create an ImageSequenceClip from the image paths
clip = ImageSequenceClip(image_paths, fps=10)

# Specify the output file name
output_file = "output.mp4"

# Write the video file
clip.write_videofile(output_file, codec="libx264")
