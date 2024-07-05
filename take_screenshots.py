import os, shutil
import sys
import time
import csv
from PIL import ImageGrab

def print_utf16(hex):
   os.system(f"env printf \'\\u{hex}     \'")


ss_region = [0, 0, 0, 0]

with open("ss_coords.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    for row in csv_reader:
        if row[0] == "start":
            ss_region[0] = int(row[1])
            ss_region[1] = int(row[2])

        elif row[0] == "end":
            ss_region[2] = int(row[1])
            ss_region[3] = int(row[2])

if ss_region[0] > ss_region[2] or ss_region[1] > ss_region[3]:
    print("Invalid screenshot co-ordinates!\nStart should not be bigger than end")
    exit()

# make char_images directory if it doesn't exist
if os.path.exists("char_images"):
    shutil.rmtree("char_images")
os.makedirs("char_images")
    

# get char codes from csv
char_codes = []

with open(sys.argv[1], "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    for row in csv_reader:
        type = row[0]

        if type == "list":
            for char_code in row[1:]:
                char_codes.append(char_code)

        elif type == "range":
            pos = int(row[1], 16)
            end = int(row[2], 16)

            while pos <= end:
                char_code = hex(pos).replace("0x", "")

                # add "0" until char has 4 digits
                char_code = f"{"0"*(4-len(char_code))}{char_code}"

                char_codes.append(char_code)
                pos += 1


no_of_images = len(char_codes)

# printing
for char_code in char_codes:
    # clear page and print char
    os.system("clear")
    print_utf16(char_code)

    # sleep so cursor isn't in screenshot
    time.sleep(0.1)

    # take screenshot of printed char
    ss_img = ImageGrab.grab(ss_region)
    ss_img.save(f"char_images/{char_code}.jpg")
    