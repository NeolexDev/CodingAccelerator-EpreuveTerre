""" module to convert hour from 24 to 12 """
import sys
import re

def from_24_to_12(input_string):
    ''' convert hour from 24 to 12 '''
    if not "h" in input_string and not ":" in input_string:
        print("Erreur: chaine invalide",file=sys.stderr)
        sys.exit(-1)
    (hour,minute) = re.split(r'[h:]',input_string)
    if not hour.isdigit():
        print("Erreur: nombre heure invalide",file=sys.stderr)
        sys.exit(-1)
    if not minute.isdigit():
        print("Erreur: nombre minute invalide",file=sys.stderr)
        sys.exit(-1)
    h = int(hour)
    m = int(minute)
    if h > 24:
        print("Erreur: heure invalide (h>24)",file=sys.stderr)
        sys.exit(-1)
    if m > 59:
        print("Erreur: minute invalide (m>59)",file=sys.stderr)
        sys.exit(-1)
    h12 = h
    if h == 0:
        h12=12
    if h > 12:
        h12 = h-12
    return f"{format(h12, '02')}:{format(m, '02')}{'AM' if h<12 else 'PM'}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"usage: python3 {sys.argv[0]} string",file=sys.stderr)
        sys.exit(-1)
    print(from_24_to_12(sys.argv[1]))
