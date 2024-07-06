import pickle
import sys
import os.path
import json
import math
from PIL import Image

#
# Functions
#

# check if a dimension argument is valid
def dimension_check(dimension, arg):
    try:
        dimension = int(sys.argv[sys.argv.index(arg)+1])

        if dimension < 0:
            print(f"{dimension} should be greater than 0")
    except:
        print(f"Invalid image {dimension}")
        exit()

    return dimension

# return closest value in list
def closest(lst, K):
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]

# return key for a value in dictionary
def key_from_val(dictionary, index):
    return list(dictionary.keys())[list(dictionary.values()).index(index)]

#
# Command line parameters
#

help_message = """Format command as such:\npython3 -path <image path> -height <height> -width <width>
Width and height are optional, if left default image resolution will be kept"""

# check if a path has been provided
if "-path" not in sys.argv:
    print(f"Image not provided. {help_message}")
    exit()

# iterate over command line arguments
for arg in sys.argv:
    # path variable check
    if arg == "-path":
        try:
            image = sys.argv[sys.argv.index(arg)+1]
        except:
            print(f"Image not provided. {help_message}")
    # help        
    elif arg == "-help":
        print(help_message)

    # height variable check
    elif arg == "-height":
        height = dimension_check(dimension="Height", arg=arg)

    # width variable check
    elif arg == "-width":
        width = dimension_check(dimension="Width", arg=arg)

# check if image is valid
if not os.path.isfile(image):
    print("Invalid image path")
    exit()

# load gradient from json
gradient_file = "gradient.json"

if os.path.isfile(gradient_file):
    with open(gradient_file, "r") as f:
        gradient = json.load(f)
else:
    print("No gradient file exists, create gradient with $ python3 sort_to_gradient.py")



# waiting message
print("low quality ascii hideo kojima is thinking")

im = Image.open(image, "r")
width, height = im.size

height = math.floor(height/2)

rgb_vals = list(im.getdata())

skip = 0

# remove every second line from rgb_vals
for y in range(height):
    skip += width # to skip a line

    for x in range(width): # iterate over entire line
        rgb_vals.pop(skip)

brightness_vals = []

for pixel in rgb_vals:
    # funny maths to convert rgb --> brightness
    red = pixel[0] * 0.2126
    green = pixel[1] * 0.7152
    blue = pixel[2] * 0.0722

    brightness = round(red + green + blue)

    brightness_vals.append(brightness)


# getting the min and max brightnesses of the image
image_min_brightness = min(brightness_vals)
image_max_brightness = max(brightness_vals)

# getting the min and max brightnesses of the gradient
gradient_min_brightness = gradient[list(gradient)[0]]
gradient_max_brightness = gradient[list(gradient)[-1]]

# shifting the image brightness down so the min of the image and gradient match
shifted_image_min_brightness = gradient_min_brightness
shifted_image_max_brightness = image_max_brightness - image_min_brightness + gradient_min_brightness

# determining scale factor so all brightness values of the image fit within the gradient
scale_factor = gradient_max_brightness / shifted_image_max_brightness



# constructing time!!
pixel_count = width*(height)

# if no output name is provided, set a default
if len(sys.argv) < 3:
    image_out = "image.asi"
else:
    image_out = f"{sys.argv[2]}"

asi = [height, width] # set first 2 bytes of asi file as the height and width

pos = 0

# Go through all pixels and assign the character with the closest brightness value to it
for y in range(height): # for each row
    for x in range(width): # for each column in row

        pos_brightness = brightness_vals[pos] * scale_factor # scale image pixel to fit in the character brightness range

        value = closest( list(gradient.values()), pos_brightness) # compare brightness value of the current pixel and pick the closest 
    
        char_code = key_from_val(gradient, value) # pick a character code based on the sorted gradient dictionary

        asi.append(char_code)

        #print(char_code)

        print(f"{pos+1}/{pixel_count}")

        pos += 1

# dump asi info to file
with open(image_out, "wb") as f:
    pickle.dump(asi, f)