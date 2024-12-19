""" program that print remainder of division of two number """
import sys
def print_remainder(a,b):
    ''' print division resultat and remainder '''
    try:
        a = int(a)
        b = int(b)
        if a < b:
            raise Exception("a must be equal or greater than be")
        print(f"resultat = {a//b}")
        print(f"reste = {a%b}")
    except Exception:
        print("erreur.")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Tu ne me la mettras pas à l’envers.")
        sys.exit(-1)
    print_remainder(sys.argv[1],sys.argv[2])
