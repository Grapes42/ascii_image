import os
import sys
import pickle

with open(sys.argv[1], "rb") as f:
   asi = pickle.load(f)

height = asi[0]
width = asi[1]

pos = 2

for y in range(height):
   string = ""
   for x in range(width):
      string += f"\\u{asi[pos]}"
      pos += 1
   string += "\n"
   os.system(f"env printf \'{string}\'")