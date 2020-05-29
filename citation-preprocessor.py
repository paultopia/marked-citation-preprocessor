#!/usr/bin/env python

import sys, os, re

path = os.path.dirname(os.environ['MARKED_PATH'])

outlines = []
for line in sys.stdin:
    outlines.append(line)

text = "".join(outlines)


pattern = re.compile(r"bibliography: (.*?.json)")

out = pattern.sub(r'bibliography: {}/\1'.format(path), text, count=1)

print(out)
