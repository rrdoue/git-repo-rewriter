#! /usr/bin/env python3

"""
This module file defines some functions where the eventual goal is to process a file or other source of git
commit entries in a way that one can rewrite a git repository with the commits in order of occurrence to overwrite
compromised values, such as passwords or api keys, in any of the files.  The inbound file must be accompanied by a
directory or other source of each commit's files in their original state.
"""

import json
import os


def process_file():
    debug = True

    input_file_source = '/Users/rrdoue/Documents/code/python/projects/git-repo-rewriter/documentation/json/examples'
    input_file = 'sample_rewriter_file.json'

    commit_dict = json.load(open(f"{input_file_source}/{input_file}"))

    for key, value in commit_dict.items():
        print(f'{key} :')
        for subkey, subvalue in value.items():
            if subkey == 'files':
                print(f'File name(s):')
                for each_file in subvalue:
                    print(f'\tFile name: {each_file}')
            else:
                print(f'{subkey} : {subvalue}')
        print()

    if debug:
        print(f'The dictionary created from the file follows:\n\n{json.dumps(commit_dict, indent=2)}')

    return None
