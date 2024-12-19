""" module to print power of two numbers """
import sys

def power(a,b):
    ''' return power of two number '''
    return int(a)**int(b)

if __name__ == "__main__":
    try:
        if len(sys.argv) != 3:
            raise Exception
        print(power(sys.argv[1],sys.argv[2]))
    except Exception:
        print("erreur.")
