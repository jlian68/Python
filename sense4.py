from sense_hat import SenseHat
from time import sleep

s = SenseHat()
s.clear()
# Αν είμαστε σε κλειστό χώρο, ρυθμίζουμε την ένταση των LEDs ώστε να μην είναι πολύ μεγάλη.
s.low_light=True
s.show_letter('A')

while True:
    a=s.accel_raw
    x=round(a['x'],0)
    y=round(a['y'],0)
    z=round(a['z'],0)
    print("x=",x,"y=",y,"z=",z)
    sleep(1)
    # Ελέγχουμε τις τιμές των αξόνων και ρυθμίζουμε με τη set_rotation() την κατεύθυνση 
    # του περιεχομένου της οθόνης.
    if x == 1:
        s.set_rotation(270)
    elif x == -1:
        s.set_rotation(90)
    elif y == 1:
        s.set_rotation(0)
    else:
        s.set_rotation(180)
    