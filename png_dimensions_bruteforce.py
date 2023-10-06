#!/usr/bin/env python3

# Created by Christopher Harris (cjharris18).
# https://github.com/cjharris18
# Credit to jdb_jdb for helping optimise me optimise this further.

from zlib import crc32
import argparse
import struct

MAX_WIDTH = 3200
MAX_HEIGHT = 3200

# Argument Handler.
parser = argparse.ArgumentParser(description='Brute force the image dimensions of a PNG image.')
required = parser.add_argument_group('Required Arguments')
optional = parser.add_argument_group('Optional Arguments')

required.add_argument('-f','--file', help='The filename of the png image you want to bruteforce.')
optional.add_argument('-v', '--verbose', help='Verbose mode.', action='store_true')
optional.add_argument('-o', '--output', help='Output the fixed png to a different filename.')
args = parser.parse_args()

# Print a nice message to the user.
print('='*51)
print(' '*4 + '**' + ' '*4 + 'PNG Image Dimension Bruteforcer' + ' '*4 + '**')
print(' '*15 + 'Created by cjharris18')
print('='*51 + '\n')

png = bytearray(open(args.file, 'rb').read())

# Pull the crc
crcStart = 29
crcTarget = (bytearray(png[crcStart:crcStart+4])).hex()
crcFound = False

for width in range(MAX_WIDTH):
    for height in range(MAX_HEIGHT):

        png[0x10:0x14] = struct.pack(">I",width)
        png[0x14:0x18] = struct.pack(">I",height)

        calculatedCrc = crc32(png[12:29])
        if calculatedCrc == int(crcTarget, 16):
            crcFound = True
            if args.verbose:
                print('[+] Found Correct Dimensions...\nWidth: {}\nHeight: {}'.format(width, height))
                print('\nRemember to pad this with leading 0\'s as required.')
            if args.output:
                with open(args.output,'wb') as file:
                    file.write(png)
                    print('\nSuccessfully wrote to: {}'.format(args.output))
            else:
                with open('fixed.png','wb') as file:
                    file.write(png)
                    print('\n[+] Successfully wrote to: fixed.png')
            break
    else:
        continue
    break

if (not crcFound):
    print('[-] Exhausted all dimensions up to (Width, Height): ({}, {})'.format(MAX_WIDTH, MAX_HEIGHT))