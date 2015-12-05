#!/usr/bin/env python

import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("bases")
args = parser.parse_args()

with open(args.bases, 'r') as gfp_fasta:
    for line in gfp_fasta:
        if line.startswith(">"):
            continue
        print line.strip()
