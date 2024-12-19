""" trouver la suisse """
import sys

def trouver_suisse(arr):
    ''' trouver le nombre au milieu '''
    print(arr)
    int_array = list(map(int, arr))
    if int_array[0] > int_array[1]:
        int_array[0], int_array[1] = int_array[1],int_array[0]
    print(int_array)
    if int_array[1] > int_array[2]:
        int_array[1], int_array[2] = int_array[2],int_array[1]
    if int_array[0] > int_array[1]:
        int_array[0], int_array[1] = int_array[1],int_array[0]
    return int_array[1]

if __name__ == "__main__":
    try:
        if len(sys.argv) != 4:
            raise Exception
        print(trouver_suisse(sys.argv[1:]))
    except Exception:
        print("erreur.")
