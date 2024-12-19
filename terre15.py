""" trié ou pas """
import sys

def is_sorted(arr):
    ''' return  true is arr is sorted '''
    int_arr = list(map(int,arr))
    for i in range(1,len(int_arr)):
        if int_arr[i] < int_arr[i-1]:
            return False
    return True

if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            raise Exception
        if is_sorted(sys.argv[1:]):
            print("Triée !")
        else:
            print("Pas Triée !")
    except Exception:
        print("erreur.")
