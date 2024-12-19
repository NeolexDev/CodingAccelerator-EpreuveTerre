""" module to convert hour from 24 to 12 """
import sys
import re

def from_24_to_12(input_number):
    ''' check if n is prime number '''
    (hour,minute) = re.split(r'[h:]',input_number)
    h = int(hour)
    m = int(minute)
    h12 = h
    if h == 0:
        h12=12
    if h > 12:
        h12 = h-12
    return f"{format(h12, '02')}:{format(m, '02')}{'AM' if h<12 else 'PM'}"

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise Exception
        print(from_24_to_12(sys.argv[1]))
    except Exception as e:
        print("erreur.")
