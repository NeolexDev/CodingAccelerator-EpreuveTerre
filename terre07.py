""" module to reverse a string """
import sys

def reverse(string):
    ''' reverse a string '''
    rev_string = ""
    for c in string[::-1]:
        rev_string += c
    return rev_string

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"usage: python3 {sys.argv[0]} string",file=sys.stderr)
        sys.exit(-1)
    print(reverse(sys.argv[1]))
