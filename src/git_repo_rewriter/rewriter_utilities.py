#! /usr/bin/env python3


def reverse_dict(dictionary):
    '''
    Given a dictionary, return a list of the dictionary's keys in reverse order. The argument is typically the 
    dictionary created from some source, like a json-formatted file of the commits that need to be rewritten or 
    reapplied from a lost good commit file.
    '''

    return dict(reversed(dictionary.items()))


def determine_order(dictionary):
    '''
    Given a dictionary, try to determine the order of the commits in the dictionary.  For example, on GitHub commits 
    are typically presented from newest to oldest. From past experience, depending on how the commits are documented, 
    the first commit could be the latest commit, and the last commit would be the first commit that contains the 
    compromised information. This suggests that the first commit may be discarded ("include": false) and the last 
    commit will contain the reset --hard value ("parent_id": "<last_good_commit>". We don't have any experience 
    retrieving commits using an automated process.
    '''

    pass

    return dictionary order

def get_reset_commit(dictionary):

    '''
    This function is a placeholder for finding the commit used to execute the git reset --hard <commit_id> command, 
    whether executed using a process in this package or through a command line command. The value may be set manually 
    in an env or configuration file containing arguments for the automated process(es).
    '''

    pass

    return proposed reset_commit

def create_reordered_commits_file(dictionary, file_location):

    '''
    Given the reordered dictionary from another function or other source, create a json-formatted file that represents 
    the desired commit order for using this package, in a latest to earliest commit order. Do not affect the contents 
    of the commits. 
    '''

    pass

    return reordered_commits_file_name, file_location
