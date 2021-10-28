# Corrupted png Dimensions Bruteforcer

## Why is this tool needed?

Sometimes a PNG can be corrupted. A useful tool for checking this is [`pngcheck`](http://www.libpng.org/pub/png/apps/pngcheck.html). If you run this and find your image has invalid dimensions, like so:

```
$ pngcheck -v corrupted_image.png 
File: corrupted_image.png (84279 bytes)
  chunk IHDR at offset 0x0000c, length 13:  invalid image dimensions (0x0)
ERRORS DETECTED in corrupted_image.png
```

Then you now know why this tool exists. You can use this to simply brute force those dimensions and fix the corrupted png for you.

## Installation Instructions

```bash
wget "https://raw.githubusercontent.com/cjharris18/png-dimensions-bruteforcer/main/png_dimensions_bruteforce.py"
chmod +x ./png_dimensions_bruteforce.py
```

*Please Note: You will need to have Python3 installed as well as the required libraries, if they are not already.* 


## Why Python

Python is quite a quick language for scripting. I originally developed this script for a CTF, and have since modifified it to work nicer and be more optimized. Python has a wide plethera of libraries, which this program uses to help its calculations.

Python is also great for string manipulation, something this program uses a lot.

## How does it work?

Well, the way a PNG works is that it uses what is known as a **crc checksum** to check if a chunk is valid or not. The chunk that the dimensions are in is known as the **IHDR** chunk. So this program takes the target crc value and essentially keeps bruteforcing the image dimensions in the **IHDR** chunk, until they are valid. When they are, the **crc checksum** will be the same as our target. For more information on this, see [my writeup](https://society.cyber.warwick.ac.uk/intakectfmissingbytes/) for a CTF challenge regarding this issue.

## Usage

```bash
$ ./png_image_bruteforce.py <FILE>
```

Above is an example of the basic usage, for more complex options see `./png_image_bruteforce.py -h`.