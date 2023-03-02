"""ex_5_1.py"""
try:
    from src.ex_5_0 import line_count
except ImportError:
    from ex_5_0 import line_count

import argparse
def main(infile):
    """Call line_count with the infile argument."""
    line_count(infile)


if __name__ == "__main__":
    # Create your argument parser object here.
    # Collect the filename argument from the command line
    # pass this argument to the main function above
    # Tests will run your command using a system call.
    # To test your program with arguments, run it from the command line
    # (see README.md for more details)
    par = argparse.ArgumentParser(description = 'prints no of lines in infile')
    par.add_argument('infile',help='file path',nargs='?')
    args_parse = par.parse_args()
    if args_parse.infile:
        main(args_parse.infile)
