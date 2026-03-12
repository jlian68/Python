from sense_hat import SenseHat
from time import sleep
from datetime import datetime
import sys

s = SenseHat()
s.low_light=True

# Ορίζουμε τις συναρτήσεις:
def up():
  s.show_letter('U')

def down():
  s.show_letter('D')

def left():
  s.show_letter('L')
  
def right():
  s.show_letter('R')

"""
while True:
    # H stick.get_events() φτιάχνει μια λίστα με ό,τι πλήκτρο έχει πατηθεί.
    # Κάθε φορά που την καλούμε, επιστρέφει μια λίστα με τις ενέργειες που
    # είχαν γίνει στο χειριστήριο από την προηγούμενη φορά που την καλέσαμε. 
    # Η for διαβάζει και αποθηκεύει μία προς μία τις ενέργειες στην get_events().
    # Για κάθε ενέργεια που διαβάζει, εκτελεί όσες εντολές είναι μέσα στη for.
    # Η κάθε ενέργεια περιλαμβάνει τρεις τιμές. Η πρώτη είναι η timestamp,
    # η οποία περιέχει τη χρονική στιγμή που έγινε η ενέργεια.
    # Η δεύτερη είναι η direction, η οποία δηλώνει ποιο από τα 5 κουμπιά πατήθηκε.
    # Η τελευταία είναι η action που παίρνει τις τιμές:
    # pressed, αν έχουμε πατήσει το κουμπί, held, αν πατήσουμε παρατεταμένα το κουμπί,
    # και released, αν έχουμε αφήσει το κουμπί.
    for event in s.stick.get_events():
        print(datetime.fromtimestamp(event.timestamp).strftime('%H:%M:%S'), event.direction, event.action)
    sleep(0.1)
"""

try:
    while True:
        s.stick.direction_up = up
        s.stick.direction_down = down
        s.stick.direction_left = left
        s.stick.direction_right = right
        # με το μεσαίο κουμπί εκτελείται η μέθοδος s.clear
        s.stick.direction_middle = s.clear
        sleep(0.1)
except KeyboardInterrupt:
    s.clear()
    print('\b\bExiting...')
    sys.exit(0)

