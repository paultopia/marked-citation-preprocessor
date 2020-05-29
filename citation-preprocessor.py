#!/usr/bin/env python

import sys, os, re

path = os.path.dirname(os.environ['MARKED_PATH'])

def normalize_path(directory, relative_file):
    relpath = directory + "/" + relative_file
    return os.path.abspath(relpath)

def normalize_bibliography(match):
    m1 = match.group(1)
    correct_path = normalize_path(path, m1)
    return r'bibliography: {}'.format(correct_path)

outlines = []
for line in sys.stdin:
    outlines.append(line)

text = "".join(outlines)


pattern = re.compile(r"bibliography: (.*?.json)")

out = pattern.sub(normalize_bibliography, text, count=1)

print(out)
