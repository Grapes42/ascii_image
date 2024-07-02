import os
import sys
import time
import math   

with open(sys.argv[1], "rb") as f:
   bytes = bytearray(f.read())

height = (bin(bytes[0])
        + bin(bytes[1]).replace("0b", ""))
height = int(height, 2)

width = (bin(bytes[2])
        + bin(bytes[3]).replace("0b", ""))
width = int(width, 2)

print(f"{height}, {width}")

with open(sys.argv[1], "r") as f:
   f.seek(4)
   asi = f.read()

block_size = 4
pos = 0



for y in range(height):
   string = ""
   for x in range(width):
      char_code = ""
      for i in range(block_size):
         char_code += asi[pos]
         #print(pos)
         pos += 1
      string += f"\\u{char_code}"
   string += "\n"

   os.system(f"env printf \'{string}\'")