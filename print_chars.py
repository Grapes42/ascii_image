import os
import time
from PIL import ImageGrab

def print_utf16(hex):
   os.system(f"env printf \'\\u{hex}     \'")

chars = []

ss_region = (0, 47, 35, 130)

if not os.path.exists("char_images"):
    os.makedirs("char_images")

# 0x0020 --> 0x007e
# space --> tilde
i = int("0x0020", 16)

while i <= int("0x007e", 16):
    chars.append(hex(i))
    i += 1



# 0x00a1 --> 0x0408
# inverted exlamation mark --> double acute accent
i = int("0x00a1", 16)

chars.append(hex(219))

while i <= int("0x02dd", 16):
    chars.append(hex(i))
    i += 1



# 0x0370 --> 0x0408
# greek capital letter heta --> cyrillic capital letter JE
i = int("0x0370", 16)

chars.append(hex(219))

while i <= int("0x0408", 16):
    chars.append(hex(i))
    i += 1



# 0x0020 --> 0x007e
# upper half block --> quadrant upper right and lower left and lower right
i = int("0x2580", 16)

chars.append(hex(219))

while i <= int("0x259f", 16):
    chars.append(hex(i))
    i += 1


no_of_images = len(chars)
pos = 1

# printing
for char in chars:

    # convert char to string and remove "0x" prefix
    char = str(char)
    char = char.split("x")[1]

    # add "0" until char has 4 digits
    char = f"{"0"*(4-len(char))}{char}"

    # clear page and print char
    os.system("clear")
    print_utf16(char)

    # sleep so cursor isn't in screenshot
    time.sleep(0.1)

    # take screenshot of printed char
    ss_img = ImageGrab.grab(ss_region)
    ss_img.save(f"char_images/{char}.jpg")
    