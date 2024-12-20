""" module to convert hour from 12 to 24 """
import sys
import re

def from_12_to_24(input_hour):
    ''' check if n is prime number '''
    if ':' not in input_hour or len(input_hour)<4:
        print("Erreur: chaine invalide",file=sys.stderr)
        sys.exit()
    am_or_pm = input_hour[-2:]
    (hour,minute) = re.split(':',input_hour[:-2])
    if not hour.isdigit():
        print("Erreur: nombre heure invalide",file=sys.stderr)
        sys.exit(-1)
    if not minute.isdigit():
        print("Erreur: nombre minute invalide",file=sys.stderr)
    h = int(hour)
    m = int(minute)
    if h > 12:
        print("Erreur: heure invalide (h>12)",file=sys.stderr)
        sys.exit(-1)
    if m > 59:
        print("Erreur: minute invalide (m>59)",file=sys.stderr)
        sys.exit(-1)
    if am_or_pm.lower() == "pm" and h<12:
        h+=12
    elif am_or_pm.lower() == "am" and h==12:
        h=0
    elif am_or_pm.lower() != "am" and am_or_pm.lower() != "pm" :
        print("Erreur: not am or pm",file=sys.stderr)
        sys.exit(-1)
    return f"{format(h,'02')}:{format(m,'02')}"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"usage: python3 {sys.argv[0]} string",file=sys.stderr)
        sys.exit(-1)
    print(from_12_to_24(sys.argv[1]))
