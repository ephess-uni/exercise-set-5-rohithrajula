""" ex_5_3.py
This module contains an entry point that:

- creates a CLi that accepts an input file of data to be processed
- shifts and scales the data to a mean of 0 and a standard deviation 1
- writes the file to the output file argument
"""
import numpy as np
import os
from argparse import ArgumentParser

if __name__ == "__main__":
    # Create your argument parser object here.
    # Collect the filename arguments from the command line
    # Rewrite your 5_3 logic here so that it utilizes the arguments passed from the command line.

    # Tests will run your command using a system call.
    # To test your program with arguments, run it from the command line
    # (see README.md for more details)

    par = ArgumentParser(description='writes the data from the inputfile to the outputfile applying a standard scale transform')
    par.add_argument('infile',help='input file path',nargs='?')
    par.add_argument('outfile',help='output file path',nargs='?')
    arg = par.parse_args()
    input = np.loadtxt(arg.infile)
    pre = (input - input.mean(axis=0))
    pos =  input.std(axis=0)
    res = pre/pos
    processed = res
    root_dir = get_repository_root()
    os.makedirs(root_dir / "outputs", exist_ok=True)
    np.savetxt(arg.outfile, processed, fmt='%.2e')
