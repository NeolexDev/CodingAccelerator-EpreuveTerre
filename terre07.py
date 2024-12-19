""" module to reverse a string """
import sys

def reverse(string):
    ''' reverse a string '''
    rev_string = ""
    for c in string[::-1]:
        rev_string += c
    return rev_string

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise Exception
        print(reverse(sys.argv[1]))
    except Exception:
        print("erreur.")
