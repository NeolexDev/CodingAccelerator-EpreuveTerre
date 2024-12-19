""" program that prints its filename """
import sys
import os

def print_filename():
    ''' Function to print filename of executable '''
    print(os.path.basename(sys.argv[0]))


if __name__ == "__main__":
    print_filename()
