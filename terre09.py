""" module to print power of two numbers """
import sys

def power(a,b):
    ''' return power of two number '''
    i=1
    res = int(a)
    while i < int(b):
        res = res*int(a)
        i+=1
    return res
if __name__ == "__main__":
    try:
        if len(sys.argv) != 3:
            raise Exception
        print(power(sys.argv[1],sys.argv[2]))
    except Exception as e:
        print(e)
