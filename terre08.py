""" module to print size of a string """
import sys

def my_strlen(string):
    ''' return size a string '''
    size = 0
    for _ in string:
        size+=1
    return size

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"usage: python3 {sys.argv[0]} string",file=sys.stderr)
        sys.exit(-1)
    print(my_strlen(sys.argv[1]))
