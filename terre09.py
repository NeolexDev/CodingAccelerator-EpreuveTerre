""" module to print power of two numbers """
import sys

def is_number_isdigit(s):
    """ Returns True if string is a number. """
    return s.replace('-','',1).isdigit()

def power(a,b):
    ''' return power of two integer '''
    i=1
    res = a
    while i < b:
        res = res*a
        i+=1
    return res
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"usage: python3 {sys.argv[0]} number number")
        sys.exit(-1)
    if not is_number_isdigit(sys.argv[1]) or not is_number_isdigit(sys.argv[2]):
        print("Les arguments doivent être des nombres")
        sys.exit(-1)
    print(power(int(sys.argv[1]),int(sys.argv[2])))
