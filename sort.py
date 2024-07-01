import os
import json

from PIL import Image
from PIL import ImageStat

def print_utf16(hex):
   os.system(f"env printf \'\\u{hex}\'")

# function to return brightness of image
def brightness(im_file):
   im = Image.open(im_file).convert('L')
   stat = ImageStat.Stat(im)
   return stat.mean[0]

# returns image directory as a list
images = os.listdir("char_images")

# define dictionary for all chars and their respective respective brightness value
chars = {}

# iterate over all images and add their name and respective brightness value to dictionary
for image in images:
   name = image.split(".")[0]

   chars[name] = brightness(f"char_images/{image}")

# create sorted dictionary
sorted_chars = {}
for key in sorted(chars, key=chars.get):
   sorted_chars[key] = chars[key]

# print all char codes and respective brightness value
for char in sorted_chars:
   print(f"{char}: {sorted_chars[char]}")

# print all chars
for char in sorted_chars:
   print_utf16(char)

# save sorted character dictionary to a .json
with open("gradient.json", "w") as f:
   json.dump(sorted_chars, f)