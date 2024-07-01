import os

chars = []

# 0x0020 --> 0x007e
# space --> tilde
i = int("0x0020", 16)

while i <= int("0x007e", 16):
    chars.append(hex(i))
    i += 1

# 0x00a1 --> 0x0408
# inverted exlamation mark --> cyrillic capital letter JE
i = int("0x00a1", 16)

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

# printing
for char in chars:
    print(int(char, 16))
    char = str(char)

    char = char.split("x")[1]

    char = f"{"0"*(4-len(char))}{char}"

    command = f"env printf \'char: \\u{char} \n'"

    os.system(command)