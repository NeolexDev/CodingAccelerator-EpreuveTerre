""" module to square root of a number """
import sys

def square_root(n1):
    ''' return square root of a number '''
    res = 1
    while True:
        if res*res == n1:
            return res
        if res > n1:
            return None
        res+=1

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"usage: python3 {sys.argv[0]} number")
        sys.exit(-1)
    if not sys.argv[1].isdigit():
        print("L'argument doivent être un entier positif")
        sys.exit(-1)
    n = square_root(int(sys.argv[1]))
    if not n:
        print(f"{sys.argv[1]} n'as pas de racine carrée")
    else:
        print(n)
