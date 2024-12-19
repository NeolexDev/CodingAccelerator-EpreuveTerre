""" program that print all arguments one by line """
import sys

def print_args():
    ''' print arguments one by line'''
    print('\n'.join(sys.argv[1:]))


if __name__ == "__main__":
    print_args()
