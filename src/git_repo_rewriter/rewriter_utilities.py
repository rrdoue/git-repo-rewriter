#! /usr/bin/env python3

import json


def reverse_dict(dictionary):
    '''
    Given a dictionary, return a list of the dictionary's keys in reverse order. The argument is typically the 
    dictionary created from some source, like a json-formatted file of the commits that need to be rewritten or 
    reapplied from a lost good commit file.
    '''

    return dict(reversed(dictionary.items()))


def determine_order(dictionary='None'):
    '''
    Given a dictionary, try to determine the order of the commits in the dictionary.  For example, on GitHub commits 
    are typically presented from newest to oldest. From past experience, depending on how the commits are documented, 
    the first commit could be the latest commit, and the last commit would be the first commit that contains the 
    compromised information. This suggests that the first commit may be discarded ("include": false) and the last 
    commit will contain the reset --hard value ("parent_id": "<last_good_commit>". We don't have any experience 
    retrieving commits using an automated process.
    '''

    debug = False

    incoming_dictionary = dictionary
    next_commit_id = None
    parent_id = None

    # For testing:
    input_file_source = '/Users/rrdoue/Documents/code/python/projects/git-repo-rewriter/documentation/json/examples/'
    input_file = 'sample_rewriter_file.json'

    incoming_dictionary = json.load(open(f"{input_file_source}{input_file}"))

    print('Comparing the current commit\'s parent Commit Id to the previous Commit Id.\n')
    for key, value in incoming_dictionary.items():
        if debug:
            print(f'{key} : {value}')
            print()
            print(f'Contents of Commit Id: {key}')
            for sub_key, sub_value in value.items():
                print(f'\t{sub_key} : {sub_value}')

        for sub_key, sub_value in value.items():
            if sub_key == 'parent_id':  # Note the single quotation marks
                if debug:
                    print(f'\nKey {key}, Next Id {next_commit_id}')
                if key == next_commit_id:
                    print('\nThe Commit Id matches the parent Commit Id from the previous commit.')
                else:
                    if key == list(incoming_dictionary.keys())[0]:
                        print('No match, but this is the first entry in the commit ids file and is expected.')
                    else:
                        print(
                            'No match, and this indicates a mismatch between the current commit and previous commit '
                            'from the ordering perspective in this file.  For example, a commit may be missing from '
                            'the file since the commit\'s Parent Id will always match the previous Commit Id.') 
                next_commit_id = sub_value
                if debug:
                    print()
                    print('# debug')
                    print(f'Sub Value = {sub_value}')
                    print(f'The next Commit Id should be {sub_value}.')
                    print(f'Set the next Commit Id to {next_commit_id}.')
                    print('# end debug')
                    print()

        if key == list(incoming_dictionary.keys())[-1]:
            print(f'\nReached the end of the file\'s Commit Ids.  If there is only one comparison mismatch between next '
                  f'commit id and parent id, the file is in descending order.  That is, the Commit Ids are ordered in '
                  f'descending order from latest commit to earliest commit from a time perspective.  When processing '
                  f'this file, the file contents must first be reversed, then processed from the compromised commit '
                  f'to the latest commit.') 
            print(
                f'This analysis suggests that Commit Id {next_commit_id} is the `git reset --hard <commit_id>` value, '
                f'but double check this recommendation.')
            print(f'If this recommendation is correct, set the configuration value `RESET_HARD_COMMIT_ID` to this '
                  f'value and set the configuration value `FILE_IS_REVERSED` to True.') 

    # if debug:
    #     print(f'The dictionary created from the file follows:\n\n{json.dumps(incoming_dictionary, indent=2)}')
    # 
    # if debug:
    #     reversed_commit_dict = reverse_dict(incoming_dictionary)
    #     print(f'The reversed dictionary created from the file follows:\n\n{json.dumps(reversed_commit_dict, indent=2)}')

    return None  # dictionary_order


def get_reset_commit(dictionary):

    '''
    This function is a placeholder for finding the commit used to execute the git reset --hard <commit_id> command, 
    whether executed using a process in this package or through a command line command. The value may be set manually 
    in an env or configuration file containing arguments for the automated process(es).
    '''

    pass

    return proposed_reset_commit

def create_reordered_commits_file(dictionary, file_location):

    '''
    Given the reordered dictionary from another function or other source, create a json-formatted file that represents 
    the desired commit order for using this package, in a latest to earliest commit order. Do not affect the contents 
    of the commits. 
    '''

    pass

    return reordered_commits_file_name, file_location
