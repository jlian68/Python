from sense_hat import SenseHat
from time import sleep

s = SenseHat()
s.clear()
s.low_light=True

while True:
    a=s.accel_raw
    x=round(a['x'],0)
    y=round(a['y'],0)
    z=round(a['z'],0)

    # Με την abs() παίρνουμε την απόλυτη τιμή κάθε άξονα.
    x=abs(x)
    y=abs(y)
    z=abs(z)

    # Αν τα G είναι περισσότερα από 1, τότε θα εμφανιστεί ο άξονας που βίωσε
    # αυτή την κίνηση στην οθόνη, ενώ με την print() η τιμή των G θα εμφανιστεί
    # στην κονσόλα. Μόλις εμφανίσουμε την τιμή, θα παγώσουμε την εφαρμογή με τη sleep()
    # για 1 δευτερόλεπτο, ώστε να έχουμε τον χρόνο να δούμε το όνομα του
    # άξονα, πριν τρέξει η clear() που θα αναλάβει να καθαρίσει την οθόνη.
    if x>1 :
        s.show_letter("x")
        print("x=",x)
        sleep(1)
    elif y>1:
        s.show_letter("y")
        print("y=",y)
        sleep(1)
    elif z>1:
        s.show_letter("z")
        print("z=",z)
        sleep(1)
    else:
        s.clear()
    sleep(0.1)