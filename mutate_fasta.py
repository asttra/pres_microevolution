#!/usr/bin/env python

import sys
import random
import argparse

#mutation functions
def mutate_base(base):
    if base == 'A':
        new_base = random.choice('CGT')
    elif base == 'C':
        new_base = random.choice('AGT')
    elif base == 'G':
        new_base = random.choice('ACT')
    else:
        new_base = random.choice('ACG')
    return new_base

def mutate(seq):
    base_list = list(seq)
    position_to_mutate = random.randint(0, len(base_list)-1)
    old_base = base_list[position_to_mutate]
    new_base = mutate_base(old_base)
    base_list[position_to_mutate] = new_base
    new_sequence = "".join(base_list)
    return new_sequence

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("bases")
    args = parser.parse_args()
    
    with open(args.bases, 'r') as fasta:
        for line in fasta:
            if line.startswith(">"):
                print('\n')
                print(line.strip())
            else:
                print('\n')
                print('Original Sequence: \n')
                print line.strip()
                print('\n')
                print('Mutated Sequence: \n')
                sequence = line.strip()
                mutated_sequence = mutate(sequence)
                print(mutated_sequence)


if __name__ == '__main__':
    main()
