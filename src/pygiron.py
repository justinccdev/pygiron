#!/usr/bin/env python

import jargparse
import rdflib

parser = jargparse.ArgParser('Graph database in Python')
parser.add_argument('path', help='path to an initial input N-Quads file')
args = parser.parse_args()

g = rdflib.Graph()
g.load(args.path, format='nt')

print len(g)
print len(g)
for s, p, o in g:
    print s, p, o