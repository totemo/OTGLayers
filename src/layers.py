#!/usr/bin/env python
#------------------------------------------------------------------------------

from __future__ import print_function
import sys
import itertools

#------------------------------------------------------------------------------

def eprint(*args, **kwargs):
    '''
    Print to stderr.
    '''
    print(*args, file=sys.stderr, **kwargs)

#------------------------------------------------------------------------------

def error(*args, **kwargs):
    '''
    Print an error message beginning with ERROR: to stderr.
    '''
    eprint(*(['ERROR:'] + list(args)), **kwargs)

#------------------------------------------------------------------------------

def warning(*args, **kwargs):
    '''
    Print a warning message beginning with WARNING: to stderr.
    '''
    eprint(*(['WARNING:'] + list(args)), **kwargs)

#------------------------------------------------------------------------------

if __name__ == '__main__':
    startY = int(sys.argv[1])
    endY = int(sys.argv[2])
    replaced = sys.argv[3]
    replacements = iter(sys.argv[4:])
    y = startY
    output = 'ReplacedBlocks: '
    sep = ''
    for count, material in itertools.cycle(zip(replacements, replacements)):
        print(count, 'x', material)
        if replaced != material:
            output += sep + '(' + replaced + ',' + material + ',' + \
                      str(y) + ',' + str(y + int(count) - 1) + ')'
        sep = ','
        y += int(count)
        if y >= endY:
            break

    print('-' * 78)
    print(output)
