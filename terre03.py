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
    if len(sys.argv) != 2:
        print(f"usage: python3 {sys.argv[0]} letter",file=sys.stderr)
        sys.exit(-1)
    if sys.argv[1] not in string.ascii_letters:
        print("Usage: l'argument doit etre une lettre",file=sys.stderr)
        sys.exit(-1)
    print_alphabet_n(sys.argv[1],end="\n")
