import cv2
import os
import re

"""
This script extracts frames from a video at a given interval and saves them as images.
"""

def images_to_video(image_folder, output_video_path, fps=3):
    """
    Combines all images in a folder into an MP4 video file with the specified FPS.
    """
    # Get all image files from the folder, sorted to maintain order
    images = sorted([img for img in os.listdir(image_folder) if img.endswith(".jpg") or img.endswith(".png")])

    # Custom sort function to extract and convert numerical parts of the filename to integers
    def sort_key(filename):
        numbers = re.findall(r'\d+', filename)
        return int(numbers[0]) if numbers else filename

    # Get all image files from the folder, sorted numerically to maintain order
    images = sorted([img for img in os.listdir(image_folder) if img.endswith(".jpg") or img.endswith(".png")], key=sort_key)
    # print("images: ", images)

    # Read the first image to determine the video size
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # For MP4 file
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))
    
    for image in images:
        frame = cv2.imread(os.path.join(image_folder, image))
        out.write(frame)  # Write the frame to the video
    
    # Release everything when job is finished
    out.release()
    print("Video creation complete.")


# Example usage
output_folder = "/home/asblab/aaron/files/hardware_trials/trial_1_images" # where the images are stored

images_to_video(output_folder, "trial_1.mp4", fps=24)

