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

    seq = ''

    parser = argparse.ArgumentParser()
    parser.add_argument("bases")
    args = parser.parse_args()
    
    with open(args.bases, 'r') as fasta:
        for line in fasta:
            if line.startswith(">"):
                print('\n')
                print('Gene Information:')
                print(line.strip())
            else:
                seq += line.strip()

        # end of for loop
        mutated_sequence = mutate(seq)
        print('\n')
        print('Mutated Sequence:')
        print(mutated_sequence)
        print('\n')


if __name__ == '__main__':
    main()
