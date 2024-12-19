""" module to convert hour from 12 to 24 """
import sys
import re

def from_12_to_24(input_hour):
    ''' check if n is prime number '''
    am_or_pm = input_hour[-2:]
    (hour,minute) = re.split(':',input_hour[:-2])
    h = int(hour)
    m = int(minute)
    if am_or_pm.lower() == "pm" and h<12:
        h+=12
    elif am_or_pm.lower() == "am" and h==12:
        h=0
    return f"{format(h,'02')}:{format(m,'02')}"


if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise Exception
        print(from_12_to_24(sys.argv[1]))
    except Exception as e:
        print("erreur.")
