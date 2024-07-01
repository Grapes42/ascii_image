# for testing screenshot dimensions

from PIL import ImageGrab
import os

ss_region = (0, 47, 30, 130)

if not os.path.exists("images"):
    os.makedirs("images")

ss_img = ImageGrab.grab(ss_region)
ss_img.save("images/test.jpg")