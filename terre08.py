""" module to print size of a string """
import sys

def my_strlen(string):
    ''' return size a string '''
    
    size = 0
    for _ in string:
        size+=1
    return size

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2 or sys.argv[1].isdigit():
            raise Exception
        print(my_strlen(sys.argv[1]))
    except Exception:
        print("erreur.")
