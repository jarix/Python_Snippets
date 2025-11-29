# -*- coding: utf-8 -*-
"""
    Argparse 101
    
    Simple example how to use argparse module.
    Compare sizes of 2 files.

    Author: Jari Honkanen
"""
import argparse
import os

parser = argparse.ArgumentParser(description="Argparse 101")
# Required named arguments
parser.add_argument('-1', '--file1', type=str, metavar='', required=True, help='name of file 1')
parser.add_argument('-2', '--file2', type=str, metavar='', required=True, help='name of file 2')
# Mutually exclusive arguments
group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet', action='store_true', help='quiet display')
group.add_argument('-v', '--verbose', action='store_true', help='verbose display')
args = parser.parse_args()

def get_file_size(file_name):
    return os.stat(file_name).st_size

if __name__ == "__main__":
    print("argparse_101 w/ arguments: ", args)
    size1 = get_file_size(args.file1)
    size2 = get_file_size(args.file2)

    if args.quiet:
        if size1 > size2:
            print(f"{args.file1} > {args.file2}")
        else:
            print(f"{args.file1} < {args.file2}")
    elif args.verbose:
        if size1 > size2:
            print(f"file '{args.file1}', size = {size1} is larger than file '{args.file2}' size {size2}")
        else:
            print(f"file '{args.file1}', size = {size1} is smaller than file '{args.file2}' size {size2}")
    else:
        if size1 > size2:
            print(f"{args.file1} is larger than {args.file2}")
        else:
            print(f"{args.file1} is smaller than {args.file2}")
