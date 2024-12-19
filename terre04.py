""" module that print if number is pair or impair """
import sys


if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            print("Tu ne me la mettras pas à l’envers.")
            sys.exit(-1)
        n = int(sys.argv[1])
        if n % 2 == 0:
            print("pair")
        else:
            print("impair")
    except ValueError:
        print("Tu ne me la mettras pas à l’envers.")
