#!/usr/bin/env python3

# Created by Christopher Harris (cjharris18).
# https://github.com/cjharris18

from zlib import crc32
import argparse
import sys

# Argument Handler.
parser = argparse.ArgumentParser(description='Brute force the image dimensions of a PNG image.')
parser._action_groups.pop()
required = parser.add_argument_group('Required Arguments')

required.add_argument('FILE', help='The filename of the png image you want to bruteforce.')
required.add_argument('-c', '--checksum', help='The target checksum for the bruteforcer.', required=True)
args = parser.parse_args()

# Print a nice message to the user.
print("="*51)
print(" "*4 + "**" + " "*4 + "PNG Image Dimension Bruteforcer" + " "*4 + "**")
print(" "*15 + "Created by cjharris18")
print("="*51 + "\n")

data = open(args.FILE, 'rb').read()
index = 12

ihdr = bytearray(data[index:index+17]) #ihdr
width_index = 7 #width
height_index = 11 #height

for x in range (1,2000):
    height = bytearray(x.to_bytes(2,'big'))
    for y in range(1,2000):
        width = bytearray(y.to_bytes(2,'big'))
        for h in range(len(height)):
            ihdr[height_index - h] = height[-h -1]
        for w in range(len(width)):
            ihdr[width_index - w] = width[-w -1]
        if hex(crc32(ihdr)) == args.checksum:
            print("Found Correct Dimensions...\nWidth: {}\nHeight: {}".format(width.hex(),height.hex()))
            sys.exit()
        for i in range(len(width)):
            ihdr[width_index - i] = bytearray(b'\x00')[0]
