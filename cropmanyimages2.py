import os
from PIL import Image

# cropping size
fit_size = int(input('Enter Fit Size : '))


#open folder
os.chdir('images')


# output folder
output_folder = input('Enter Folder Name : ')
os.makedirs(output_folder, exist_ok=True)

#loop over each image
for image in os.listdir('.'):
    if image.endswith(('.png','.jpg','.jpeg')):
        im = Image.open(image)
        width , height = im.size

        if width > height :
            height = int((fit_size/width)*height)
            width = fit_size
            

        else:
            width = int((fit_size/height)*width)
            height = fit_size
        
        im1 = im.resize((width, height))
        im1.save(f"{output_folder}/{image}")

