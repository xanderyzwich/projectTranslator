#! /bin/python
"""
This tool is designed to aid development for multilingual projects
dictionary.input file is taken in with "spanish = english" format
executable set scripts are output ( spanish2english.sh, english2spanish.sh )
"""

import string
import os

current_path = os.path.dirname(__file__)
input_file = os.path.relpath(os.path.join('..', 'io', 'dictionary.input'))
e2s_file = os.path.relpath(os.path.join('..', 'io', 'english2spanish.sh'))
s2e_file = os.path.relpath(os.path.join('..', 'io', 'spanish2english.sh'))
head = """#! /bin/bash

sed -i '
"""
foot = """' "$@"
"""

def writeBoth(s2e, e2s, string):
    """
    write the string to both writeable files
    :param s2e: writable file for spanish to english
    :param e2s: writable file for english to spanish
    :param string: string to be written
    """
    s2e.write(string)
    e2s.write(string)


def sed_each(s2e, e2s, spanish, english):
    """
    call sed_string to create sed strings for both ways
    :param s2e: writable file for spanish to english
    :param e2s: writable file for english to spanish
    :param spanish: spanish word
    :param english: english word
    """
    s2e.write(sed_string(spanish, english) + '\n')
    e2s.write(sed_string(english, spanish) + '\n')


def sed_string(find, replace):
    """
    create sed string
    :param find:
    :param replace:
    """
    return 's/%s/%s/' % (find, replace)


if __name__ == "__main__":
    with open(input_file, 'r') as dictionary, open(s2e_file, 'w') as s2e, open(e2s_file, 'w') as e2s:
        writeBoth(s2e, e2s, head)
        for line in dictionary.readlines():
            spanish, english = line.rstrip('\n').split(" = ")
            sed_each(s2e, e2s, spanish.lower(), english.lower())
            sed_each(s2e, e2s, string.capwords(spanish), string.capwords(english))
            sed_each(s2e, e2s, spanish.upper(), english.upper())
        writeBoth(s2e, e2s, foot)
    print("Output scripts can be found in ../io directory")

