import os
import json

from PIL import Image
from PIL import ImageStat

# function to return brightness of image
def brightness( im_file ):
   im = Image.open(im_file).convert('L')
   stat = ImageStat.Stat(im)
   return stat.mean[0]

# returns image directory as a list
images = os.listdir("images")

# define dictionary for all chars and their respective respective brightness value
chars = {}

# iterate over all images and add their name and respective brightness value to dictionary
for image in images:
   name = image.split(".")[0]

   chars[name] = brightness(f"images/{image}")

# create sorted dictionary
sorted_chars = {}
for key in sorted(chars, key=chars.get):
   sorted_chars[key] = chars[key]

# print all char codes and respective brightness value
for char in sorted_chars:
   print(f"{char}: {sorted_chars[char]}")

# print all chars
for char in sorted_chars:
   os.system(f"env printf \'\\u{char}\'")

# save sorted character dictionary to a .json
with open("gradient.json", "w") as f:
   json.dump(sorted_chars, f)