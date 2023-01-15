from PIL import Image
import os

# Set the directory where the images are located
image_dir = r"C:\Users\rexvizsla\Desktop\AI\convert_to_jpeg\input"

# Create a folder for the converted images
if not os.path.exists("output"):
    os.mkdir("output")

# Iterate through the files in the directory
for filename in os.listdir(image_dir):
    # Check if the file is an image file
    if filename.endswith(("jpg", "jpeg", "png", "bmp")):
        # Open the image file
        with Image.open(os.path.join(image_dir, filename)) as im:
            new_im = Image.new("RGB", im.size, (255, 255, 255))
            new_im.paste(im, (0,0))
            new_im.save(os.path.join("output", os.path.splitext(filename)[0]+'.jpg'))

