""" trié ou pas """
import sys

def is_integer(s):
    """ Returns True if string is a number. """
    return s.replace('-','',1).isdigit()


def is_sorted(int_arr):
    ''' return  true is arr is sorted '''
    for i in range(1,len(int_arr)):
        if int_arr[i] < int_arr[i-1]:
            return False
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"usage: python3 {sys.argv[0]} number number ...",file=sys.stderr)
        sys.exit(-1)
    args = []
    for n in sys.argv[1:]:
        if not is_integer(n):
            print("Erreur: les arguments doivent etre des nombres entiers",file=sys.stderr)
            sys.exit(-1)
        args.append(int(n))
    if is_sorted(args):
        print("Triée !")
    else:
        print("Pas Triée !")

