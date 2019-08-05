#!/usr/bin/python

import argparse
import os

parser = argparse.ArgumentParser(description='Generate vimwiki files out of jrnl.sh journal')
parser.add_argument('-i','--input', help='Input file name',required=True)
parser.add_argument('-o','--output',help='Output directory name', required=False)
args = parser.parse_args()

if not os.path.exists(args.input):
  print("Input file doesn't exist!")
  exit(1)

if not (os.path.exists(args.output) and os.path.isdir(output)):
  print("Output path either not exist or not a directory!")
  exit(1)

with open(args.input, "r") as ins:
  array = []
  for line in ins:
    print(line)
