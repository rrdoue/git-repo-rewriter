#! /usr/bin/env python3

"""
This module file defines some functions where the eventual goal is to process a file or other source of git
commit entries in a way that one can rewrite a git repository with the commits in order of occurrence to overwrite
compromised values, such as passwords or api keys, in any of the files.  The inbound file must be accompanied by a
directory or other source of each commit's files in their original state. 
todos: 
1. Add an env file that allows one to set all the required input values, such as the local repository directory, the 
file locations for all affected commits, and the reset --hard commit. This avoids entering arguments on the command 
line or through requesting input.
"""

import json
import os
import rewriter_utilities


def process_file():
    debug = False

    input_file_source = '/Users/rrdoue/Documents/code/python/projects/git-repo-rewriter/documentation/json/examples/'
    input_file = 'sample_rewriter_file.json'

    commit_files_source = '/Users/rrdoue/Documents/applications/git/clean_wmcontroller/files/'

    commit_dict = json.load(open(f"{input_file_source}{input_file}"))

    reversed_commit_dict = rewriter_utilities.reverse_dict(commit_dict)

    for key, value in reversed_commit_dict.items():
        print(f'{key} :')
        for subkey, subvalue in value.items():
            if subkey == 'files':
                print(f'File name(s) and location:')
                for each_file in subvalue:
                    file_directory_tree = each_file.split('/')
                    source_file = file_directory_tree[-1]
                    print(f'\t{commit_files_source}{key}/{source_file}')
            else:
                print(f'{subkey} : {subvalue}')
        print()

    if debug:
        print(f'The dictionary created from the file follows:\n\n{json.dumps(commit_dict, indent=2)}')

    if debug:
        reversed_commit_dict = rewriter_utilities.reverse_dict(commit_dict) 
        print(f'The reversed dictionary created from the file follows:\n\n{json.dumps(reversed_commit_dict, indent=2)}')

    return None
