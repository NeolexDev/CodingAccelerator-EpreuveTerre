""" module to square root of number """
import sys

def square_root(n):
    ''' return square root of a number '''
    res = 1
    while True:
        if res*res == int(n):
            return res
        if res > int(n):
            return None
        res+=1

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise Exception
        print(square_root(sys.argv[1]))
    except Exception as e:
        print("erreur.")
