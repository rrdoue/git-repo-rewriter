#! /usr/bin/env python3

"""python-functions, Section 4, Exercise 19b: Define a function that takes one mandatory  argument, the name of an 
output file, any number of additional input file arguments,  and an optional separator argument that defaults to an 
empty string.  The function  should read all the lines in each input file and write them to the named output  
file, adding the separator in between the contents of each input file.  The test cell uses files in the current 
executable file location to avoid having to  provide a full path to the input files. """

import json
import os


def process_file():  # input_file, output_file, separator=''
    debug = False

    input_file_source = '/Users/rrdoue/Documents/code/python/projects/git-repo-rewriter/documentation/json/examples'
    input_file = 'sample_rewriter_file.json'

    if debug:
        print(f"{input_file_source}/{input_file}")

    commit_dict = json.load(open(f"{input_file_source}/{input_file}"))

    print(f'The dictionary created from the file follows:\n\n{json.dumps(commit_dict, indent=2)}')

    return None
