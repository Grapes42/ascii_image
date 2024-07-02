import os
import sys
import time

def print_utf16(hex):
   os.system(f"env printf \'\\u{hex}\'")

with open(sys.argv[1], "rb") as f:
   asi = f.read()

for byte in asi:
   char = str(hex(byte)).split("x")[1]

   char = f"{"0"*(4-len(char))}{char}"

   print_utf16(char)