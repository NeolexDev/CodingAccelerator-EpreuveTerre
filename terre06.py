""" program that print remainder of division of two number """
import sys
def print_remainder(n1,n2):
    ''' print division resultat and remainder '''
    if n1 < n2:
        print("Erreur: n1 doit être plus grand que n2",file=sys.stderr)
        return -1
    if n2 == 0:
        print("Erreur: Division par 0 impossible",file=sys.stderr)
        return -1
    print(f"resultat = {n1//n2}")
    print(f"reste = {n1%n2}")
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"usage: python3 {sys.argv[0]} a b",file=sys.stderr)
        sys.exit(-1)
    a = sys.argv[1]
    b = sys.argv[2]
    if not a.isdigit() or not b.isdigit():
        print("Erreur: Les arguments doivent etre des entier positif",file=sys.stderr)
        sys.exit(-1)
    print_remainder(int(a),int(b))
