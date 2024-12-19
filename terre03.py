""" module that prints alphabet ending by letter in 1st argument"""
import string
import sys

def print_alphabet_n(n, end=""):
    ''' print alphabet ending by letter n'''
    for c in string.ascii_lowercase:
        print(c,end="")
        if c == n.lower():
            print(end,end="")
            return


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"usage: {sys.argv[0]} letter")
        sys.exit(-1)
    if sys.argv[1] not in string.ascii_letters:
        print("first argument should a letter")
        sys.exit(-1)
    print_alphabet_n(sys.argv[1],end="\n")
