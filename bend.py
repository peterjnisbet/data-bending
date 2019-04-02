# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 19:54:24 2019

@author: Pete
"""

# coding: utf-8
import os
import random

__author__ = "adrn <adrn@astro.columbia.edu>"

def simple_data_bend(input_file, output_file, grayscale=True):
    # Open file in binary mode
    f = open(input_file, "rb")
    data = f.read()
    f.close()

    # Save header separately -- probably bad to mess with the header bytes
    header = data[:1000]
    core_data = data[1000:]
    data_size = len(core_data)

    letters = "abcde"
    # Do some simple mucking about -- for example, replace all bytecode 'e' with 'b'
    for xx in range(5):
        ii = random.randint(0, data_size-1)
        jj = random.randint(ii, ii + random.randint(100, 10000))

        pre = core_data[:ii]
        post = core_data[jj:]
        # Select out a sub-sample of the data
        sub_data = core_data[ii:jj]
        sub_data = sub_data.replace(letters[random.randint(0, len(letters)-1)], letters[random.randint(0, len(letters)-1)])

        core_data = pre + sub_data + post

    f = open(output_file, "wb")
    f.write(header + core_data)
    f.close()

    # If the user wants a grayscale image, try importing PIL -- carry on if that doesn't work.
    if grayscale:
        try:
            import Image
            # Now open the image with Python Imaging Library and save it as grayscale
            im = Image.open(output_file)
            im = im.convert("1")
            im.save(output_file)
        except ImportError:
            print("Couldn't find Python Imaging Library. Install that if you want to save grayscale images.")
            pass

    return True

#if __name__ == "__main__":
#    from argparse import ArgumentParser
#
#    parser = ArgumentParser()
#    parser.add_argument("-i", "--input", dest="input_file", type=str, required=True, help="The input image filename.")
#    parser.add_argument("-o", "--output", dest="output_file", type=str, help="The output image filename.")
#    parser.add_argument("-O", "--overwrite", dest="overwrite", action="store_true", default=False, \
#        help="Overwrite the output file if it already exists.")
#    parser.add_argument("-g", "--grayscale", dest="grayscale", action="store_true", default=False, \
#        help="Save the output image as grayscale.")
#
#    args = parser.parse_args()
#
#    if not os.path.exists(args.input_file):
#        raise FileError("File {0} not found!".format(args.input_file))
#
#    if args.output_file == None:
#        in_path = os.path.dirname(args.input_file)
#        outfile = "{0}_bent{1}".format(*os.path.splitext(args.input_file))
#    else:
#        outfile = args.output_file
#
#    if os.path.exists(outfile) and not args.overwrite:
#        raise ValueError("Output file {0} already exits! If you'd like to overwrite it, use the '-O' flag".format(outfile))
#
#    simple_data_bend(args.input_file, outfile, args.grayscale)
    
input_file = 'GOPR4937.jpg'
output_file = 'output.jpg'
simple_data_bend(input_file, output_file)