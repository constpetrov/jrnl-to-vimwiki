#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='Generate vimwiki files out of jrnl.sh journal')
parser.add_argument('-i','--input', help='Input file name',required=True)
parser.add_argument('-o','--output',help='Output directory name', required=False)
args = parser.parse_args()

#TODO Add checks if input file and output dir exist

with open(args.input, "r") as ins:
  array = []
  for line in ins:
    print(line)
