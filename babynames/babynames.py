#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    with open(filename, 'r') as fid:
        whole = fid.read()

    #<h3 align="center">Popularity in 1990</h3>
    #year = re.findall(r'P[\w\s]+(\d{4})\<', whole)
    year = re.findall(r'in\s(\d{4})\<', whole)

    if year is None:
        sys.stderr.write('Couldn\'t find the year!\n')
        sys.exit(1)


    #<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>

    #name_match = re.findall(r'.*><td>(\d+)</td><(.*)><(.*)>', whole)    #fid.close()
    #name_match = re.findall(r'.*><td>(\d+)</td><(\W\w+)><(\W\w+)>', whole)    #fid.close()
    name_match = re.findall(r'.*><td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', whole)

    name_rank = dict()
    for rank, boy, girl in name_match:
        if boy not in name_rank:
            name_rank[boy] = rank
        #else:
        #    raise KeyError('boy name already exists')

        # found out some of boy name is also used as girl name
        if girl not in name_rank:
            name_rank[girl] = rank
        #else:
        #    raise KeyError('girl name already exists')

    # sort by name
    name_in_order = sorted(name_rank)

    # build the list
    name_list = year + [' '.join([x, name_rank[x]]) for x in name_in_order]

    return name_list


def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if not args:
        print 'usage: [--summaryfile] file [file ...]'
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]

    dump = ''
    for file_ in args:
        print file_
        name_list = extract_names(file_)
        dump += '\n'.join(name_list)
    dump += '\n'

    if summary:
        with open('./summary.txt', 'w') as fid:
            fid.write(dump)
        print './summary.txt is created'

    # +++your code here+++
    # For each filename, get the names, then either print the text output
    # or write it to a summary file

if __name__ == '__main__':
    main()
