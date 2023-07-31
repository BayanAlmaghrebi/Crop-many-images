import os
from PIL import Image

# cropping size
width = int(input('Enter Cropping Width : '))
height = int(input('Enter Cropping Height : '))

#open folder
os.chdir('images')


# output folder
output_folder = input('Enter Folder Name : ')
os.makedirs(output_folder, exist_ok=True)

#loop over each image
for image in os.listdir('.'):
    if image.endswith(('.png','.jpg','.jpeg')):
        im = Image.open(image)
        im1 = im.crop((0, 0, width, height))
        im1.save(f"{output_folder}/{image}")

