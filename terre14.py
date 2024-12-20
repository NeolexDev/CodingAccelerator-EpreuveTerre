""" trouver la suisse """
import sys
def is_integer(s):
    """ Returns True if string is a number. """
    return s.replace('-','',1).isdigit()

def trouver_suisse(int_array):
    ''' trouver le nombre au milieu '''
    if int_array[0] > int_array[1]:
        int_array[0], int_array[1] = int_array[1],int_array[0]
    if int_array[1] > int_array[2]:
        int_array[1], int_array[2] = int_array[2],int_array[1]
    if int_array[0] > int_array[1]:
        int_array[0], int_array[1] = int_array[1],int_array[0]
    return int_array[1]

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"usage: python3 {sys.argv[0]} number number number",file=sys.stderr)
        sys.exit(-1)
    array_arg = []
    for n in sys.argv[1:]:
        if not is_integer(n):
            print("Erreur les arguments doivent être des nombres", file=sys.stderr)
        array_arg.append(int(n))
    print(trouver_suisse(array_arg))
