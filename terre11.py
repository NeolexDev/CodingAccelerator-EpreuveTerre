""" module to check if number is prime number """
import sys

def square_root(n):
    ''' return square root of a number '''
    res = 1
    while True:
        if res*res == int(n):
            return res
        if res > int(n):
            return None
        res+=1
    
def is_prime(n):
    ''' check if n is prime number '''
    if n < 2 or (n>2 and n%2==0):
        return False
    for i in range(3,n):
        if n%i == 0:
            return False
    return True

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise Exception
        num = sys.argv[1]
        if is_prime(int(num)):
            print(f"Oui, {num} est un  nombre premier.")
        else:
            print(f"Non, {num} n'est pas un nombre premier.")
    except Exception as e:
        print("erreur.")
