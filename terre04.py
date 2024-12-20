""" module that print if number is pair or impair """
import sys
def is_integer(s):
    """ Returns True if string is a number. """
    return s.replace('-','',1).isdigit()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"usage: python3 {sys.argv[0]} number",file=sys.stderr)
        sys.exit(-1)
    if not is_integer(sys.argv[1]):
        print("Erreur: l'argument doit etre un entier",file=sys.stderr)
        sys.exit(-1)
    n = int(sys.argv[1])
    if n % 2 == 0:
        print("pair")
    else:
        print("impair")
