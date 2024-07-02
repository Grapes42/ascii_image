import sys
import json
import math
from PIL import Image

def closest(lst, K):
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]

def key_from_val(dictionary, index):
    return list(dictionary.keys())[list(dictionary.values()).index(index)]

with open("gradient.json", "r") as f:
    gradient = json.load(f)

print("low quality ascii hideo kojima is thinking")

image = sys.argv[1]

im = Image.open(image, "r")
width, height = im.size


rgb_vals = list(im.getdata())

skip = 0

# remove every second line from rgb_vals
for y in range( math.floor(height/2) ):
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
pixel_count = width*(height/2)

if len(sys.argv) < 3:
    image_out = "image.asi"
else:
    image_out = f"{sys.argv[2]}"

height = 100

with open(image_out, "wb") as f:
    f.write(height.to_bytes(2, "big"))
    f.write(width.to_bytes(2, "big"))

f = open(image_out, "a")

pos = 0

for y in range( math.floor(height/2) ):
    for x in range( math.floor(width) ):
        pos_brightness = brightness_vals[pos] * scale_factor

        # compare brightness value of the current pixel and pick the closest 
        value = closest( list(gradient.values()), pos_brightness)
    
        char_code = key_from_val(gradient, value)

        f.write(char_code)
        #print(char_code)

        print(f"{pos+1}/{pixel_count}")

        pos += 1

f.close()